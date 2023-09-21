from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery

def test_database_connection():
        query = "SELECT * FROM cliente WHERE ID = '000189f4-f5b1-a5c0-65b4-90b1b4b0kld4';"
        mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                query,
                2
        )

        databaseQueryResults = mysqlDBTest.connect_to_database()
        assert databaseQueryResults[0] == "000189f4-f5b1-a5c0-65b4-90b1b4b0kld4"
        assert databaseQueryResults[5] == "Ivaldir"       