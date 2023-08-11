# Model Registry
import mlflow.pytorch

# Log the trained model to the model registry
model_uri = "runs:/<run_id>/model"
registered_model_name = "my_model"

# Register the model in the model registry
model_version = mlflow.register_model(model_uri, registered_model_name)

# Transition the model version to production
mlflow.models.update_model_version_stage(
    name=registered_model_name,
    version=model_version.version,
    stage="Production"
)

# Serving Infrastructure
import mlflow.sagemaker

# Deploy the registered model to AWS SageMaker
deployment_name = "my_deployment"
mlflow.sagemaker.deploy(
    model_uri=f"models:/{registered_model_name}/{model_version.version}",
    deployment_name=deployment_name,
    region="us-west-2",
    mode="replace",
    instance_type="ml.m4.xlarge",
    instance_count=1,
)


# Packaging Code into Reproducible Runs
# # Create a Conda environment YAML file
# mlflow run . --experiment-id=<experiment_id> --backend=conda --output conda_env.yaml

# # Create a Docker image
# mlflow run . --experiment-id=<experiment_id> --backend=docker --build
