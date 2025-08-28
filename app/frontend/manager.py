import streamlit as st
import pandas as pd
from datetime import datetime

from app.backend.services import SaleService
from app.core.utils.format import format_sale_df_english_to_portuguese
from app.core.utils.transform import google_sheet_base_url_to_df
from app.data.sheets import (
    MAR,
    ABRIL,
    MAIO,
    JUNHO,
    JULHO,
    AGOSTO
)

def page():
    """
    This function sets up the Streamlit page for the sales management system.
    """

    st.set_page_config(page_title="Sistema de Gestão", layout="wide")

    st.title("Sistema de Gestão de Vendas do CASI")
    
    
    def load_data(option: str) -> pd.DataFrame:
        if option == "MARÇO":
            url = MAR
        elif option == "ABRIL":
            url = ABRIL
        elif option == "MAIO":
            url = MAIO
        elif option == "JUNHO":
            url = JUNHO
        elif option == "JULHO":
            url = JULHO
        elif option == "AGOSTO":
            url = AGOSTO
        else:
            url = MAR
            
        df = google_sheet_base_url_to_df(url)
        return df

    st.sidebar.header("Selecionar Base de Dados")

    OPTIONS = ["MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO"]
    selected_month = st.sidebar.radio(
        "Escolha o mês:",
        options=OPTIONS
    )
    
    service = SaleService(
        load_data(selected_month)
    )
    
    df = service.get_df()
    
    st.dataframe(format_sale_df_english_to_portuguese(df), height=450)  # Usar st.dataframe com altura fixa

    # Seletores de intervalo de datas
    st.sidebar.subheader("Filtrar por intervalo de datas")
    min_date = pd.to_datetime(df["sale_date"].min()).date()
    max_date = pd.to_datetime(df["sale_date"].max()).date()

    start_date = st.sidebar.date_input("Data Inicial", min_date, min_value=min_date, max_value=max_date)
    end_date = st.sidebar.date_input("Data Final", max_date, min_value=min_date, max_value=max_date)
    
    st.sidebar.write(f"Data Inicial Selecionada: {start_date.strftime('%d/%m/%Y')}")
    st.sidebar.write(f"Data Final Selecionada: {end_date.strftime('%d/%m/%Y')}")
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Verificar se o intervalo de datas é válido
    if start_date > end_date:
        st.sidebar.error("A data inicial não pode ser maior que a data final.")

    if st.sidebar.button("Gerar Relatório"):
        # Filtrar o DataFrame pelo intervalo de datas
        
        result = service.get_money_by_date_interval(
            start_date=start_date,
            end_date=end_date
        )

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Resumo do Relatório**")
            st.write(f"Data Inicial: {result.start_date.strftime('%d-%m-%Y')}")
            st.write(f"Data Final: {result.end_date.strftime('%d-%m-%Y')}")
            st.write(f"Total: R$ {result.total_money:,.2f}")

        with col2:
            st.write("**Métodos de Pagamento**")
            for payment in result.money_by_payment_method:
                st.write(f"{payment.method}: R$ {payment.value:,.2f}")