import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="Trade_prediction_system"

list_of_files=[
    f"src/Trade_prediction_system/__init__.py",
    f"src/Trade_prediction_system/components/__init__.py",
    f"src/Trade_prediction_system/components/data_ingestion.py",
    f"src/Trade_prediction_system/components/data_transformation.py",
    f"src/Trade_prediction_system/components/model_trainer.py",
    f"src/Trade_prediction_system/components/model_monitering.py",
    f"src/Trade_prediction_system/pipelines/__init__.py",
    f"src/Trade_prediction_system/pipelines/training_pipeline.py",
    f"src/Trade_prediction_system/pipelines/prediction_pipeline.py",
    f"src/Trade_prediction_system/exception.py",
    f"src/Trade_prediction_system/logger.py",
    f"src/Trade_prediction_system/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Assuming list_of_files is already defined
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
