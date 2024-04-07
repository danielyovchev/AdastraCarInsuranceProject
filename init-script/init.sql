CREATE TABLE IF NOT EXISTS customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS car (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(id),
    make VARCHAR(255),
    model VARCHAR(255),
    year INT
);

CREATE TABLE IF NOT EXISTS insurance_company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS agent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    insurance_company_id INT REFERENCES insurance_company(id)
);

CREATE TABLE IF NOT EXISTS policy (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(id),
    car_id INT REFERENCES car(id),
    agent_id INT REFERENCES agent(id),
    policy_number VARCHAR(255),
    policy_date DATE,
    price DOUBLE PRECISION
);


-- Insert sample data into 'customer' table
INSERT INTO customer (name, email) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com')
ON CONFLICT DO NOTHING;

-- Insert sample data into 'car' table
INSERT INTO car (customer_id, make, model, year) VALUES
(1, 'Toyota', 'Corolla', 2018),
(2, 'Honda', 'Civic', 2020)
ON CONFLICT DO NOTHING;

-- Insert sample data into 'insurance_company' table
INSERT INTO insurance_company (name) VALUES
('Global Insurance'),
('National Insurance')
ON CONFLICT DO NOTHING;

-- Insert sample data into 'policy' table
-- INSERT INTO policy (customer_id, car_id, insurance_company_id, policy_number, policy_date, price) VALUES
-- (1, 1, 1, 'POLICY123', '2024-01-30', 655.52),
-- (2, 2, 2, 'POLICY456', '2024-02-10', 350.0)
-- ON CONFLICT DO NOTHING;

-- Insert sample data into 'agent' table
INSERT INTO agent (name, insurance_company_id) VALUES
('Alice Johnson', 1),
('Bob Williams', 2)
ON CONFLICT DO NOTHING;

-- Insert more customers
INSERT INTO customer (name, email) VALUES
('Emily Watson', 'emily.watson@example.com'),
('Michael Brown', 'michael.brown@example.com'),
('Sophia Johnson', 'sophia.johnson@example.com'),
('James Wilson', 'james.wilson@example.com')
ON CONFLICT DO NOTHING;

-- Insert more cars (make sure customer_id matches existing customers)
INSERT INTO car (customer_id, make, model, year) VALUES
(3, 'Ford', 'Fiesta', 2019),
(3, 'Chevrolet', 'Cruze', 2021),
(4, 'Ford', 'Mustang', 2020),
(5, 'Tesla', 'Model 3', 2022),
(6, 'Toyota', 'Camry', 2021)
ON CONFLICT DO NOTHING;

-- Assuming the initial insurance companies are sufficient, we'll skip adding more here

-- Insert more policies (ensure customer_id, car_id, and insurance_company_id are correct)
INSERT INTO policy (customer_id, car_id, agent_id, policy_number, policy_date, price) VALUES
(1, 1, 1, 'POLICY123', '2024-01-30', 655.52), -- Agent 1 for Customer 1
(2, 2, 2, 'POLICY456', '2024-02-10', 350.0),  -- Agent 2 for Customer 2
(3, 3, 1, 'POLICY789', '2024-03-15', 500.00), -- Agent 1 for Customer 3
(3, 4, 2, 'POLICY101', '2024-04-01', 600.00), -- Agent 2 for Customer 3
(4, 5, 1, 'POLICY102', '2024-03-20', 700.00), -- Agent 1 for Customer 4
(5, 6, 2, 'POLICY103', '2024-04-05', 800.00), -- Agent 2 for Customer 5
(6, 7, 1, 'POLICY104', '2024-03-25', 450.00)  -- Agent 1 for Customer 6
ON CONFLICT DO NOTHING;

-- Insert more agents (ensure insurance_company_id matches existing companies)
INSERT INTO agent (name, insurance_company_id) VALUES
('Catherine Zeta', 1),
('Chris Rock', 2),
('Anna Smith', 1),
('Robert Downey', 2)
ON CONFLICT DO NOTHING;


