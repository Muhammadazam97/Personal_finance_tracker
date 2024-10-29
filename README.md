# Personal_finance_tracker

This project is a **Personal Finance Tracker** that allows users to log, track, and manage their financial transactions. It provides a simple way to view income and expenses over specific periods and visualizes the data to make financial management easier. All transaction data is stored in a CSV file for easy access and compatibility with software like Excel or Google Sheets.

## Features

- **Add New Transaction**: Log a transaction by entering the date, amount, category (Income or Expense), and description.
- **View Transactions by Date Range**: View a list of all transactions within a specified date range, categorized by income and expenses.
- **Summary and Insights**: Get a quick summary of total income, total expenses, and net profit or savings.
- **Data Visualization**: View a plot/chart of income and expenses over the selected date range, making it easier to understand financial trends.
- **Data Export**: All transactions are stored in a CSV file (`finance_data.csv`), which can be easily imported into other tools for further analysis.

## Technologies Used

This project is built with:
- **Python**: The main programming language for building this tracker.
- **Pandas**: For handling and manipulating CSV data efficiently.
- **Matplotlib**: For creating graphical representations of financial data.

## Prerequisites

To run this project, make sure you have the following Python libraries installed:
```bash
pip install pandas
pip install matplotlib
```

# How to Use

### 1. Run the Program
Start the program by running:
```bash
python main.py
```
### 2. Options Menu
You will see a menu with the following options:

- __Add a New Transaction:__ Log a new income or expense.
- __View Transactions and Summary by Date Range:__ See transactions and a summary of income and expenses within a specific date range.
- __Exit:__ Close the program.

### 3. Adding a New Transaction
- Choose option 1 from the menu.
- Enter the __date__ for the transaction.
- Enter the __amount__ of the transaction.
- Specify whether it’s an __Income__ or __Expense__.
- Add a brief __description__ (e.g., "Groceries" or "Salary").
- You will see a confirmation message: "Entry added successfully".


### 4. Viewing Transactions and Summary by Date Range
- Choose option 2 from the menu.
- Enter the start and end date to specify the date range.
- The program will display all transactions within the range, categorized by income and expenses.
- You will also see a summary showing:

  - Total income
  - Total expenses
  - Net savings or profit
- You will be prompted: "Do you want to see a plot? (y/n)". Selecting 'y' will show a chart visualizing income and expenses over time.

### 5. Exiting the Program
- Choose option 3 to exit the program.

## Data Storage
All data is stored in a CSV file named (`finance_data.csv`), which serves as the database for the project. The CSV format allows you to easily import the data into tools like __Excel__ or __Google Sheets__ if further analysis is required.

## Example CSV Structure

Here’s a sample structure for the `finance_data.csv` file:

```csv
date,amount,category,description
29-10-2024,123.32,Income,Salary
29-10-2024,345.0,Income,Side Gig
18-02-2023,1456.0,Income,Salary
15-08-2024,50.75,Expense,Groceries
```

## Future Enhancements
In future versions, we could add:
- __Category-specific breakdowns:__ Filter data based on specific categories (e.g., Rent, Food).
- __Savings Goals:__ Track progress towards personal savings or spending goals.
- __Monthly/Annual Reports:__ Automatically generate monthly or yearly summaries.

## Contributing
Feel free to submit issues or pull requests if you would like to contribute to this project. For major changes, please discuss them in an issue first.
