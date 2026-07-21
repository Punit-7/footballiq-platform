# src/data_engineering/ingest_statsbomb.py
from statsbombpy import sb
import os
 
os.makedirs("data/raw/statsbomb", exist_ok=True)
competitions = sb.competitions()
competitions.to_csv("data/raw/statsbomb/competitions.csv", index=False)
 
# Pick a competition_id/season_id from the CSV above, e.g. Premier League 15/16
matches = sb.matches(competition_id=2, season_id=27)
matches.to_csv("data/raw/statsbomb/matches.csv", index=False)
 
for match_id in matches["match_id"]:
    events = sb.events(match_id=match_id)
    events.to_json(f"data/raw/statsbomb/events_{match_id}.json", orient="records")
