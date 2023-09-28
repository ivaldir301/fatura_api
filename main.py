from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from repository.queries.queryCliente import queryCliente
from repository.queries.queryProduto import queryProduto
from models.venda.faturaVenda import FaturaVenda
from utils.generateCodigo import check_if_new_codigo_exists_and_generate_new
from utils.UUIDGenerator import get_new_uiid
from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.cliente import Cliente2
from models.produto import Produto2
import http.client
import secrets

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

security = HTTPBasic()

# Function for verifying if credentials comming throught http headers are valid 
# based on fixed data
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "user")
    correct_password = secrets.compare_digest(credentials.password, "password")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Routes to get the documentation for the endpoints, swagger and json types
@app.get("/test/{name}", tags=["Hello World"])
def hello_world(name: str = Depends(get_current_username)) -> None:
    return {"Hello my first FastAPI api, the name is {}".format(name)} 

@app.get("/docs")
async def get_documentation(username: str = Depends(get_current_username)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json")
async def openapi(username: str = Depends(get_current_username)):
    return get_openapi(title = "FastAPI", version="0.1.0", routes=app.routes)


# The other endpoints related to clients, products and faturavenda starts here

@app.post("/cliente", status_code=201, tags=["Cliente"])
def create_new_client(cliente: Cliente2 = Body(...)):
    newClientQuery = queryCliente(
        get_new_uiid(1),
        check_if_new_codigo_exists_and_generate_new(1),
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


@app.put("/cliente/{id}", status_code = 201, tags=["Cliente"])
def update_client_with_id(id: str, client: Cliente2 = Body(...)):
    queryClientTest = queryCliente(
        id,
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


@app.delete("/cliente/{id}", tags=["Cliente"])
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


@app.post("/produto", tags=["Produto"])
def create_new_product(product: Produto2 = Body(...)) -> None:
    queryProductTest = queryProduto(
        get_new_uiid(2),
        check_if_new_codigo_exists_and_generate_new(2),
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


@app.put("/produto/{id}", tags=["Produto"])
def update_product_with_id(id: str, product: Produto2 = Body(...)):
    queryProductTest = queryProduto(
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


@app.delete("/produto/{id}", tags=["Produto"])
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

@app.post("/faturavenda", tags=["Fatura Venda"])
def insertNewFaturaVenda(faturaVenda: FaturaVenda = Body(...)):
    conn = http.client.HTTPSConnection("fatura.opentec.cv")
    
    faturaProdutosArraySanitazed = ((str(faturaVenda.produtos).replace("ProdutoFaturaVenda", "", len(faturaVenda.produtos))).replace("(", "{", len(faturaVenda.produtos))).replace(")", "}", len(faturaVenda.produtos))
            
    payload = """tipo_fatura_id={}
                 serie_id={}
                 data_venda={}
                 condicoes_pagamento={}
                 cliente_id={}
                 produtos={}
                 requisicao={}
                 desconto_financeiro={}
                 nota={}""".format(
                                faturaVenda.tipoFaturaId,
                                faturaVenda.serie_id,
                                faturaVenda.data_venda,
                                faturaVenda.condicao_pagamento,
                                faturaVenda.cliente_id,
                                faturaProdutosArraySanitazed,
                                faturaVenda.requisicao,
                                faturaVenda.desconto_financeiro,
                                faturaVenda.nota
                            )
                                      
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_csrf=ac410cbb999a9149a88e8b1f8e76fa45d2b12cb8d865ba3d822d54de6d800b9ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22rSDvz6Gq7hxMWmfIX23oruyQvEuQrHnS%22%3B%7D; app-opentec-lab=j6tlei98du7fbtc7siaukhn84r'
    }
    
    conn.request("POST", "/web/index.php?r=remote-venda/create", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
