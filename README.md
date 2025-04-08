# 🛍️ Customer Purchase Insights

A complete data engineering mini-project to extract, transform, and analyze customer purchase data. This project simulates a real-world pipeline — from raw CSV ingestion to KPI generation — and presents insights using Python, SQL, and Streamlit.

---

## 🚀 Project Overview

This project demonstrates:
- Data ingestion and cleaning
- Deriving KPIs like Total Spend, Average Purchase Value, Frequency, etc.
- Loading the data into a PostgreSQL database
- Querying with SQL
- Visualizing customer trends using Streamlit

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white&style=for-the-badge)
![SQL](https://img.shields.io/badge/-SQL-4479A1?logo=sqlite&logoColor=white&style=for-the-badge)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge)
![Google Colab](https://img.shields.io/badge/-Colab-F9AB00?logo=googlecolab&logoColor=white&style=for-the-badge)

---

## 📁 Project Structure

customer-purchase-insights/ │ ├── data/ │ ├── raw_customers.csv │ └── processed_customers.csv │ ├── etl/ │ └── etl_pipeline.py │ ├── sql/ │ ├── create_table.sql │ └── kpi_queries.sql │ ├── streamlit_app/ │ └── app.py │ ├── colab_notebooks/ │ └── ETL_Pipeline_and_KPIs.ipynb │ └── README.md


---

## ⚙️ How to Run This Project

### ▶️ On Google Colab:
1. [Open this notebook](https://colab.research.google.com/) *(Insert your Colab notebook link here)*
2. Run the cells one by one.
3. Outputs will be shown at each stage of ETL + KPI generation.

### ▶️ Locally with Streamlit:
1. Clone this repo:
   
   git clone https://github.com/safzz/Customer-purchase-insights.git
   cd Customer-purchase-insights
   
2. Install dependencies:

   pip install -r requirements.txt

3. Run the dashboard:

   streamlit run streamlit_app/app.py

📊 KPIs Included
   
   Total Purchase Amount

   Average Purchase Value

   Purchase Frequency

   RFM Score

   Customer Retention Categories

🧠 What I Learned
  
  Building a real-world ETL pipeline from scratch

  Cleaning and preprocessing raw datasets

  Writing advanced SQL queries for business metrics

  Connecting Python with PostgreSQL

  Creating interactive dashboards with Streamlit

  Presenting data insights for decision-making

💡 Future Improvements
  
  Automate data refresh using Airflow

  Add customer segmentation using ML

  Deploy dashboard using Docker & cloud

🙋‍♀️ About Me

I'm an aspiring Data Engineer with a passion for transforming raw data into meaningful insights.
Currently working at a leading MNC and building my skills for impactful roles in Data Technology.







