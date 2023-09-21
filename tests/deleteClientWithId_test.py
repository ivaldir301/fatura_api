from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryCliente import queryCliente
from models.cliente import Cliente

newClient = Cliente("000189f4-f5b1-a5c0-65b4-90b1b4b0ffd4")

queryClientTest = queryCliente(newClient.id)

def test_delete_client_from_database():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClientTest.delete_client_with_id(),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    assert dbQueryResults == "Data deleted sucessfully"
    