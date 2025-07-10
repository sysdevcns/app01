import psycopg2
from psycopg2 import sql
import pandas as pd
from config.settings import Settings

class DatabaseModel:
    def __init__(self):
        self.config = Settings.DB_CONFIG
    

    def _get_connection(self):
        try:
            return psycopg2.connect(**self.config)
        except Exception as e:
            raise Exception(f"Erro de conexão: {str(e)}")
    

    def get_tables(self):
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                return [table[0] for table in cursor.fetchall()]
    

    def get_table_columns(self, table_name):
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = %s
                """, (table_name,))
                return cursor.fetchall()
    
   
    def get_table_data(self, table_name, limit=100):
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    sql.SQL("SELECT * FROM {} LIMIT {}").format(
                        sql.Identifier(table_name),
                        sql.Literal(limit)
                    )
                )
                data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                return pd.DataFrame(data, columns=columns)


    def execute_query(self, query):
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                
                if query.strip().lower().startswith("select"):
                    data = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description]
                    return pd.DataFrame(data, columns=columns)
                else:
                    conn.commit()
                    return None
    

    def insert_data(self, table_name, data):
        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                columns_sql = sql.SQL(', ').join(map(sql.Identifier, data.keys()))
                values_sql = sql.SQL(', ').join(map(sql.Placeholder, data.keys()))
                
                query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                    sql.Identifier(table_name),
                    columns_sql,
                    values_sql
                )
                
                cursor.execute(query, data)
                conn.commit()