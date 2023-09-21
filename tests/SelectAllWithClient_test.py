from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryCliente import queryCliente

queryClient = queryCliente()

def test_database_execute_query_select_all():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClient.get_all_clients_in_database(),
                1
    )

    databaseQueryResults = mysqlDBTest.connect_to_database()
    assert databaseQueryResults[0][0] == "000189f4-f5b1-a5c0-65b4-90b1b4b0f3ef"

