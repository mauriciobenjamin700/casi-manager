from pydantic import field_validator

from app.backend.core.base import BaseSchema
from app.backend.utils import format


class SaleSchema(BaseSchema):
    """
    A schema representing a purchase record.
    
    Attributes:
        item (str): The name of the purchased item.
        quantity (int): The quantity of the item purchased.
        price (float): The price of a single unit of the item.
        total_cost (float): The total cost of the purchase.
        purchase_date (str): The date when the purchase was made.
    """
    product: str
    quantity: int
    price: float
    total_cost: float
    payment_method: str
    seller: str
    sale_date: str
    description: str
    
    
    @field_validator("product", mode="before")
    def validate_product(cls, value: str) -> str:
        """
        Validate and format the product name.
        
        Args:
            cls: The class itself.
            value (str): The product name to validate.
        
        Returns:
            str: The formatted product name.
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
    
    @field_validator("payment_method", mode="before")
    def validate_payment_method(cls, value: str) -> str:
        """
        Validate and format the payment method.
        
        Args:
            cls: The class itself.
            value (str): The payment method to validate.
        
        Returns:
            str: The formatted payment method.
        """

        return format.format_name(value)
    
    @field_validator("seller", mode="before")
    def validate_seller(cls, value: str) -> str:
        """
        Validate and format the seller name.
        
        Args:
            cls: The class itself.
            value (str): The seller name to validate.
        
        Returns:
            str: The formatted seller name.
        """

        return format.format_name(value)
    
    @field_validator("sale_date", mode="before")
    def validate_sale_date(cls, value: str) -> str:
        """
        Validate and format the sale date.
        
        Args:
            cls: The class itself.
            value (str): The sale date to validate.
        
        Returns:
            str: The formatted sale date.
        """

        return format.format_date(value)
    
    
    @field_validator("description", mode="before")
    def validate_description(cls, value: str) -> str:
        """
        Validate and format the description.
        
        Args:
            cls: The class itself.
            value (str): The description to validate.
        
        Returns:
            str: The formatted description.
        """

        return format.format_description(value)