"""
A module for formatting various data types, including names, prices, dates, quantities, and descriptions.

Functions:
- format_name(name: str) -> str: Formats a name by UpperCase letter of each word.
- format_price(price: str) -> float: Formats a price string to a float.
- format_date(date: str) -> datetime: Formats a date string to a datetime object.
- format_quantity(quantity: str) -> int: Formats a quantity string to an integer.
- format_description(description: str) -> str: Formats a description string by capitalizing the first letter of each word.
"""

from datetime import datetime


def format_name(name: str) -> str:
    """
    Format a name by UpperCase of each word.
    
    Args:
        name (str): The name to format.
        
    Returns:
        str: The formatted name.
    """
    name = str(name)
    name = name.strip()
    name= name.upper()
    return name


def format_price(price: str) -> float:
    """
    Format a price string to a float.
    
    Args:
        price (str): The price string to format.
    
    Returns:
        float: The formatted price.
    """
    price = str(price)
    price.strip()
    price.replace("$", "")
    return float(price)


def format_date(date: str) -> datetime:
    """
    Format a date string to a datetime object.
    
    Args:
        date (str): The date string to format.
    
    Returns:
        datetime: The formatted date string.
    """
    date = str(date)
    date = date.strip()
    date.replace("/", "-")
    date = datetime.strptime(date, "%d-%m-%Y")
    return date


def format_quantity(quantity: str) -> int:
    """
    Format a quantity string to an integer.
    
    Args:
        quantity (str): The quantity string to format.
    
    Returns:
        int: The formatted quantity.
    """
    quantity = str(quantity)
    quantity = quantity.strip()
    return int(quantity)


def format_description(description: str) -> str:
    """
    Format a description string by capitalizing the first letter of each word.
    
    Args:
        description (str): The description to format.
        
    Returns:
        str: The formatted description.
    """
    description = str(description)
    description = description.strip()
    description = description.capitalize()
    return description