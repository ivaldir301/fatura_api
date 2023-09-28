from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from repository.queries.queryProduto import queryProduto
from models.produto import Produto

productTest = Produto("02f3db02-c614-7d36-438f-705c12ac7957")

deleteQueryTest = queryProduto(productTest.id)

def test_delete_product_in_database():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                deleteQueryTest.delete_product_with_id(),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    assert dbQueryResults == "Data deleted sucessfully"