from database.configuration.databaseConfiguration import DatabaseConnectorAndQuery

def test_database_connection():
        query = "SELECT * FROM cliente WHERE ID = '000189f4-f5b1-a5c0-65b4-90b1b4b0fd5c';"
        mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                query
        )

        databaseQueryResults = mysqlDBTest.connect_database_and_query()
        assert databaseQueryResults[0][0] == "000189f4-f5b1-a5c0-65b4-90b1b4b0fd5c"
        assert databaseQueryResults[0][4] == "Neusa Mendes Gomes"       