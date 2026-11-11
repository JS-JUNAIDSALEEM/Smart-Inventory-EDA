
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Data validation function
def validate_data(df, opening_stock, reorder_level):

    validation_results = {
        "Unique Transaction IDs": df["Transaction_ID"].is_unique,
        "No Negative Quantities": (df["Quantity"] >= 0).all(),
        "No Missing Values": df.isnull().sum().sum() == 0,
        "Valid Movement Types": df["Movement_Type"].isin(["Stock In", "Stock Out"]).all(),
        "Valid Dates": df["Date"].notnull().all(),
        "Valid Products": df["Product"].isin(opening_stock.keys()).all(),
        "Opening Stock Available": df["Product"].isin(opening_stock.keys()).all(),
        "Reorder Levels Available": df["Product"].isin(reorder_level.keys()).all()
    }

    return validation_results


def main():

# Create output folder

    os.makedirs("output/csv_reports", exist_ok=True)
    os.makedirs("output/visualizations", exist_ok=True)

# Inventory transactions data
    data = [
        {"Transaction_ID": 1,   "Date": "2026-01-01",  "Product": "Mouse",       "Movement_Type": "Stock Out",   "Quantity": 5},
        {"Transaction_ID": 2,   "Date": "2026-01-01",  "Product": "Keyboard",    "Movement_Type": "Stock Out",   "Quantity": 3},
        {"Transaction_ID": 3,   "Date": "2026-01-02",  "Product": "Monitor",     "Movement_Type": "Stock Out",   "Quantity": 2},
        {"Transaction_ID": 4,   "Date": "2026-01-02",  "Product": "USB Cable",   "Movement_Type": "Stock In",    "Quantity": 20},
        {"Transaction_ID": 5,   "Date": "2026-01-03",  "Product": "Headphones",  "Movement_Type": "Stock Out",   "Quantity": 4},
        {"Transaction_ID": 6,   "Date": "2026-01-03",  "Product": "Mouse",       "Movement_Type": "Stock Out",   "Quantity": 7},
        {"Transaction_ID": 7,   "Date": "2026-01-04",  "Product": "Keyboard",    "Movement_Type": "Stock In",    "Quantity": 10},
        {"Transaction_ID": 8,   "Date": "2026-01-04",  "Product": "Monitor",     "Movement_Type": "Stock Out",   "Quantity": 3},
        {"Transaction_ID": 9,   "Date": "2026-01-05",  "Product": "USB Cable",   "Movement_Type": "Stock Out",   "Quantity": 6},
        {"Transaction_ID": 10,  "Date": "2026-01-05",  "Product": "Headphones",  "Movement_Type": "Stock In",    "Quantity": 15},
        {"Transaction_ID": 11,  "Date": "2026-01-06",  "Product": "Mouse",       "Movement_Type": "Stock In",    "Quantity": 12},
        {"Transaction_ID": 12,  "Date": "2026-01-06",  "Product": "Keyboard",    "Movement_Type": "Stock Out",   "Quantity": 4},
        {"Transaction_ID": 13,  "Date": "2026-01-07",  "Product": "Monitor",     "Movement_Type": "Stock In",    "Quantity": 8},
        {"Transaction_ID": 14,  "Date": "2026-01-07",  "Product": "USB Cable",   "Movement_Type": "Stock Out",   "Quantity": 5},
        {"Transaction_ID": 15,  "Date": "2026-01-08",  "Product": "Headphones",  "Movement_Type": "Stock Out",   "Quantity": 6},
        {"Transaction_ID": 16,  "Date": "2026-01-08",  "Product": "Mouse",       "Movement_Type": "Stock Out",   "Quantity": 10},
        {"Transaction_ID": 17,  "Date": "2026-01-09",  "Product": "Keyboard",    "Movement_Type": "Stock Out",   "Quantity": 8},
        {"Transaction_ID": 18,  "Date": "2026-01-09",  "Product": "Monitor",     "Movement_Type": "Stock Out",   "Quantity": 2},
        {"Transaction_ID": 19,  "Date": "2026-01-10",  "Product": "USB Cable",   "Movement_Type": "Stock In",    "Quantity": 25},
        {"Transaction_ID": 20,  "Date": "2026-01-10",  "Product": "Headphones",  "Movement_Type": "Stock Out",   "Quantity": 5},
        {"Transaction_ID": 21,  "Date": "2026-01-11",  "Product": "Mouse",       "Movement_Type": "Stock Out",   "Quantity": 12},
        {"Transaction_ID": 22,  "Date": "2026-01-11",  "Product": "Keyboard",    "Movement_Type": "Stock Out",   "Quantity": 6},
        {"Transaction_ID": 23,  "Date": "2026-01-12",  "Product": "Monitor",     "Movement_Type": "Stock In",    "Quantity": 10},
        {"Transaction_ID": 24,  "Date": "2026-01-12",  "Product": "USB Cable",   "Movement_Type": "Stock Out",   "Quantity": 8},
        {"Transaction_ID": 25,  "Date": "2026-01-13",  "Product": "Headphones",  "Movement_Type": "Stock Out",   "Quantity": 9},
        {"Transaction_ID": 26,  "Date": "2026-01-13",  "Product": "Mouse",       "Movement_Type": "Stock Out",   "Quantity": 8},
        {"Transaction_ID": 27,  "Date": "2026-01-14",  "Product": "Keyboard",    "Movement_Type": "Stock Out",   "Quantity": 7},
        {"Transaction_ID": 28,  "Date": "2026-01-14",  "Product": "Monitor",     "Movement_Type": "Stock Out",   "Quantity": 4},
        {"Transaction_ID": 29,  "Date": "2026-01-14",  "Product": "USB Cable",   "Movement_Type": "Stock Out",   "Quantity": 7},
        {"Transaction_ID": 30,  "Date": "2026-01-14",  "Product": "Headphones",  "Movement_Type": "Stock In",    "Quantity": 12}
    ]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Convert Date column into date format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Opening stock of each product
    opening_stock = {
        "Mouse": 100,
        "Keyboard": 80,
        "Monitor": 40,
        "USB Cable": 120,
        "Headphones": 60
    }

    # Reorder level of each product
    reorder_level = {
        "Mouse": 50,
        "Keyboard": 35,
        "Monitor": 20,
        "USB Cable": 40,
        "Headphones": 25
    }

