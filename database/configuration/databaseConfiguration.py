import mysql.connector
from mysql.connector import Error

class DatabaseConnectorAndQuery:
    def __init__(self, host_name: str, database_name: str, user: str, password:str, query:str) -> None:
        self.__host_name = host_name
        self.__user = user
        self.__password = password
        self.__database_name = database_name
        self.__query = query

    def connect_database_and_query(self) -> None:
        try:
            database_connection = mysql.connector.connect(
                host = self.__host_name,
                database = self.__database_name,
                user = self.__user,
                password = self.__password
            )

            if database_connection.is_connected():
                database_specific_info = database_connection.get_server_info()
                print("Connected to MySQL server version ", database_specific_info)
                cursor = database_connection.cursor()
                print(self.__query)
                
                cursor.execute(self.__query)
                #database_connection.commit()
                
                cursor.fetchall() 
                print("here")
                cursor.close()
                database_connection.close()
                print("Connection to database was closed!")
                record = cursor.fetchall
                
                print("You are connected to the database \n", record)
                
                if record is None:
                    return 
                else:
                    return record


        except Error as DatabaseConnectionError:
            print("There's was a problem when connectin to the database", DatabaseConnectionError)


# def test_connection():
#      mysqlDBTest = DatabaseConnectorAndQuery(
#         '127.0.0.1',
#         'faturacao',
#         'root',
#         '',
#         'SELECT * FROM cliente;'
#     )
     
# assert(test_connection())


