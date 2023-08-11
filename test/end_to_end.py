import requests

# Base URL of your deployed machine learning application
base_url = 'http://localhost:8000'

def test_prediction():
    # Define the input data for testing
    data = {
        'question': 'سلام، من موقع نماز حالم بد شد، چکار کنم؟'
    }
    
    # Send a POST request to the prediction endpoint
    response = requests.post(f'{base_url}/question', json=data)
    
    # Check the response status code
    assert response.status_code == 200
    
    # Get the predicted result from the response
    prediction = response.json()['quesion']
    prediction2 = response.json()['answer']
    
    # Perform assertions or checks on the predicted result
    assert prediction == 'expected_prediction'
    
    print('Prediction test passed!')

# Run the end-to-end tests
test_prediction()
