from pathlib import Path
from src.extract import extract_csv
from src.transform import transform_data
from src.load import load_data
import logging

PROJECT_ROOT = Path(__file__).resolve().parent
df_path = PROJECT_ROOT/"data"/"raw"/"Superstore.csv"

logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",)

logger = logging.getLogger(__name__)

def main():
    # Extract
    df = extract_csv(df_path)

    # Transform
    transformed_df = transform_data(df)

    # Load
    load_data(transformed_df)


if __name__ == "__main__":
    main()
