import streamlit as st

def render(service):
    st.subheader("Tabelas disponíveis no banco de dados")
    
    try:
        tables = service.handle_tables_request()
        
        if tables:
            st.write("Lista de tabelas:")
            for table in tables:
                st.code(table)
        else:
            st.warning("Nenhuma tabela encontrada no banco de dados.")
    except Exception as e:
        st.error(f"Erro: {str(e)}")