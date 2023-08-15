CREATE TABLE IF NOT EXISTS {{ params["schema"] }}.{{ params["table"] }} (
    "date" DATE 
  , "name" VARCHAR(140)
  , "url" VARCHAR(280)
);