from datetime import datetime
from pydantic import field_validator

from app.core.base import BaseSchema


class Payment(BaseSchema):
    """
    Schema for Payment Method
    
    Attributes:
        method (str): The payment method used for the sale.
        value (float): The value associated with the payment method.
    """
    method: str
    value: float


class SaleReport(BaseSchema):
    """
    Schema for Sale Report
    
    Attributes:
        start_date (datetime): Start date of the report.
        end_date (datetime): End date of the report.
        total_money (float): Total money earned in the specified date range.
        money_by_payment_method (list[Payment]): List of payment methods and their values.
    """
    start_date: datetime
    end_date: datetime
    total_money: float
    money_by_payment_method: list[Payment]