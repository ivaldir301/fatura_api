from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from authentication.autoDocumentationAuthentication import check_entity_credencials
from fastapi import Depends
import uvicorn

from routers import cliente, produto, faturaVenda

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(cliente.router)
app.include_router(produto.router)
app.include_router(faturaVenda.router)

@app.get("/docs")
async def get_documentation(username: str = Depends(check_entity_credencials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json")
async def openapi(username: str = Depends(check_entity_credencials)):
    return get_openapi(title = "FastAPI", version="0.1.0", routes=app.routes)

# This line serves to run the fastapi as a normal .py program and debugg it in vscode/pycharm
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)