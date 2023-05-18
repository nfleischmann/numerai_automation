from flask import Flask, request, abort
import boto3
import json
import os

app = Flask(__name__)

# boto3 S3 client
s3_client = boto3.client('s3')
bucket_name = os.getenv('BUCKET_NAME')

# Load model data from file
with open('model_data.json', 'r') as f:
    model_data = json.load(f)

@app.route('/upload_model', methods=['POST'])
def upload_model():
    # Check if file and name are provided
    if 'file' not in request.files or 'name' not in request.form:
        abort(400, description="Both file and name must be provided")

    file = request.files['file']
    name = request.form['name']

    # Save file to S3
    s3_client.upload_fileobj(file, bucket_name, f'{name}.pt')

    # Save model data
    model_data.append({
        'name': name,
        's3_location': f's3://{bucket_name}/{name}.pt'
    })

    # Write model data to file
    with open('model_data.json', 'w') as f:
        json.dump(model_data, f)

    return 'Model uploaded successfully', 200

@app.route('/delete_model', methods=['DELETE'])
def delete_model():
    name = request.form['name']

    # Check if name exists in model data
    if not any(d['name'] == name for d in model_data):
        abort(400, description="Model name not found")

    # Delete file from S3
    s3_client.delete_object(Bucket=bucket_name, Key=f'{name}.pt')

    # Remove model data
    model_data[:] = [d for d in model_data if d.get('name') != name]

    # Write model data to file
    with open('model_data.json', 'w') as f:
        json.dump(model_data, f)

    return 'Model deleted successfully', 200

@app.route('/list_models', methods=['GET'])
def list_models():
    # Return model data as JSON
    return json.dumps(model_data), 200
