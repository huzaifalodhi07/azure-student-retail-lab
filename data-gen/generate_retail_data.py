import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path
import json, random
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)
random.seed(42)

out = Path("retail_demo")
out.mkdir(exist_ok=True)

# customers
n_customers = 1000
customers = pd.DataFrame({
    "customer_id": range(1, n_customers + 1),
    "first_name": [fake.first_name() for _ in range(n_customers)],
    "last_name": [fake.last_name() for _ in range(n_customers)],
    "gender": np.random.choice(["Male", "Female"], n_customers),
    "city": np.random.choice(["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad"], n_customers),
    "region": np.random.choice(["North", "South", "Central"], n_customers),
    "signup_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0, 450, n_customers), unit="D"),
    "loyalty_tier": np.random.choice(["Bronze", "Silver", "Gold"], n_customers)
})
customers.to_csv(out / "customers.csv", index=False)

# products
n_products = 200
products = pd.DataFrame({
    "product_id": range(1, n_products + 1),
    "category": np.random.choice(["Electronics", "Fashion", "Home", "Grocery"], n_products),
    "subcategory": np.random.choice(["A", "B", "C", "D"], n_products),
    "product_name": [fake.word().title() + " Item" for _ in range(n_products)],
    "brand": np.random.choice(["BrandX", "BrandY", "BrandZ"], n_products),
    "unit_price": np.round(np.random.uniform(5, 500, n_products), 2),
    "launch_date": pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 700, n_products), unit="D"),
    "is_active": np.random.choice([True, False], n_products, p=[0.9, 0.1])
})
products.to_csv(out / "products.csv", index=False)

# orders
n_orders = 5000
orders = pd.DataFrame({
    "order_id": range(1, n_orders + 1),
    "customer_id": np.random.randint(1, n_customers + 1, n_orders),
    "order_date": pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 180, n_orders), unit="D"),
    "order_status": np.random.choice(["Completed", "Cancelled", "Pending", "Returned"], n_orders, p=[0.75, 0.08, 0.12, 0.05]),
    "sales_channel": np.random.choice(["Web", "Mobile", "Store"], n_orders),
    "payment_method": np.random.choice(["Card", "Wallet", "COD"], n_orders)
})
orders.to_csv(out / "orders.csv", index=False)

# order_items
n_items = 12000
order_items = pd.DataFrame({
    "order_item_id": range(1, n_items + 1),
    "order_id": np.random.randint(1, n_orders + 1, n_items),
    "product_id": np.random.randint(1, n_products + 1, n_items),
    "quantity": np.random.randint(1, 5, n_items),
    "unit_price": np.round(np.random.uniform(5, 500, n_items), 2),
    "discount_pct": np.round(np.random.choice([0, 0.05, 0.10, 0.15], n_items), 2)
})
order_items.to_csv(out / "order_items.csv", index=False)

# payments
payments = pd.DataFrame({
    "payment_id": range(1, n_orders + 1),
    "order_id": range(1, n_orders + 1),
    "payment_date": orders["order_date"],
    "amount": np.round(np.random.uniform(10, 1000, n_orders), 2),
    "payment_status": np.random.choice(["Paid", "Failed", "Refunded"], n_orders, p=[0.88, 0.07, 0.05])
})
payments.to_csv(out / "payments.csv", index=False)

# returns
n_returns = 400
returns = pd.DataFrame({
    "return_id": range(1, n_returns + 1),
    "order_id": np.random.randint(1, n_orders + 1, n_returns),
    "product_id": np.random.randint(1, n_products + 1, n_returns),
    "return_date": pd.to_datetime("2025-02-01") + pd.to_timedelta(np.random.randint(0, 120, n_returns), unit="D"),
    "return_reason": np.random.choice(["Damaged", "Wrong Item", "Not Needed"], n_returns),
    "refund_amount": np.round(np.random.uniform(5, 400, n_returns), 2)
})
returns.to_csv(out / "returns.csv", index=False)

# web_events json
events = []
for i in range(1, 3001):
    events.append({
        "event_id": i,
        "event_time": (datetime(2025, 1, 1) + timedelta(minutes=random.randint(0, 150000))).isoformat(),
        "customer_id": random.randint(1, n_customers),
        "session_id": fake.uuid4(),
        "event_type": random.choice(["view", "click", "add_to_cart", "checkout"]),
        "product_id": random.randint(1, n_products),
        "page_url": f"/product/{random.randint(1, n_products)}",
        "referrer": random.choice(["google", "facebook", "direct"]),
        "device_type": random.choice(["mobile", "desktop", "tablet"])
    })

with open(out / "web_events.json", "w") as f:
    for e in events:
        f.write(json.dumps(e) + "\n")

control = pd.DataFrame([
    ["customers", "raw/customers", "csv", "curated/customers", "Y"],
    ["products", "raw/products", "csv", "curated/products", "Y"],
    ["orders", "raw/orders", "csv", "curated/orders", "Y"],
    ["order_items", "raw/order_items", "csv", "curated/order_items", "Y"],
    ["payments", "raw/payments", "csv", "curated/payments", "Y"],
    ["returns", "raw/returns", "csv", "curated/returns", "Y"],
    ["web_events", "raw/web_events", "json", "curated/web_events", "Y"]
], columns=["source_entity", "source_folder", "source_format", "sink_folder", "load_enabled"])
control.to_csv(out / "ingestion_control.csv", index=False)

print("Files created in ./retail_demo")
