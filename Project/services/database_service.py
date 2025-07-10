from controllers.database_controller import DatabaseController

class DatabaseService:
    def __init__(self):
        self.controller = DatabaseController()
    
    def handle_tables_request(self):
        return self.controller.get_tables_list()
    
    def handle_table_data_request(self, table_name):
        return self.controller.get_table_data(table_name)
    
    def handle_query_execution(self, query):
        return self.controller.execute_custom_query(query)
    
    def handle_table_structure_request(self, table_name):
        return self.controller.get_table_structure(table_name)
    
    def handle_data_insertion(self, table_name, data):
        return self.controller.insert_table_data(table_name, data)