# 1. Basic data validation

    print("\n============= DATA VALIDATION =============\n")

    validation_results = validate_data(df, opening_stock, reorder_level)

    for test, result in validation_results.items():
        print(f"{test}: {result}")

    if not all(validation_results.values()):
        print("\nData validation failed. Please check the transaction data.")
        return

    print("\nAll data validation checks passed.")

    print("\n=============== INVENTORY TRANSACTION DATA ================\n")
    print(df.to_string(index=False))

# 2. Analyze stock movement

    print("\n================== STOCK MOVEMENT ANALYSIS ==================\n")

    # Stock In increases stock and Stock Out decreases stock
    df["Stock_Change"] = np.where(
        df["Movement_Type"] == "Stock In",
        df["Quantity"],
        -df["Quantity"]
    )

    total_stock_in = df[df["Movement_Type"] == "Stock In"]["Quantity"].sum()
    total_stock_out = df[df["Movement_Type"] == "Stock Out"]["Quantity"].sum()

    print("Total Stock In:", total_stock_in)
    print("Total Stock Out:", total_stock_out)
    print("Net Stock Movement:", df["Stock_Change"].sum())

# 3. Product movement summary

    product_summary = df.groupby("Product").agg(
        Total_Stock_In=("Stock_Change", lambda x: x[x > 0].sum()),
        Total_Stock_Out=("Stock_Change", lambda x: abs(x[x < 0].sum())),
        Net_Movement=("Stock_Change", "sum"),
        Total_Transactions=("Transaction_ID", "count")
    ).reset_index()

    # Calculate current stock using opening stock
    product_summary["Opening_Stock"] = product_summary["Product"].map(opening_stock)

    product_summary["Current_Stock"] = (
        product_summary["Opening_Stock"] + product_summary["Net_Movement"]
    )

    # Add reorder level
    product_summary["Reorder_Level"] = product_summary["Product"].map(reorder_level)

    # Check which products need restocking
    product_summary["Stock_Status"] = np.where(
        product_summary["Current_Stock"] <= product_summary["Reorder_Level"],
        "Reorder Needed",
        "Stock Available"
    )

    print("\n=================================================== PRODUCT MOVEMENT SUMMARY ======================================================\n")
    print(product_summary.to_string(index=False))

# 4. Find fast-moving and slow-moving products

    print("\n========== PRODUCT DEMAND ANALYSIS ==========")

    demand_summary = product_summary[["Product", "Total_Stock_Out"]].copy()

    demand_summary = demand_summary.sort_values( by="Total_Stock_Out", ascending=False)

    print("\nFast Moving Products:")
    print(demand_summary.head(2).to_string(index=False))

    print("\nSlow Moving Products:")
    print(demand_summary.tail(2).sort_values( by="Total_Stock_Out").to_string(index=False))

