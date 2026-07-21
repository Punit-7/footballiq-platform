# src/data_engineering/etl.py
import pandas as pd
from sqlalchemy import create_engine
from rapidfuzz import process
 
engine = create_engine("postgresql://footballiq:footballiq@localhost:5432/footballiq")
matches_raw = pd.read_csv("data/raw/statsbomb/matches.csv")
 
canonical_teams = matches_raw["home_team"].unique().tolist()
def normalize_team(name, choices=canonical_teams):
    match, score, _ = process.extractOne(name, choices)
    return match if score > 85 else name
 
matches_raw["home_team"] = matches_raw["home_team"].apply(normalize_team)
matches_raw["away_team"] = matches_raw["away_team"].apply(normalize_team)
matches_raw = matches_raw.drop_duplicates(subset=["match_date", "home_team", "away_team"])
 
matches_raw.to_sql("matches_staging", engine, if_exists="replace", index=False)
print(f"Loaded {len(matches_raw)} rows into matches_staging")
