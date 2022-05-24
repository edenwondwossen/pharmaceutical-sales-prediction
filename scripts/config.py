from pathlib import Path

class Config:
  RANDOM_SEED = 90
  DATASET_PATH = Path("../data")
  REPO = "C:/Users/dell/OneDrive/Desktop/pharmaceutical-sales-prediction"
  DATASET_FILE_PATH = DATASET_PATH / "train.csv"
  FEATURES_PATH = DATASET_PATH / "features"
  MODELS_PATH = Path("../models")