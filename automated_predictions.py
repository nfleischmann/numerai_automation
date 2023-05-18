import configparser
import numerapi
import pandas as pd
import torch
import json

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')
public_id = config.get('NumerAPI', 'PublicID')
secret_key = config.get('NumerAPI', 'SecretKey')

# Set up NumerAPI
napi = numerapi.NumerAPI(public_id, secret_key)

# Step 1: Download new data from Numerai API
current_round = napi.get_current_round()
dataset_path = f"tournament_data/live_int8_{current_round}.parquet"
napi.download_dataset("v4.1/live_int8.parquet", dataset_path)
data = pd.read_parquet(dataset_path)

# Only keep columns that start with "feature"
features = data.columns[data.columns.str.startswith('feature')]
data = data[features].astype('int8')

# Step 2: Load model data from file
with open('model_data.json', 'r') as f:
    model_data = json.load(f)

# Step 3: Iterate over models and make predictions
for model_info in model_data:
    # Download the model from the S3 bucket
    model_name = model_info['name']
    s3_location = model_info['s3_location']
    numerai_id = model_info['numerai_id']
    local_model_path = f"models/{model_name}.pt"

    # Load the model and do inference on the new data
    model = torch.jit.load(local_model_path)

    # Create a DataFrame to hold the predictions
    predictions = pd.DataFrame(index=data.index, columns=['prediction'])

    # Iterate over rows and make predictions
    for idx, row in data.iterrows():
        predictions.loc[idx, 'prediction'] = model(torch.tensor(row.values))

    # Step 4: Upload predictions to Numerai API
    predictions.to_csv(f"predictions/{model_name}_predictions.csv")
    napi.upload_predictions(f"predictions/{model_name}_predictions.csv", model_id=numerai_id)
