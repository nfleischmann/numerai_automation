import os
import numerapi
import pandas as pd
import torch
import boto3
import json

# Set up NumerAPI
public_id = os.getenv('NUMERAI_PUBLIC_ID')
secret_key = os.getenv('NUMERAI_SECRET_KEY')
napi = numerapi.NumerAPI(public_id, secret_key)

# Step 1: Download new data from Numerai API
dataset_path = "live.parquet"
napi.download_dataset("v4/live.parquet", dataset_path)
data = pd.read_parquet(dataset_path)

# Only keep columns that start with "feature"
features = data.columns[data.columns.str.startswith('feature')]
data = data[features]

# Step 2: Load model data from file
with open('model_data.json', 'r') as f:
    model_data = json.load(f)

# boto3 S3 client
s3_client = boto3.client('s3')

# Step 3: Iterate over models and make predictions
for model_info in model_data:
    # Download the model from the S3 bucket
    model_name = model_info['name']
    s3_location = model_info['s3_location']
    local_model_path = f"{model_name}.pt"
    bucket_name, model_key = s3_location.replace('s3://', '').split('/', 1)
    s3_client.download_file(bucket_name, model_key, local_model_path)

    # Load the model and do inference on the new data
    model = torch.jit.load(local_model_path)

    # Create a DataFrame to hold the predictions
    predictions = pd.DataFrame(index=data.index, columns=['prediction'])

    # Iterate over rows and make predictions
    for idx, row in data.iterrows():
        predictions.loc[idx, 'prediction'] = model(torch.tensor(row.values))

    # Step 4: Upload predictions to Numerai API
    predictions.to_csv(f"{model_name}_predictions.csv")
    model_id = napi.get_models()[model_name]
    napi.upload_predictions(f"{model_name}_predictions.csv", model_id=model_id)
