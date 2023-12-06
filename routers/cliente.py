import sys
from authentication.autoDocumentationAuthentication import check_entity_credencials

sys.path.insert(1, "/Users/ivaldir/Desktop/coding/ApiFaturacao")

from models.cliente import Cliente2
from repository.queries.queryCliente import queryCliente
from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from utils.UUIDGenerator import get_new_uiid
from utils.generateCodigo import check_if_new_codigo_exists_and_generate_new
from utils.dateTimeFormatGenerator import generateDateTimeInFormat

from fastapi import Body, APIRouter, Depends, HTTPException, status

from os import environ as env
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.post("/cliente", status_code=201, tags=["Cliente"])
def create_new_client(cliente: Cliente2 = Body(...), username: str = Depends(check_entity_credencials)):
    newClientUUID = get_new_uiid(1)
    newClientCodigo = check_if_new_codigo_exists_and_generate_new(1)

    newClientQuery = queryCliente(cliente)
    
    # print(newClientQuery.insert_new_client_in_database(newClientUUID, newClientCodigo, generateDateTimeInFormat()))
    # print(cliente.pessoa_contacto)

    mysqlDBTest = DatabaseConnectorAndQuery(
        env['DATABASE_IP_ADRESS'],
        env['DATABASE_PORT'],
        env["DATABASE_NAME"],
        env['DATABASE_USER_NAME'],
        env['DATABASE_PASSWORD'],
        newClientQuery.insert_new_client_in_database(newClientUUID, newClientCodigo, generateDateTimeInFormat()),
        0
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        return {
            "success": True,
            "msg": "Cliente criado com sucesso",
            "data": {
                "codigo": newClientCodigo,
                "id": newClientUUID
            }
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.put("/cliente/{codigo}", status_code = 201, tags=["Cliente"])
def update_client_with_codigo(codigo: str, cliente: Cliente2 = Body(...), username: str = Depends(check_entity_credencials)):
    newClientQuery = queryCliente(cliente)

    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                newClientQuery.update_client_with_codigo(codigo, generateDateTimeInFormat()),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults ==  "Data updated sucessfully":
        return {
            "success": True,
            "msg": "Cliente atualizado com sucesso",
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


@router.delete("/cliente/{codigo}", tags=["Cliente"])
def delete_client_with_codigo(codigo: str, username: str = Depends(check_entity_credencials)):
    queryClientTest = queryCliente()
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryClientTest.delete_client_with_codigo(codigo),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data deleted sucessfully":
        return {
            "success": True,
            "msg": "Cliente eliminado com sucesso",
            "data": {}
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )
