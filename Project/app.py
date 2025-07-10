from views.templates.base import setup_page
from views.templates.sidebar import render_sidebar
from services.database_service import DatabaseService
from views.pages import (
    tables_view,
    query_exec_view,
    data_view_view,
    data_insert_view
)

def main():
    setup_page()
    service = DatabaseService()
    
    operation = render_sidebar(service)
    
    if operation == "Consultar tabelas":
        tables_view.render(service)
    elif operation == "Executar consulta SQL":
        query_exec_view.render(service)
    elif operation == "Visualizar dados":
        data_view_view.render(service)
    elif operation == "Inserir dados":
        data_insert_view.render(service)

if __name__ == "__main__":
    main()