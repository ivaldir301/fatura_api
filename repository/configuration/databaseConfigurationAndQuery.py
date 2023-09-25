import mysql.connector
from mysql.connector import Error

class DatabaseConnectorAndQuery:
    def __init__(self, host_name: str, database_name: str, user: str, password:str, query:str, queryType: int) -> None:
        self.__host_name = host_name
        self.__user = user
        self.__password = password
        self.__database_name = database_name
        self.__query = query
        self.__queryType = queryType

    def connect_to_database(self):
        try:
            database_connection = mysql.connector.connect(
                host = self.__host_name,
                database = self.__database_name,
                user = self.__user,
                password = self.__password,
                autocommit=True
            )
            
            if database_connection.is_connected():
                print("Connection to database established sucessfully")
                print("Connected to MySQL server version ", database_connection.get_server_info())
                            
            cursor = database_connection.cursor()
            
            result = None
            
            #print(self.__query)
            
            if self.__queryType == 0:
                cursor.execute(self.__query)
                return "Data inserted sucessfully"
            elif self.__queryType == 1:
                cursor.execute(self.__query)
                result = cursor.fetchall()
            elif self.__queryType == 2:
                cursor.execute(self.__query)
                result = cursor.fetchone()
            elif self.__queryType == 3:
                cursor.execute(self.__query)
                return "Data updated sucessfully"
            elif self.__queryType == 4:
                cursor.execute(self.__query)
                return "Data deleted sucessfully"
                       
            cursor.close()
            database_connection.close()
            
            if result != None:
                return result
            
            print("Connection to database was closed!")
            
                
        except Error as DatabaseConnectionError:
            print("There's was a problem when connectin to the database", DatabaseConnectionError)
            



