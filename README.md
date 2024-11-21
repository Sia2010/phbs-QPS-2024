# phbs-QPS-2024

# Fetch US CPI Data Script

This script fetches the US Core CPI data from the Federal Reserve Economic Data (FRED) API and calculates the last 4 quarters of inflation rates. The data is resampled to quarterly averages before calculating the percentage change (inflation rate).

## Installation

1. Clone this repository.
2. Install the required Python dependencies:
   ```bash
   pip install pandas pandas_datareader
## Project Structure 
    project/
    ├── src/
    │   └── utils.py            # Utility functions (e.g.,calculating inflation rates)
    ├── scripts/
    │   └── fetch_us_cpi.py     # Main script to fetch and process CPI data
    └── data/                   # Folder where results are saved

## Usage
Run the script from the `scripts` folder to fetch data and calculate inflation rates:
```bash
python scripts/fetch_us_cpi.py
```
This script will:
- Fetch Core CPI data (CPILFESL) from FRED starting from 2000-01-01.
- Calculate quarterly inflation rates using CPI percentage changes.
- Display the last 4 quarters of inflation rates in the terminal.
- Save the results to a CSV file in the data folder:
``` bash
data/inflation_data.csv
