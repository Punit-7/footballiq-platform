# src/data_engineering/validate.py
import pandera.pandas as pa
from pandera import Column, Check
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://footballiq:footballiq@localhost:5432/footballiq")

df = pd.read_sql("SELECT * FROM matches_staging", engine)

if {"home_goals", "away_goals"}.issubset(df.columns):
    df = df.rename(columns={"home_goals": "home_score", "away_goals": "away_score"})

if not {"home_score", "away_score"}.issubset(df.columns):
    raise ValueError("Expected either home_goals/away_goals or home_score/away_score columns in matches_staging")

schema = pa.DataFrameSchema({
    "home_score": Column(int, Check.ge(0), nullable=True),
    "away_score": Column(int, Check.ge(0), nullable=True),
})

schema.validate(df)
print("All data quality checks passed.")
