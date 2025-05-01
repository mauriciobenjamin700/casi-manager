import pandas as pd
from pandas import DataFrame

def google_sheet_base_url_to_df(url: str, use_grid: bool = True) -> DataFrame:
    """
    Convert a Google Sheets URL to a base URL for use with pandas.

    Args:
        url (str): The Google Sheets URL.

    Returns:
        str: The base URL for use with pandas.
    """
    # Remove the "/edit" part of the URL
    base_url, params = url.split("/edit")
    
    grid = params.split("#")[-1]
    
    if use_grid:
        url = f"{base_url}/export?format=csv&{grid}"
    else:
        url = f"{base_url}/export?format=csv"
    
    df = pd.read_csv(url)
    
    return df