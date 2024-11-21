import pandas as pd

def calculate_quarterly_inflation(data):
    """
    Calculate the quarterly inflation rates from the CPI data.
    :param data: DataFrame containing CPI values indexed by date.
    :return: A DataFrame with quarterly inflation rates.
    """
    data = data.resample('Q').mean()  # Resample to quarterly averages
    data['Inflation_Rate'] = data['CPI'].pct_change() * 100  # Quarterly percentage change
    return data[-5:-1]  # Return the last 4 quarters
