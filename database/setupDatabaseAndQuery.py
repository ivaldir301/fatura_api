from configuration.databaseConfiguration import DatabaseConnectorAndQuery

def setud_database_and_query(query: str):
    mysqlDBTest = DatabaseConnectorAndQuery(
        '127.0.0.1',
        'faturacao',
        'root',
        '',
        query  # 'SELECT * FROM cliente;'
    )

    mysqlDBTest.connect_database_and_query()