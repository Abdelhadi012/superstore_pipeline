import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger(__name__)

def extract_csv(file_path: str | Path) -> pd.DataFrame:
    file_path = Path(file_path)
    logger.info(f"Starting CSV extraction: {file_path}")

    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not exist: {file_path}")
    
    if not file_path.is_file():
        raise IsADirectoryError(f"NOT a CSV file: {file_path}")
    
    if file_path.stat().st_size == 0:
        raise ValueError(f"CSV file is empty: {file_path}")

    df = pd.read_csv(file_path)

    logger.info(f"CSV extracion completed: rows = {len(df)}, columns= {len(df.columns)}")

    return df