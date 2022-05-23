from pathlib import Path


class Config:
    RANDOM_SEED = 42
    ASSETS_PATH = Path("./data")
    ORIGINAL_DATASET_FILE_PATH = ASSETS_PATH / "AdSmartABdata.csv"
    DATASET_PATH = ASSETS_PATH / "data"
    FEATURES_PATH = ASSETS_PATH / "features"
    MODELS_PATH = ASSETS_PATH / "models"
    METRICS_FILE_PATH = ASSETS_PATH / "metrics.json"