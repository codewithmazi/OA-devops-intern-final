import mlflow

mlflow.set_experiment("devops-assessment")
with mlflow.start_run():
    mlflow.log_param("assessment", "final")
    mlflow.log_metric("stars", 5)
    print("Logged to MLflow!")
