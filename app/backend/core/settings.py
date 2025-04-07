from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    A class representing the configuration settings for the application.
    
    Attributes:
        SHEETS (list[str]): A list of sheet names used in the application.
        SHEET_PURCHASES_COLUMNS (list[str]): A list of column names for the purchases sheet.
        SHEET_SALES_COLUMNS (list[str]): A list of column names for the sales sheet.
        MAPPING_PURCHASE_COLUMNS (dict[str, str]): A mapping of purchase column names to their corresponding keys.
        MAPPING_SALES_COLUMNS (dict[str, str]): A mapping of sales column names to their corresponding keys.
    """
    SHEETS: list[str] = Field(
        default=[
            "Compras", 
            "Produtos", 
            "Caixa", 
            "purchases",
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
    )
    PURCHASES_SHEET_NAME: str = Field(
        default="Compras",
        description="Nome da aba de compras no Excel"
    )
    SHEET_PURCHASES_COLUMNS: list[str] = Field(
        default=[
            "Data",
            "Item",
            "Quantidade",
            "Preço unitário",
            "Custo total",
        ]
    )
    SHEET_SALES_COLUMNS: list[str] = Field(
        default=[
            "Data",
            "Produto",
            "Valor unitário"
            "Quantidade",
            "Total",
            "Forma de pagamento",
            "Vendedor",
            "Observação"
        ]
    )
    MAPPING_PURCHASE_COLUMNS: dict[str, str] = Field(
        default={
            "Data": "purchase_date",
            "Item": "item",
            "Quantidade": "quantity",
            "Preço unitário": "price",
            "Custo total": "total_cost",
        }
    )
    MAPPING_SALES_COLUMNS: dict[str, str] = Field(
        default={
            "Data": "sale_date",
            "Produto": "product",
            "Valor unitário": "price",
            "Quantidade": "quantity",
            "Total": "total_cost",
            "Forma de pagamento": "payment_method",
            "Vendedor": "seller",
            "Observação": "description"
        }
    )
    
    
settings = Settings()