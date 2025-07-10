import streamlit as st
import pandas as pd

def render(service):
    st.subheader("Inserir dados em uma tabela")
    
    try:
        tables = service.handle_tables_request()
        selected_table = st.selectbox("Selecione uma tabela para inserção:", tables)
        
        if selected_table:
            columns = service.handle_table_structure_request(selected_table)
            
            st.write(f"Estrutura da tabela {selected_table}:")
            col_info = pd.DataFrame(columns, columns=["Coluna", "Tipo"])
            st.table(col_info)
            
            st.subheader("Formulário de inserção")
            values = {}
            for column in columns:
                col_name, col_type = column
                if col_type in ("integer", "bigint", "smallint"):
                    values[col_name] = st.number_input(col_name, step=1)
                elif col_type in ("numeric", "decimal", "real", "double precision"):
                    values[col_name] = st.number_input(col_name, step=0.01)
                elif col_type == "boolean":
                    values[col_name] = st.checkbox(col_name)
                else:
                    values[col_name] = st.text_input(col_name)
            
            if st.button("Inserir dados"):
                try:
                    service.handle_data_insertion(selected_table, values)
                    st.success("Dados inseridos com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao inserir dados: {str(e)}")
    except Exception as e:
        st.error(f"Erro: {str(e)}")