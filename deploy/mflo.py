import mlflow
from deploy import model
# Set the tracking URI
mlflow.set_tracking_uri('http://localhost:8000')

# Start an MLflow experiment
mlflow.set_experiment('my_experiment')

# Log parameters, metrics, and artifacts
with mlflow.start_run():
    mlflow.log_param('learning_rate', 0.01)
    
    # Training code here
    
    mlflow.log_metric('accuracy', 0.85)
    
    # Save the trained model
    mlflow.pytorch.log_model(model, 'model')
    
    # Log additional artifacts (e.g., plots, images)
    mlflow.log_artifact('results.png')
