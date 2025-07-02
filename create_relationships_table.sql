-- Table: accounts (already exists)
-- handle: PK, unique username/handle

-- Table: account_relationships
CREATE TABLE IF NOT EXISTS account_relationships (
    id SERIAL PRIMARY KEY,
    account_handle VARCHAR(255) NOT NULL REFERENCES accounts(handle) ON DELETE CASCADE,
    related_handle VARCHAR(255) NOT NULL REFERENCES accounts(handle) ON DELETE CASCADE,
    relationship_type VARCHAR(16) NOT NULL CHECK (relationship_type IN ('follower', 'following')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(account_handle, related_handle, relationship_type)
);

-- Usage:
--  - To represent that A follows B:
--      account_handle = 'A', related_handle = 'B', relationship_type = 'following'
--      account_handle = 'B', related_handle = 'A', relationship_type = 'follower'
--
--  - Query followers of X:
--      SELECT account_handle FROM account_relationships WHERE related_handle = 'X' AND relationship_type = 'follower';
--  - Query who X is following:
--      SELECT related_handle FROM account_relationships WHERE account_handle = 'X' AND relationship_type = 'following';
