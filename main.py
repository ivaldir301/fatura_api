from database.queries import queryCliente, queryProduto
from models import cliente, produto
from database import setupDatabaseAndQuery
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world() -> None:
    return {"Hello my first FastAPI api"} 

@app.put("v1/cliente")
def create_new_client() -> None:
    return "product created"

@app.get("v1/cliente")
def get_all_clients():
    return "clients"

@app.get("v1/cliente/{}")
def get_cliente_with_id(id: str):
    return "cliente com id"

@app.update("v1/cliente/{}")
def update_client_with_id(id: str):
    return "cliente foi atualizado"

@app.delete("v1/cliente")
def delete_client_with_id(id: str):
    return "cliente deletado"

@app.put("v1/produto")
def create_new_product() -> None:
    return "product created"

@app.get("v1/produto")
def get_all_products():
    return "produtos"

@app.get("v1/produto/{}")
def get_product_with_id(id: str):
    return "produto com id"

@app.update("v1/produto/{}")
def update_product_with_id(id: str):
    return "produto atualizado"

@app.delete("v1/produto/")
def delete_product_with_id(id: str):
    return "produto deletado"
