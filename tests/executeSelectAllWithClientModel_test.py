from database.configuration.databaseConfiguration import DatabaseConnectorAndQuery
from models.cliente import Cliente
from models.produto import Produto
from database.queries.queryCliente import queryCliente
from database.queries.queryProduto import queryProduto
from datetime import datetime

clienteTest = Cliente(
        # '000189f4-f5b1-a5c0-65b4-90b1b4b0fd5c',
        # None,
        # '03409',
        # 'C',
        # 'Neusa Mendes Gomes',
        # None,
        # 121192024,
        # None,
        # '',
        # None,
        # None,
        # None,
        # None, 
        # datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        # None,
        # 'A',
        # None, 
        # None,
        # None,
        # '9BF4FA24-3C50-40BD-848C-4E8C22FB92A0',
        # 'A56CA66F-54DB-4953-88FE-47C8C7D653B3'
)

queryClient = queryCliente(
#     clienteTest.id,
#     clienteTest.designacao,
#     clienteTest.ind_coletivo,
#     clienteTest.nif,
#     clienteTest.email,
#     clienteTest.telefone,
#     clienteTest.pr_enquadramento_id,
#     clienteTest.pessoa_contacto,
#     clienteTest.descricao
)


def test_database_execute_query_with_models():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClient.get_all_clients_in_database()
    )

    databaseQueryResults = mysqlDBTest.connect_database_and_query()
    assert databaseQueryResults[0][0] == "000189f4-f5b1-a5c0-65b4-90b1b4b0fd5c"
    assert databaseQueryResults[0][4] == "Neusa Mendes Gomes"       

