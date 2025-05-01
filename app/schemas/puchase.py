from pydantic import field_validator

from app.core.base import BaseSchema
from app.core.utils import format


class PurchaseSchema(BaseSchema):
    """
    A schema representing a purchase record.
    
    Attributes:
        item (str): The name of the purchased item.
        quantity (int): The quantity of the item purchased.
        price (float): The price of a single unit of the item.
        total_cost (float): The total cost of the purchase.
        purchase_date (str): The date when the purchase was made.
    """
    item: str
    quantity: int
    price: float
    total_cost: float
    purchase_date: str
    
    
    @field_validator("item", mode="before")
    def validate_item(cls, value: str) -> str:
        """
        Validate and format the item name.
        
        Args:
            cls: The class itself.
            value (str): The item name to validate.
        
        Returns:
            str: The formatted item name.
        """

        return format.format_name(value)
    
    @field_validator("quantity", mode="before")
    def validate_quantity(cls, value: str) -> int:
        """
        Validate and format the quantity.
        
        Args:
            cls: The class itself.
            value (str): The quantity to validate.
        
        Returns:
            int: The formatted quantity.
        """

        return format.format_quantity(value)
    
    @field_validator("price", mode="before")
    def validate_price(cls, value: str) -> float:
        """
        Validate and format the price.
        
        Args:
            cls: The class itself.
            value (str): The price to validate.
        
        Returns:
            float: The formatted price.
        """

        return format.format_price(value)
    
    @field_validator("total_cost", mode="before")
    def validate_total_cost(cls, value: str) -> float:
        """
        Validate and format the total cost.
        
        Args:
            cls: The class itself.
            value (str): The total cost to validate.
        
        Returns:
            float: The formatted total cost.
        """

        return format.format_price(value)
    
    @field_validator("purchase_date", mode="before")
    def validate_purchase_date(cls, value: str) -> str:
        """
        Validate and format the purchase date.
        
        Args:
            cls: The class itself.
            value (str): The purchase date to validate.
        
        Returns:
            str: The formatted purchase date.
        """

        return format.format_date(value)