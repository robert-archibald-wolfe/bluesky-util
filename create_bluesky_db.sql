-- Create the bluesky_util user (with password, change as needed)
CREATE USER bluesky_util WITH PASSWORD 'your_secure_password';

-- Create the bluesky_accounts database owned by bluesky_util
CREATE DATABASE bluesky_accounts
    WITH 
    OWNER = bluesky_util
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

-- (Optional) Grant all privileges on the database to the owner
GRANT ALL PRIVILEGES ON DATABASE bluesky_accounts TO bluesky_util;
