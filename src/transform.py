import pandas as pd

def transform_data(df):
    df = df.copy()

    df.columns = (
        df.columns.str.strip().str.lower().str.replace(r"\s+", "_", regex=True)
    )

    text_columns = df.select_dtypes(
        include=["object", "str"]
    ).columns

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    numeric_columns = [
        'row_id',
        'sales',
        'quantity',
        'discount',
        'profit',
        'postal_code'
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="raise"
        )

    date_columns = [
        'order_date',
        'ship_date'
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(
            df[column],
            format="mixed",
            errors="raise"
        )

    required_columns = [
        'row_id',
        'order_id',
        'order_date',
        'ship_date',
        'sales',
        'quantity',
        'discount',
        'profit'
    ]

    missing_columns = [
        column for column in required_columns if column not in df.columns 
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    critical_columns = [
        "row_id",
        "order_id",
        "order_date",
        "ship_date",
        "sales",
        "quantity"
    ]

    if df[critical_columns].isna().any().any():
        raise ValueError("Critical columns contain missing values")

    duplicate_count = df.duplicated(subset=["row_id"]).sum()
    if duplicate_count :print(f"Duplicate count{duplicate_count}")

    return df