import os
from pandas_datareader import data as pdr
import datetime as dt
from pathlib import Path
import sys
import pandas as pd

# Add src folder to the path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from utils import calculate_quarterly_inflation  # Import the utility function

def main():
    # Define the parameters
    cpi_series = 'CPILFESL'
    start_date = dt.datetime(2000, 1, 1)  

    # Fetch data
    print("Fetching CPI data from FRED...")
    cpi_data = pdr.DataReader(cpi_series, 'fred', start_date)
    cpi_data.columns = ['CPI']  # Rename the column for easier handling

    # Calculate the last 4 quarters of inflation
    print("Calculating quarterly inflation rates...")
    inflation_data = calculate_quarterly_inflation(cpi_data)

    # Print the results
    print("\nLast 4 Quarters of US Inflation:")
    print(inflation_data[['Inflation_Rate']])
    file_path = os.path.join('data', 'inflation_data.csv')
    inflation_data.to_csv(file_path, index=True)  # 保存索引
    print(f"Inflation data saved to {file_path}")

if __name__ == "__main__":
    main()
