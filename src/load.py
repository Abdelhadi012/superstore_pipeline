import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, text
from sqlalchemy.exc import SQLAlchemyError

def engine_create():
    load_dotenv()
    db_url = URL.create(
        drivername='postgresql+psycopg2',
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME")
    )

    engine = create_engine(
        db_url,
        echo=False
    )
    # engine = create_engine("sqlite:///mydatabse.db", echo=True)
    return engine

def test_connection(engine):
    with engine.connect() as conn:
        result = conn.execute(text("select version()"))
        print(result.scalar())

# engine = engine()
# test_connection(engine)

def load_db(df, engine):
    if df.empty:
        print("No data to load")
        return 0
    try:
        with engine.begin() as conn:
            df.to_sql(
                name="superstore",
                con=conn,
                schema="public",
                if_exists="append",
                index=False,
                method="multi",
                chunksize=1000
            )

        print(f"Loaded {len(df)} successfully.")
        return len(df)
    except SQLAlchemyError:
        print("Loading failed.")

    