CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scripts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE execution_steps (
    id SERIAL PRIMARY KEY,
    script_id INT REFERENCES scripts(id) ON DELETE CASCADE,
    step_number INT NOT NULL,
    state JSONB NOT NULL,               -- Stores array states in JSON
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
