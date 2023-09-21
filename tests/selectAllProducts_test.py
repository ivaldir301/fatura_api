from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryProduto import queryProduto

queryProductTest = queryProduto()

def test_select_all_products_in_database():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryProductTest.get_all_products_in_database(),
                1
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    assert dbQueryResults[0][0] == "017642d3-7d43-354b-4963-fe7ad83d3ec3"
