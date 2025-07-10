from models.database_model import DatabaseModel
import pandas as pd

class DatabaseController:
    def __init__(self):
        self.model = DatabaseModel()
    
    def get_tables_list(self):
        try:
            return self.model.get_tables()
        except Exception as e:
            raise Exception(f"Erro ao obter tabelas: {str(e)}")
    
    def get_table_data(self, table_name):
        try:
            return self.model.get_table_data(table_name)
        except Exception as e:
            raise Exception(f"Erro ao obter dados da tabela: {str(e)}")
    
    def execute_custom_query(self, query):
        try:
            return self.model.execute_query(query)
        except Exception as e:
            raise Exception(f"Erro na consulta SQL: {str(e)}")
    
    def get_table_structure(self, table_name):
        try:
            return self.model.get_table_columns(table_name)
        except Exception as e:
            raise Exception(f"Erro ao obter estrutura da tabela: {str(e)}")
    
    def insert_table_data(self, table_name, data):
        try:
            return self.model.insert_data(table_name, data)
        except Exception as e:
            raise Exception(f"Erro ao inserir dados: {str(e)}")