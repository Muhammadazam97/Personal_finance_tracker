import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_date,get_category, get_description
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"


    #Class method decorator
    @classmethod #this will have access to the class itself but it won't have access to its instance of the class
    #in OOP when you create a new instance of the class.we have some different properties on that instance.
        #in this case,method we have defined is having access to class itself.
        #means,i acn access things like,other class methods and class variable that we defined here
    # Intialize CSV file
    def intialize_csv(cls):
        #try to read in the CSV FILE
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)   #Specofy the four different columns,we want to have inside the csv file
            # **DATA FRAME**
            # Object within Pandas that allows us to access different rows/columns from a csv file
            # Export the data frame to a csv file
            df.to_csv(cls.CSV_FILE, index=False)

            # now add some entries to the file
    @classmethod
    def add_entry(cls, date, amount, category, description):
        # Using Pandas or CSV WRITER
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description

        }# Storing into the python dictionary,just to write into the correct columns when we use
        with open(cls.CSV_FILE, "a", newline="") as  csvfile:
        # A = apending to the end of the file.we're just opening it and then putting the cursor at the very end of the file.
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Enter added successfully")

            # we creating CSV WRITER --> "Take a dictionary and write it into the CSV FILE"

    @classmethod #give us all the transactions within a date range
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # Convert all the dates inside of the date column to a datetime object,to use them to filter by different transactions
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)



        # now Creating something known as MASK
        # MASK: something that can apply to the different rows inside of a dataframe to see if we should select that row or not
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]  #returns a new filtered dataframe

        if filtered_df.empty:
            print("No transaction found in the given range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income:  ${total_income:.2f}")# 2 Decimal palces
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Saving: ${(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.intialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category,description)

def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
            .resample("D")
            .sum()
            .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exciting...")
            break
        else:
            print("Invalid choice.Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()















