CREATE TABLE IF NOT EXISTS {{ params["schema"] }}.{{ params["table"] }} (
    time          TIMESTAMP
  , latitude      FLOAT
  , longitude     FLOAT
  , temperature   FLOAT
    )