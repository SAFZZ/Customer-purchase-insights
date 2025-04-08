import pandas as pd
import os

os.makedirs("customer_project/data", exist_ok=True)


customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "location": ["New York", "California", "Texas", "Florida"]
})
customers.to_csv("customer_project/data/processed_customers.csv", index=False)

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 2, 3, 4],
    "product_id": [1001, 1002, 1003, 1001, 1002],
    "quantity": [2, 1, 5, 2, 3],
    "order_date": pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-05", "2023-01-06"])
})
orders.to_csv("customer_project/data/processed_orders.csv", index=False)


products = pd.DataFrame({
    "product_id": [1001, 1002, 1003],
    "product_name": ["Laptop", "Smartphone", "Headphones"],
    "price": [1200.0, 800.0, 150.0]
})
products.to_csv("customer_project/data/processed_products.csv", index=False)
