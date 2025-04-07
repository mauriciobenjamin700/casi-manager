from openpyxl import load_workbook
from os.path import exists
from pandas import (
    DataFrame,
    read_excel
)

from app.backend.core.settings import settings

class DataLoaderService:
    """
    A service to load and preprocess data from an Excel file. This class is designed to handle the loading of data from a specified Excel file, and provides methods to access specific sheets and preprocess the data.
    
    Args:
        data_source (str): The path to the Excel file. Defaults to "Vendas.xlsx".
    
    Methods:
        load_data(): Loads the data from the specified Excel file.
        get_sheet(sheet_name: str): Returns a DataFrame of a specific sheet from the Excel file.
        preprocess_data(raw_data): Preprocesses the loaded data.
    """
    def __init__(self, data_source: str = "Vendas.xlsx"):
        self.data_source = data_source
        self.sheets = None  # Armazena todas as abas do Excel como um dicionário de DataFrames
        self.load_data()

    def load_data(self):
        """
        Carrega o arquivo Excel inteiro em memória como um dicionário de DataFrames.
        """
        if not exists(self.data_source):
            raise FileNotFoundError(f"The data source {self.data_source} does not exist.")
        
        # Carrega todas as abas do Excel em um dicionário de DataFrames
        self.sheets = read_excel(self.data_source, sheet_name=None, engine='openpyxl')

    def get_sheet(self, sheet_name: str) -> DataFrame:
        """
        Retorna o DataFrame de uma aba específica do Excel.
        """
        if self.sheets is None:
            raise ValueError("Nenhum dado foi carregado. Certifique-se de que o arquivo foi carregado corretamente.")
        
        if sheet_name not in self.sheets:
            raise ValueError(f"A aba '{sheet_name}' não existe no arquivo Excel.")
        
        return self.sheets[sheet_name]
    
    def get_purchases(self) -> DataFrame:
        
        return self.get_sheet(settings.PURCHASES_SHEET_NAME)

    def preprocess_data(self, raw_data):
        # Logic to preprocess the loaded data
        pass
    
    def load_excel_with_values(self, file_path: str, sheet_name: str) -> DataFrame:
        """
        Carrega uma aba específica de um arquivo Excel, garantindo que os valores calculados das fórmulas sejam lidos.
        """
        wb = load_workbook(file_path, data_only=True)  # data_only=True garante que os valores calculados sejam lidos
        sheet = wb[sheet_name]

        # Converte a aba em um DataFrame
        data = sheet.values
        columns = next(data)  # Primeira linha como cabeçalho
        df = DataFrame(data, columns=columns)
        return df