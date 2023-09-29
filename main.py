from fastapi import FastAPI

from routers import cliente, produto, faturaVenda, autoDocumentation

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(cliente.router)
app.include_router(produto.router)
app.include_router(faturaVenda.router)
app.include_router(autoDocumentation.router)

@app.get("/test", tags=["Hello World"])
def hello_world() -> None:
    return {"Hello my first FastAPI api"} 
