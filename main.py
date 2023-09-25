from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from repository.queries.queryCliente import queryCliente
from repository.queries.queryProduto import queryProduto
from models.cliente import Cliente2
from models.produto import Produto2
from models.venda.faturaVenda import FaturaVenda
import http.client
from fastapi import FastAPI
from fastapi import Body
import json

app = FastAPI()

@app.get("/{name}")
def hello_world(name: str) -> None:
    return {"Hello my first FastAPI api, the name is {}".format(name)} 


@app.post("/cliente", status_code=201)
def create_new_client(cliente: Cliente2 = Body(...)):
    newClientQuery = queryCliente(
        cliente.id,
        cliente.foto_perfil,
        cliente.codigo,
        cliente.ind_coletivo,
        cliente.designacao,
        cliente.descricao,
        cliente.nif,
        cliente.numero_cliente,
        cliente.email,
        cliente.telefone,
        cliente.geografia_id,
        cliente.coordenadas,
        cliente.endereco,
        cliente.dt_registro,
        cliente.dt_alteracao,
        cliente.estado,
        cliente.pessoa_contacto,
        cliente.is_cliente_validado,
        cliente.pr_enquadramento_id,
        cliente.glb_user_id,
        cliente.entidade_id
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                newClientQuery.insert_new_client_in_database(),
                0
    )
     
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        return "Data inserted sucessfully"
    else:
        return "There was an error"


@app.put("/cliente", status_code = 201)
def update_client_with_id(client: Cliente2 = Body(...)):
    queryClientTest = queryCliente(
        client.id,
        client.foto_perfil,
        client.codigo,
        client.ind_coletivo,
        client.designacao,
        client.descricao,
        client.nif,
        client.numero_cliente,
        client.email,
        client.telefone,
        client.geografia_id,
        client.coordenadas,
        client.endereco,
        client.dt_registro,
        client.dt_alteracao,
        client.estado,
        client.pessoa_contacto,
        client.is_cliente_validado,
        client.pr_enquadramento_id,
        client.glb_user_id,
        client.entidade_id
    )

    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClientTest.update_client_with_id(),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults ==  "Data updated sucessfully":
        return "Update done sucessfully"
    else:
        return "there was an error"


@app.delete("/cliente/{id}")
def delete_client_with_id(id: str):
    queryClientTest = queryCliente(id)
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClientTest.delete_client_with_id(),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data deleted sucessfully":
        return "data deleted sucessfully"
    else:
        return "there was an error"


@app.post("/produto")
def create_new_product(product: Produto2 = Body(...)) -> None:
    queryProductTest = queryProduto(
        product.id,
        product.codigo,
        product.designacao,
        product.produto_servico,
        product.vendivel,
        product.compravel,
        product.preco_custo,
        product.preco_venda,
        product.pr_categoria_id,
        product.entidade_id,
        product.glb_user_id,
        product.pr_iva_id,
        product.pr_iva_compra_id,
        product.pr_unidade_id,
        product.dt_registro,
        product.dt_alteracao,
        product.estado,
        product.desconto_comercial,
        product.foto_perfil
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryProductTest.insert_new_product_in_database(),
                2
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        return "Product insertion successful" 
    else:
        return "There was an error"


@app.put("/produto")
def update_product_with_id(product: Produto2 = Body(...)):
    queryProductTest = queryProduto(
        product.id,
        product.codigo,
        product.designacao,
        product.produto_servico,
        product.vendivel,
        product.compravel,
        product.preco_custo,
        product.preco_venda,
        product.pr_categoria_id,
        product.entidade_id,
        product.glb_user_id,
        product.pr_iva_id,
        product.pr_iva_compra_id,
        product.pr_unidade_id,
        product.dt_registro,
        product.dt_alteracao,
        product.estado,
        product.desconto_comercial,
        product.foto_perfil
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryProductTest.update_product_with_id(),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data updated sucessfully":
        return "update successful"
    else:
        return "there was an error"


@app.delete("/produto/{id}")
def delete_product_with_id(id: str):
    deleteQueryTest = queryProduto(id)

    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                deleteQueryTest.delete_product_with_id(),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data deleted sucessfully":
        return "delete sucessfull"
    else:
        return "there was an error"

@app.post("/faturavenda")
def insertNewFaturaVenda(faturaVenda: FaturaVenda = Body(...)):
    conn = http.client.HTTPSConnection("fatura.opentec.cv")
    
    # transform produtos array into json objects
    
    jsonObjectsProducts = []
    
    for product in faturaVenda.produtos:
        jsonObjectsProducts.append(json.dumps(product))
        
    payload = """serie_id:{}
                 data_venda:{}
                 condicoes_pagamento:{}
                 cliente_id:{}
                 produtos:{}""".format(
                                    faturaVenda.serie_id,
                                    faturaVenda.data_venda,
                                    faturaVenda.condicao_pagamento,
                                    faturaVenda.cliente_id,
                                    jsonObjectsProducts,
                                    faturaVenda.requisicao,
                                    faturaVenda.desconto_financeiro,
                                    faturaVenda.nota
                                )
                                      
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_csrf=ac410cbb999a9149a88e8b1f8e76fa45d2b12cb8d865ba3d822d54de6d800b9ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22rSDvz6Gq7hxMWmfIX23oruyQvEuQrHnS%22%3B%7D; app-opentec-lab=j6tlei98du7fbtc7siaukhn84r'
    }
    
    print(payload)
    conn.request("POST", "/web/index.php?r=remote-venda/create", payload, headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))
