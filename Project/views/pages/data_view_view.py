import streamlit as st
import pandas as pd

def render(service):
    st.subheader("Visualizar dados de uma tabela")
    
    try:
        tables = service.handle_tables_request()
        selected_table = st.selectbox("Selecione uma tabela:", tables)
        
        if selected_table and st.button("Carregar dados"):
            df = service.handle_table_data_request(selected_table)
            st.dataframe(df)
            
            st.subheader("Estatísticas básicas")
            st.write(df.describe())
    except Exception as e:
        st.error(f"Erro: {str(e)}")