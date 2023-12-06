import sys
from authentication.autoDocumentationAuthentication import check_entity_credencials
from utils.generateCodigo import check_if_new_codigo_exists_and_generate_new

sys.path.insert(1, "/Users/ivaldir/Desktop/coding/ApiFaturacao")

from models.produto import Produto2
from repository.queries.queryProduto import queryProduto
from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery

from utils.dateTimeFormatGenerator import generateDateTimeInFormat
from utils.generateCodigo import check_if_new_codigo_exists_and_generate_new
from utils.UUIDGenerator import get_new_uiid

from fastapi import Body, APIRouter, Depends, HTTPException, status
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.post("/produto", tags=["Produto"])
def create_new_product(produto: Produto2 = Body(...), username: str = Depends(check_entity_credencials)) -> None:
    newProductUUID = get_new_uiid(2)
    newProductCodigo = check_if_new_codigo_exists_and_generate_new(2)

    queryProductTest = queryProduto(produto)
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryProductTest.insert_new_product_in_database(newProductUUID, newProductCodigo, generateDateTimeInFormat()),
                0
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        return {
            "success": True,
            "msg": "Produto criado com sucesso",
            "data": {
                "codigo": newProductUUID,
                "id": newProductCodigo
            }
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.put("/produto/{codigo}", tags=["Produto"])
def update_product_with_codigo(codigo: str, produto: Produto2 = Body(...), username: str = Depends(check_entity_credencials)):
    queryProductTest = queryProduto(produto)
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryProductTest.update_product_with_codigo(codigo, generateDateTimeInFormat()),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data updated sucessfully":
        return {
            "success": True,
            "msg": "Produto atualizado com sucesso",
            "data": {
                "codigo": codigo,
            }
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.delete("/produto/{codigo}", tags=["Produto"])
def delete_product_with_codigo(codigo: str, username: str = Depends(check_entity_credencials)):
    deleteQueryTest = queryProduto()

    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                deleteQueryTest.delete_product_with_codigo(codigo),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data deleted sucessfully":
        return {
            "success": True,
            "msg": "Produto eliminado com sucesso",
            "data": {}
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )