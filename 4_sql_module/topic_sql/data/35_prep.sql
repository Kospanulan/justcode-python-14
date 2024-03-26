CREATE TABLE online_sales (
    order_id SERIAL PRIMARY KEY,
    product_id INT,
    sales_date DATE,
    revenue DECIMAL(10, 2),
	ship_address VARCHAR(100)
);

INSERT INTO online_sales (product_id, sales_date, revenue, ship_address) VALUES
     (1, '2023-01-01', 100.50, 'Розыбакиева 240'),
     (2, '2023-01-02', 75.20, 'Абая 89'),
     (3, '2023-01-03', 120.75, 'Толе Би 58');

CREATE TABLE offline_sales (
    order_id SERIAL PRIMARY KEY,
    product_id INT,
    sales_date DATE,
    revenue DECIMAL(10, 2)
);

INSERT INTO offline_sales (product_id, sales_date, revenue) VALUES
     (2, '2023-01-01', 50.25),
     (3, '2023-01-02', 90.80),
     (4, '2023-01-03', 110.00);
	
	





CREATE TABLE returns (
    return_id SERIAL PRIMARY KEY,
    product_id INT,
    return_date DATE,
    quantity INT
);

INSERT INTO returns (product_id, return_date, quantity) VALUES
      (2, '2023-01-03', 2),
      (3, '2023-01-02', 1),
      (4, '2023-01-01', 3);



CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50)
);

INSERT INTO products (product_name, category) VALUES
    ('Product A', 'Electronics'),
    ('Product B', 'Clothing'),
    ('Product C', 'Home Appliances'),
    ('Product D', 'Books');

