from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryCliente import queryCliente

queryClientTest = queryCliente("000189f4-f5b1-a5c0-65b4-90b1b4b0kld4")

def test_query_select_with_id():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClientTest.get_client_with_id(), 
                2
    )
    
    databaseQueryResults = mysqlDBTest.connect_to_database()
    assert databaseQueryResults[2] == "5969"       