# 5. Compare first week and second week demand

    print("\n================= WEEKLY DEMAND TREND ===================\n")

    first_week = df[
        (df["Date"] >= "2026-01-01") &
        (df["Date"] <= "2026-01-07") &
        (df["Movement_Type"] == "Stock Out")
    ]

    second_week = df[
        (df["Date"] >= "2026-01-08") &
        (df["Date"] <= "2026-01-14") &
        (df["Movement_Type"] == "Stock Out")
    ]

    week_one_demand = first_week.groupby("Product")["Quantity"].sum()
    week_two_demand = second_week.groupby("Product")["Quantity"].sum()

    weekly_summary = pd.DataFrame({
        "Product": list(opening_stock.keys())
    })

    weekly_summary["First_Week_Demand"] = (
        weekly_summary["Product"].map(week_one_demand).fillna(0)
    )

    weekly_summary["Second_Week_Demand"] = (
        weekly_summary["Product"].map(week_two_demand).fillna(0)
    )

    weekly_summary["Demand_Trend"] = np.select(
        [
            weekly_summary["Second_Week_Demand"] >
            weekly_summary["First_Week_Demand"],

            weekly_summary["Second_Week_Demand"] <
            weekly_summary["First_Week_Demand"]
        ],
        [
            "Increasing",
            "Decreasing"
        ],
        default="No Change"
    )

    print(weekly_summary.to_string(index=False))

# 6. Find unusual stock-out movements

    print("\n============== UNUSUAL STOCK MOVEMENTS =================\n")

    stock_out_data = df[df["Movement_Type"] == "Stock Out"].copy()

    # Calculate average stock-out quantity for each product
    stock_out_data["Average_Demand"] = (stock_out_data.groupby("Product")["Quantity"].transform("mean"))

    # Find unusually large stock-out quantities
    unusual_movements = stock_out_data[stock_out_data["Quantity"] > stock_out_data["Average_Demand"] * 1.5].copy()

    print("Unusual Stock-Out Records:")

    if unusual_movements.empty:
        print("No unusual stock movements found.")
    else:
        print(unusual_movements[["Date", "Product", "Quantity", "Average_Demand"]].to_string(index=False))

# 7. Analyze weekday-wise demand

    print("\n========== WEEKDAY DEMAND ANALYSIS ==========\n")

    df["Day"] = df["Date"].dt.day_name()

    weekday_summary = df[df["Movement_Type"] == "Stock Out"].groupby("Day")["Quantity"].sum().reset_index()
    weekday_summary = weekday_summary.sort_values(by="Quantity", ascending=False)

    print(weekday_summary.to_string(index=False))

# 8. Create reorder alerts

    print("\n========== REORDER ALERTS ==========\n")

    reorder_alerts = product_summary[
        product_summary["Stock_Status"] == "Reorder Needed"
    ]

    if reorder_alerts.empty:
        print("No products need restocking.")
    else:
        print(reorder_alerts[
            ["Product", "Current_Stock", "Reorder_Level"]
        ].to_string(index=False))

# 9. Daily stock movement summary

    daily_summary = df.groupby("Date").agg(
        Total_Stock_In=("Stock_Change", lambda x: x[x > 0].sum()),
        Total_Stock_Out=("Stock_Change", lambda x: abs(x[x < 0].sum())),
        Net_Movement=("Stock_Change", "sum")
    ).reset_index()

    print("\n================ DAILY MOVEMENT SUMMARY ================\n")
    print(daily_summary.to_string(index=False))

# 10. Create charts

    sns.set_theme(style="whitegrid")

    # Chart 1: Product demand
    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=demand_summary,
        x="Product",
        y="Total_Stock_Out"
    )

    plt.title("Product Demand Analysis")
    plt.xlabel("Product")
    plt.ylabel("Total Stock Out")
    plt.tight_layout()
    plt.savefig("output/visualizations/product_demand.png")
    plt.show()

    # Chart 2: Daily stock-out trend
    plt.figure(figsize=(10, 5))

    sns.lineplot(
        data=daily_summary,
        x="Date",
        y="Total_Stock_Out",
        marker="o"
    )

    plt.title("Daily Stock-Out Trend")
    plt.xlabel("Date")
    plt.ylabel("Stock Out Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/visualizations/daily_stock_out_trend.png")
    plt.show()

    # Chart 3: Weekday demand
    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=weekday_summary,
        x="Day",
        y="Quantity"
    )

    plt.title("Weekday-wise Product Demand")
    plt.xlabel("Day")
    plt.ylabel("Total Demand")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/visualizations/weekday_demand.png")
    plt.show()

    # 11. Export reports
    product_summary.to_csv(
        "output/csv_reports/product_movement_summary.csv",
        index=False
    )

    weekly_summary.to_csv(
        "output/csv_reports/weekly_demand_trend.csv",
        index=False
    )

    daily_summary.to_csv(
        "output/csv_reports/daily_movement_summary.csv",
        index=False
    )

    unusual_movements.to_csv(
        "output/csv_reports/unusual_stock_movements.csv",
        index=False
    )

    reorder_alerts.to_csv(
        "output/csv_reports/reorder_alerts.csv",
        index=False
    )

    weekday_summary.to_csv(
        "output/csv_reports/weekday_demand_summary.csv",
        index=False
    )

    print("\n==================== PROJECT COMPLETED ===================\n")
    print("All reports and charts are saved in the output folder.")


if __name__ == "__main__":
    main()
