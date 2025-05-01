from datetime import datetime
from pandas import DataFrame

from app.core import settings
from app.core.enums import PaymentMethods
from app.core.utils import format
from app.schemas.sale import SaleReport, Payment


class SaleService:
    def __init__(self, df: DataFrame) -> None:
        self.df = df
        
        # Clean column names by removing leading and trailing whitespace
        self.df.columns = self.df.columns.str.strip()
        # Rename columns based on the mapping defined in settings
        self.df.rename(
            columns=settings.MAPPING_SALES_COLUMNS,
            inplace=True,
        )
        # Filter out columns that are not in the mapping
        mapped_columns = list(settings.MAPPING_SALES_COLUMNS.values())
        self.df = self.df.loc[:, mapped_columns]  # Use .loc to avoid SettingWithCopyWarning
        self.df = self.df.dropna(how="any", axis=0)
        
        self.__clean_date()
        self.__clean_product()
        self.__clean_price()
        self.__clean_quantity()
        self.__clean_total_cost()
        self.__clean_payment_method()
        self.__clean_seller()
        self.__clean_description()
        
        
    def get_money_by_date_interval(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> SaleReport:
        """
        Returns the total money earned in a specified date range.
        
        This method calculates the total money earned in the specified date range and
        returns a SaleReport object containing the start date, end date, total money,
        and a list of payment methods with their corresponding values.
        
        Args:
            start_date (datetime): Start date of the report.
            end_date (datetime): End date of the report.
        Returns:
            SaleReport: A SaleReport object containing the report data.
        """
        
        print(self.df["sale_date"].unique())
        
        filtered_df = self.df[
            (self.df["sale_date"] >= start_date) &
            (self.df["sale_date"] < end_date)
        ]
        
        
        total_money = filtered_df["total_cost"].sum()
        
        payment_methods = (
            filtered_df.groupby("payment_method")["total_cost"]
            .sum()
            .reset_index()
            .rename(columns={"total_cost": "value"})
        )
        
        payment_methods_list = [
            Payment(method=row["payment_method"], value=float(row["value"]))
            for _, row in payment_methods.iterrows()
        ]
        
        return SaleReport(
            start_date=start_date,
            end_date=end_date,
            total_money=total_money,
            money_by_payment_method=payment_methods_list
        )
        
        
    def get_df(self) -> DataFrame:
        """
        Returns the cleaned DataFrame.
        
        This method returns the cleaned DataFrame after applying all the cleaning methods.
        
        Args:
            None
        Returns:
            DataFrame: The cleaned DataFrame.
        """
        return self.df

    def export(self, output: str = "result.csv") -> None:
        """
        Exports the cleaned DataFrame to a CSV file.
        
        This method saves the cleaned DataFrame to a CSV file with the name defined in
        settings.SALES_CSV_FILE_NAME.
        
        Args:
            None
        """
        self.df.to_csv(output, index=False)
        
    def __clean_date(self) -> None:
        """
        Cleans the date column in the DataFrame.
        
        This method standardizes the date values in the DataFrame by removing specific
        characters and converting them to datetime.
        
        Args:
            None
        """
        self.df["sale_date"] = self.df["sale_date"].map(lambda x: format.format_date(x))
        
        
    def __clean_product(self) -> None:
        """
        Cleans the product column in the DataFrame.
        
        This method standardizes the product values in the DataFrame by removing specific
        characters and converting them to uppercase.
        
        Args:
            None
        """
        self.df["product"] = self.df["product"].map(lambda x: format.format_name(x))
        
        
        
    def __clean_price(self) -> None:
        """
        Cleans the price column in the DataFrame.
        
        This method standardizes the price values in the DataFrame by removing specific
        characters and converting them to float.
        
        Args:
            None
        """
        self.df["price"] = self.df["price"].map(lambda x: format.format_price(x))
        
    def __clean_quantity(self) -> None:
        """
        Cleans the quantity column in the DataFrame.
        
        This method standardizes the quantity values in the DataFrame by removing specific
        characters and converting them to int.
        
        Args:
            None
        """
        self.df["quantity"] = self.df["quantity"].map(lambda x: format.format_quantity(x))
        
    def __clean_total_cost(self) -> None:
        """
        Cleans the total cost column in the DataFrame.
        
        This method standardizes the total cost values in the DataFrame by removing specific
        characters and converting them to float.
        
        Args:
            None
        """
        self.df["total_cost"] = self.df["total_cost"].map(lambda x: format.format_price(x))
        
        
    def __clean_payment_method(self) -> None:
        """
        Cleans the payment method column in the DataFrame.
        
        This method standardizes the payment method values in the DataFrame by replacing
        specific strings with their corresponding enum values.
        
        Args:
            None
        """
        self.df["payment_method"] = self.df["payment_method"].str.strip()
        self.df["payment_method"] = self.df["payment_method"].str.upper()
        self.df["payment_method"] = self.df["payment_method"].str.replace("DINHEIRO", PaymentMethods.PAPER.value) 
        self.df["payment_method"] = self.df["payment_method"].str.replace("FÍSICO", PaymentMethods.PAPER.value)
        self.df["payment_method"] = self.df["payment_method"].str.replace("FISICO", PaymentMethods.PAPER.value)
        self.df["payment_method"] = self.df["payment_method"].str.replace("PIX", PaymentMethods.VIRTUAL.value)
        self.df["payment_method"] = self.df["payment_method"].str.replace("???", PaymentMethods.OTHER.value)
        
        
    def __clean_seller(self) -> None:
        """
        Cleans the seller column in the DataFrame.
        
        This method standardizes the seller values in the DataFrame by removing specific
        characters and converting them to uppercase.
        
        Args:
            None
        """
        self.df["seller"] = self.df["seller"].map(lambda x: format.format_name(x))
        
        
    def __clean_description(self) -> None:
        """
        Cleans the description column in the DataFrame.
        
        This method standardizes the description values in the DataFrame by removing specific
        characters and converting them to uppercase.
        
        Args:
            None
        """
        self.df["description"] = self.df["description"].map(
            lambda x: format.format_name(x)
            if isinstance(x, str) else None
        )