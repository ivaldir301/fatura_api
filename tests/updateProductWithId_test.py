from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryProduto import queryProduto
from models.produto import Produto


produtoTest = Produto(
    "02cc8444-f63c-3125-b4bc-5e8237e324iv",
    "00134",
    "Dobradiça HS12002 curva A8 c/Amortecedor calço 3 U",
    "P",
    "A",
    "",
    0.0000,
    160.8696,
    "6328790f-7060-1307-6853-ac3ba10f0064",
    "7d8bf0c0-33a6-1246-7c94-1c96245dfc3a",
    "0b055788-bf3b-b4fb-e28e-0a6d63158f84",
    "36B46EFB-CBEB-4E1F-97F9-C77D2C79F08C",
    "B14B2AF5-BA35-465E-A25D-D4FA8D66BCBD",
    "C6F795C4-E589-4A03-B596-3A1FD7AED1F3",
    "2022-01-04 18:23:08",
    "2022-09-15 19:18:39",
    "A",
    0.0,
    ""
)

queryProductTest = queryProduto(
    produtoTest.id,
    produtoTest.codigo,
    produtoTest.designacao,
    produtoTest.produto_servico,
    produtoTest.vendivel,
    produtoTest.compravel,
    produtoTest.preco_custo,
    produtoTest.preco_venda,
    produtoTest.pr_categoria_id,
    produtoTest.entidade_id,
    produtoTest.glb_user_id,
    produtoTest.pr_iva_id,
    produtoTest.pr_iva_compra_id,
    produtoTest.pr_unidade_id,
    produtoTest.dt_registro,
    produtoTest.dt_alteracao,
    produtoTest.estado,
    produtoTest.desconto_comercial,
    produtoTest.foto_perfil
)


def test_insert_new_product_in_database():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryProductTest.update_product_with_id(),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    assert dbQueryResults == "Data updated sucessfully"