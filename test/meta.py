import requests

# Base URL of your deployed machine learning application
base_url = 'http://localhost:8000'

# Model version and metadata
model_version = 'v1'
model_metadata = {
    'version': model_version,
    'description': 'Model trained on XYZ dataset'
}

def deploy_model():
    # Define the model deployment request payload
    deployment_data = {
        'model_version': model_version,
        'model_metadata': model_metadata
    }
    
    # Send a POST request to the deployment endpoint
    response = requests.post(f'{base_url}/quesion', json=deployment_data)
    
    # Check the response status code
    assert response.status_code == 200
    
    print('Model deployed successfully!')

def get_model_version():
    # Send a GET request to the model version endpoint
    response = requests.get(f'{base_url}/version')
    
    # Check the response status code
    assert response.status_code == 200
    
    # Get the model version from the response
    model_version = response.json()['version']
    
    return model_version

def update_model_metadata(new_metadata):
    # Send a PUT request to the model metadata endpoint
    response = requests.put(f'{base_url}/metadata', json=new_metadata)
    
    # Check the response status code
    assert response.status_code == 200
    
    print('Model metadata updated successfully!')

# Deploy the model
deploy_model()

# Get the current model version
current_model_version = get_model_version()
print('Current Model Version:', current_model_version)

# Update the model metadata
new_metadata = {
    'version': 'v2',
    'description': 'Updated model trained on ABC dataset'
}
update_model_metadata(new_metadata)
