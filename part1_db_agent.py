#model="gemini-2.5-flash-lite",
#model="gemini-2.5-flash"

!pip install -U "langchain>=0.3.12" \
               "langchain-core>=0.3.30" \
               "langchain-community>=0.3.12" \
               "langchain-google-genai>=2.0.0" \
               "sqlalchemy" \

# Create Mock Database

DB_FILE = "customer_orders.db"

# Remove old database file if it exists
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create Customers table
cursor.execute("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Country TEXT
);
""")

# Create Orders table
cursor.execute("""
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Amount REAL,
    OrderDate TEXT
);
""")

# Insert data
customers_data = [
    (1, 'Alice Johnson', 'Canada'),
    (2, 'Bob Smith', 'USA'),
    (3, 'Charlie Brown', 'Canada'),
    (4, 'Diana Prince', 'USA')
]
orders_data = [
    (101, 1, 150.00, '2025-06-15'), (102, 1, 50.00, '2025-07-01'), # Alice
    (103, 3, 200.00, '2025-06-20'), (104, 3, 75.00, '2025-07-10'), # Charlie
    (105, 2, 300.00, '2025-07-12'), (106, 2, 100.00, '2025-07-15'), # Bob
]
cursor.executemany("INSERT INTO Customers VALUES (?, ?, ?)", customers_data)
cursor.executemany("INSERT INTO Orders VALUES (?, ?, ?, ?)", orders_data)
conn.commit()
conn.close()

print(f"Mock database '{DB_FILE}' created successfully.")



