# Smart Inventory EDA v1

## About the Project

Smart Inventory EDA is a Python project that I created to explore inventory transaction data and understand product stock movement patterns.

This project analyzes stock-in and stock-out transactions to find product demand trends, fast-moving products, slow-moving products, and unusual stock movements.

It also checks reorder levels and creates different reports and charts to understand inventory activities.

The dataset is manually created using Python dictionaries.

## Features

- Analyze inventory transactions
- Calculate total stock-in and stock-out
- Find net stock movement
- Analyze product movement
- Identify fast-moving and slow-moving products
- Compare weekly product demand
- Find increasing and decreasing demand trends
- Detect unusual stock-out movements
- Analyze weekday-wise demand
- Generate reorder alerts
- Analyze daily stock movement
- Perform basic data validation
- Create data visualization charts
- Export analysis reports to CSV files

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
Smart-Inventory-EDA/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── output/
    ├── product_movement_summary.csv
    ├── weekly_demand_trend.csv
    ├── daily_movement_summary.csv
    ├── unusual_stock_movements.csv
    ├── reorder_alerts.csv
    ├── weekday_demand_summary.csv
    ├── product_demand.png
    ├── daily_stock_out_trend.png
    └── weekday_demand.png
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Smart-Inventory-EDA.git
```

### 2. Open the Project Folder

```bash
cd Smart-Inventory-EDA
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

## Reports

The project generates different reports inside the output folder:

- **product_movement_summary.csv:** Shows stock-in, stock-out, net movement, and current stock of each product.
- **weekly_demand_trend.csv:** Compares product demand between the first and second week.
- **daily_movement_summary.csv:** Shows daily stock-in and stock-out information.
- **unusual_stock_movements.csv:** Contains unusually large stock-out transactions.
- **reorder_alerts.csv:** Shows products that need restocking.
- **weekday_demand_summary.csv:** Shows product demand on different weekdays.

## Charts

The project also creates three charts:

- Product Demand Analysis
- Daily Stock-Out Trend
- Weekday-wise Product Demand

## What I Learned

While making this project, I practiced:

- Exploring transaction datasets
- Analyzing stock movement patterns
- Comparing product demand
- Using Pandas groupby and transform
- Applying NumPy conditions
- Working with dates and weekdays
- Finding unusual data records
- Creating charts using Matplotlib and Seaborn
- Exporting analysis reports to CSV files

## Future Improvements

- Use a larger inventory transaction dataset.
- Analyze monthly and seasonal demand.
- Add more product movement patterns.
- Improve stock-out risk analysis.
- Create an interactive inventory analysis dashboard.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)