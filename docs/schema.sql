-- docs/schema.sql
CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    team_id INT REFERENCES teams(team_id)
);
CREATE TABLE matches (
    match_id SERIAL PRIMARY KEY,
    match_date DATE NOT NULL,
    home_team_id INT REFERENCES teams(team_id),
    away_team_id INT REFERENCES teams(team_id),
    home_goals INT,
    away_goals INT,
    competition VARCHAR(100)
);
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches(match_id),
    player_id INT REFERENCES players(player_id),
    minute INT,
    event_type VARCHAR(50),
    xg FLOAT
);
CREATE TABLE player_match_stats (
    id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches(match_id),
    player_id INT REFERENCES players(player_id),
    minutes_played INT,
    goals INT,
    assists INT,
    pass_accuracy FLOAT
);
