# sales_analysis_finance.py
# Finance-Focused Retail Sales & Profit Analysis
# Author: Shreyas Wagh
# Objective: Analyze revenue, profit, and key finance metrics for data-driven business decisions.

import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------- Load Dataset ---------------- #
file_path = "/Users/shreyaswagh/METRICS FOR SALES AND RETAILS/GlobalMart_Sales_2021_2025.csv"

if not os.path.exists(file_path):
    print(f"❌ Error: File not found at {file_path}")
    exit()

df = pd.read_csv(file_path)
print("✅ Data loaded successfully!")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# ---------------- KPI SECTION ---------------- #
print("\n📊 Finance Key Performance Indicators (KPIs):")
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
avg_profit_margin = df["Profit_Margin"].mean()
total_net_sales = df["Net_Sales"].sum()
avg_arpu = df["ARPU"].mean()
avg_clv = df["CLV"].mean()

print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Average Profit Margin: {avg_profit_margin:.2%}")
print(f"Total Net Sales: {total_net_sales:,.2f}")
print(f"Average ARPU (Revenue per User): {avg_arpu:,.2f}")
print(f"Average CLV (Customer Lifetime Value): {avg_clv:,.2f}")

# ---------------- Revenue by Region ---------------- #
print("\n🌍 Revenue by Region (Strategic Finance Insight):")
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print(region_revenue)

plt.figure(figsize=(8,5))
region_revenue.plot(kind="bar", color="skyblue", title="Total Revenue by Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png")
plt.show()

# ---------------- Top Products by Revenue ---------------- #
print("\n📦 Top 10 Products by Revenue (Profitability Focus):")
top_products = df.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(10)
print(top_products)

plt.figure(figsize=(8,5))
top_products.plot(kind="barh", color="orange", title="Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.show()

# ---------------- Average Revenue per Year ---------------- #
print("\n📈 Average Revenue by Year (Trend Analysis for Forecasting):")
avg_revenue_year = df.groupby("Year")["Revenue"].mean()
print(avg_revenue_year)

plt.figure(figsize=(8,5))
avg_revenue_year.plot(kind="line", marker="o", color="green", title="Average Revenue by Year")
plt.ylabel("Average Revenue")
plt.tight_layout()
plt.savefig("charts/avg_revenue_year.png")
plt.show()

# ---------------- Monthly Revenue Trend ---------------- #
print("\n📅 Monthly Revenue Trend (Seasonality Analysis):")
monthly_revenue = df.groupby(["Year", "Month"])["Revenue"].sum()
print(monthly_revenue.head(12))

plt.figure(figsize=(10,5))
monthly_revenue.plot(kind="line", marker="o", title="Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png")
plt.show()

# ---------------- Profit vs COGS ---------------- #
print("\n💰 Profit vs COGS by Year (Cost Efficiency Analysis):")
profit_vs_cogs = df.groupby("Year")[["Profit","COGS"]].sum()
print(profit_vs_cogs)

profit_vs_cogs.plot(kind="bar", figsize=(8,5), title="Profit vs COGS by Year")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("charts/profit_vs_cogs.png")
plt.show()

# ---------------- Save Reports ---------------- #
os.makedirs("reports", exist_ok=True)
kpi_report = {
    "Total Revenue": total_revenue,
    "Total Profit": total_profit,
    "Average Profit Margin": avg_profit_margin,
    "Total Net Sales": total_net_sales,
    "Average ARPU": avg_arpu,
    "Average CLV": avg_clv
}
pd.DataFrame([kpi_report]).to_csv("reports/KPIs_report.csv", index=False)
print("\n📂 Reports saved in 'reports/' folder.")
print("📈 Charts saved in 'charts/' folder.")

print("\n✅ Finance Analysis Completed Successfully!")
