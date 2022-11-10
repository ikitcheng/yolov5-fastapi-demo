# backend/config.py
from pathlib import Path

ROOT_DIR = Path(__file__).parent

PATH_TO_MODEL = ROOT_DIR / "models"
PATH_TO_DATA = ROOT_DIR / "data"

MODELS = {
    "small": "yolov5s",
    "medium": "yolov5m",
    "large": "yolov5l",
    "xlarge": "yolov5x",
}