import streamlit as st

def render_sidebar(controller):
    st.sidebar.title("Operações")
    operation = st.sidebar.selectbox(
        "Selecione:",
        ["Consultar tabelas", "Executar consulta SQL", "Visualizar dados", "Inserir dados"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Configuração do banco de dados:**
    - Host: `autorack.proxy.rlwy.net`
    - Porta: `36858`
    """)
    
    return operation