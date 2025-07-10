import streamlit as st

def render(service):
    st.subheader("Executar consulta SQL personalizada")
    query = st.text_area("Digite sua consulta SQL:", height=150)
    
    if st.button("Executar"):
        if query:
            try:
                result = service.handle_query_execution(query)
                
                if result is not None:
                    st.dataframe(result)
                    
                    csv = result.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "Download como CSV",
                        csv,
                        "resultado_consulta.csv",
                        "text/csv",
                        key='download-csv'
                    )
                else:
                    st.success("Comando executado com sucesso!")
            except Exception as e:
                st.error(f"Erro na consulta: {str(e)}")
        else:
            st.warning("Por favor, digite uma consulta SQL.")