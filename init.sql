DROP DATABASE IF EXISTS quotes_db;

CREATE DATABASE quotes_db;

\c quotes_db;

CREATE TABLE IF NOT EXISTS quotes (
    quote_id    serial PRIMARY KEY,
    author      VARCHAR(100),
    quote       VARCHAR(200)
);