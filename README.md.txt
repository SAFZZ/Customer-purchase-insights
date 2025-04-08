📦 Customer Purchase Insights – ETL Data Pipeline Project
This project demonstrates a mini ETL (Extract, Transform, Load) pipeline designed to simulate how raw e-commerce data is cleaned and transformed into a business-ready dataset for analytics.

📊 Objective
To build an end-to-end ETL pipeline that processes raw customer, product, and order data into a unified dataset which can be used to derive key insights such as:

Top customers by spend

Frequently purchased products

Customer-product relationships

🛠️ Tech Stack
Language: Python

Libraries: pandas, os

Data Format: CSV

Tools: Google Colab / Jupyter Notebook (for prototyping), GitHub (for versioning)

📂 Project Structure
bash
Copy
Edit
customer-purchase-insights/
├── etl/
│   ├── extract.py                # Code to load raw CSVs
│   └── transform.py              # Code to clean, merge and output the final dataset
├── data/
│   ├── processed_customers.csv   # Cleaned customer data
│   ├── processed_orders.csv      # Cleaned order data
│   ├── processed_products.csv    # Cleaned product data
│   └── final_dataset.csv         # Final merged dataset for analytics
├── README.md
└── requirements.txt
🔄 How It Works
extract.py
Loads raw data from CSV files for customers, orders, and products.

transform.py
Cleans and merges the datasets, removing duplicates and invalid entries. The output is a final dataset ready for analytics.

final_dataset.csv
Includes enriched information such as customer names, product names, and quantities for purchase behavior analysis.

🚀 Getting Started
1. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
2. Run the pipeline
bash
Copy
Edit
python etl/extract.py
python etl/transform.py
📈 Sample Insights (Optional)
You can use this dataset to generate visualizations such as:

Top 10 customers by purchase volume

Most frequently ordered products

Customer behavior trends over time

📌 Ideal For
This project is perfect for:

Data Engineering portfolios

Applying for roles involving ETL pipelines, SQL, Python, or big data platforms

Showcasing basic understanding of data cleaning, merging, and transformation

