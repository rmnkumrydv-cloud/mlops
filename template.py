import os
from pathlib import Path
import logging
list_of_files = [
    ".github/workflows",

    "src/__init__.py",

    # Components
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",

    # Pipelines
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",

    # Utils
    "src/utils/utils.py",

    # Logger & Exception handling
    "src/logger/logging.py",
    "src/exception/exception.py",

    # Tests
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

    # Setup scripts
    "init_setup.sh",

    # Requirements
    "requirements.txt",
    "requirements_dev.txt",

    # Packaging
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",

    # Experiments
    "experiment/experiments.ipynb"
]
logging.basicConfig(level=logging.INFO)

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Create empty file if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
