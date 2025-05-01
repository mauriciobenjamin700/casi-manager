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
    integer_part, decimal_part= price.split(",")
    integer_part = "".join(filter(str.isdigit, integer_part))
    decimal_part = "".join(filter(str.isdigit, decimal_part))
    
    new_price = integer_part + "." + decimal_part
    
    return float(new_price)


def format_date(date: str) -> datetime:
    """
    Format a date string to a datetime object.
    
    Args:
        date (str): The date string to format.
    
    Returns:
        datetime: The formatted date string.
    """
    try:
        date = str(date).strip()
        # Substituir barras por hifens
        date = date.replace("/", "-")
        # Converter para datetime
        date = datetime.strptime(date, "%d-%m-%Y")
        return date
    except Exception as e:
        raise ValueError(f"Invalid date format: {date}. Error: {e}")


def format_quantity(quantity: str) -> int:
    """
    Format a quantity string to an integer.
    
    Args:
        quantity (str): The quantity string to format.
    
    Returns:
        int: The formatted quantity.
    """
    try:
        quantity = str(quantity)
        quantity = quantity.strip()
        quantity = float(quantity)  
        return int(quantity)
    except Exception as e:
        raise ValueError(f"Invalid quantity format: {quantity} -> {e}.")


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