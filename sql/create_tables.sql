CREATE TABLE IF NOT EXISTS fighters (
    fighter_id TEXT PRIMARY KEY,
    fighter_name TEXT,
    nickname TEXT,
    height_cm REAL,
    weight_lbs REAL,
    reach_cm REAL,
    stance TEXT,
    date_of_birth TEXT,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    weight_class TEXT
);

CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    event_name TEXT,
    event_date TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    venue TEXT
);

CREATE TABLE IF NOT EXISTS fights (
    fight_id TEXT PRIMARY KEY,
    event_id TEXT,
    fighter_1_id TEXT,
    fighter_2_id TEXT,
    winner_id TEXT,
    weight_class TEXT,
    method TEXT,
    round INTEGER,
    time TEXT,
    referee TEXT,
    fight_date TEXT,
    result TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (fighter_1_id) REFERENCES fighters(fighter_id),
    FOREIGN KEY (fighter_2_id) REFERENCES fighters(fighter_id),
    FOREIGN KEY (winner_id) REFERENCES fighters(fighter_id)
);

CREATE TABLE IF NOT EXISTS gold_fighter_summary (
    fighter_id TEXT PRIMARY KEY,
    fighter_name TEXT,
    total_fights INTEGER,
    total_wins INTEGER,
    total_losses INTEGER,
    win_rate REAL,
    finish_wins INTEGER,
    decision_wins INTEGER,
    weight_class TEXT,
    FOREIGN KEY (fighter_id) REFERENCES fighters(fighter_id)
);

CREATE TABLE IF NOT EXISTS gold_event_summary (
    event_id TEXT PRIMARY KEY,
    event_name TEXT,
    total_fights INTEGER,
    total_finishes INTEGER,
    total_decisions INTEGER,
    finish_rate REAL,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);