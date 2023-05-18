from flask import Flask, request, abort
import json
import os

app = Flask(__name__)

# Local models directory
models_dir = 'models'

# Load model data from file
with open('model_data.json', 'r') as f:
    model_data = json.load(f)

@app.route('/upload_model', methods=['POST'])
def upload_model():
    # Check if file, name, and numeral_id are provided
    if 'file' not in request.files or 'name' not in request.form or 'numeral_id' not in request.form:
        abort(400, description="File, name and numeral_id must be provided")

    file = request.files['file']
    name = request.form['name']
    numeral_id = request.form['numeral_id']

    # Save file locally
    file.save(os.path.join(models_dir, f'{name}.pt'))

    # Save model data
    model_data.append({
        'name': name,
        'numeral_id': numeral_id,
        'location': f'{models_dir}/{name}.pt'
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

    # Delete file locally
    os.remove(os.path.join(models_dir, f'{name}.pt'))

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
