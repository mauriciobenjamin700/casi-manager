
from app.backend.services.data_loader import DataLoaderService


data_loader = DataLoaderService("data/Vendas.xlsx")

df = data_loader.load_excel_with_values("data/Vendas.xlsx", "Compras")

print(df.head())
print(df.columns)