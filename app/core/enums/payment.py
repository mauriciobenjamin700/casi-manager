from enum import Enum


class PaymentMethods(str, Enum):
    """
    Enum for payment methods.
    
    Attributes:
        PAPER (str): Represents physical payment.
        VIRTUAL (str): Represents digital payment.
    """
    PAPER = "FÍSICO"
    VIRTUAL = "DIGITAL"
    OTHER = "OUTRO"