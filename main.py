from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from authentication.autoDocumentationAuthentication import check_entity_credencials
from fastapi import Depends

from routers import cliente, produto, faturaVenda, autoDocumentation

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(cliente.router)
app.include_router(produto.router)
app.include_router(faturaVenda.router)


@app.get("/test", tags=["Hello World"])
def hello_world() -> None:
    return {"Hello my first FastAPI api"} 


@app.get("/docs")
async def get_documentation(username: str = Depends(check_entity_credencials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json")
async def openapi(username: str = Depends(check_entity_credencials)):
    return get_openapi(title = "FastAPI", version="0.1.0", routes=app.routes)

