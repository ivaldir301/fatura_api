from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryProduto import queryProduto
from models.produto import Produto

productTest = Produto("017642d3-7d43-354b-4963-fe7ad83d3ec3")

queryProductTest = queryProduto(productTest.id)

def test_select_client_with_id_in_database():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryProductTest.get_product_with_id(),
                2
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    assert dbQueryResults[1] == "00271"