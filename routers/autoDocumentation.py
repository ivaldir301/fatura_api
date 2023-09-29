import sys

sys.path.insert(1, "/Users/ivaldir/Desktop/coding/ApiFaturacao")

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from authentication.autoDocumentationAuthentication import check_entity_credencials
from fastapi import Depends, APIRouter

router = APIRouter()

@router.get("/docs")
async def get_documentation(username: str = Depends(check_entity_credencials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@router.get("/openapi.json")
async def openapi(username: str = Depends(check_entity_credencials)):
    return get_openapi(title = "FastAPI", version="0.1.0", routes=router.routes)

