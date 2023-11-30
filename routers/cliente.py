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

def show_client_entid(client: str):
    print(client)

@router.post("/cliente", status_code=201, tags=["Cliente"])
def create_new_client(cliente: Cliente2 = Body(...), username: str = Depends(check_entity_credencials)):
    newClientUUID = get_new_uiid(1)
    
    show_client_entid("\n" + cliente.pessoa_contacto + " here's the data" + "\n")
    
    # for dados in cliente:
    #     print(dados)

    newClientQuery = queryCliente(
        newClientUUID,
        check_if_new_codigo_exists_and_generate_new(1),
        cliente.ind_coletivo,
        cliente.designacao,
        cliente.descricao,
        cliente.nif,
        cliente.numero_cliente,
        cliente.email,
        cliente.telefone,
        cliente.geografia_id,
        cliente.endereco,
        generateDateTimeInFormat(),
        cliente.pessoa_contacto,
        cliente.entidade_id
    )
    
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                newClientQuery.insert_new_client_in_database(),
                0
    )
     
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        return {
            "success": True,
            "msg": "Cliente criado com sucesso",
            "data": {
                "codigo": cliente.codigo,
                "id": cliente.id
            }
        }
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.put("/cliente/{codigo}", status_code = 201, tags=["Cliente"])
def update_client_with_codigo(codigo: str, client: Cliente2 = Body(...), username: str = Depends(check_entity_credencials)):
    queryClientTest = queryCliente(
        codigo,
        client.ind_coletivo,
        client.designacao,
        client.descricao,
        client.nif,
        client.numero_cliente,
        client.email,
        client.telefone,
        client.geografia_id,
        client.endereco,
        generateDateTimeInFormat(),
        client.pessoa_contacto,
    )

    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryClientTest.update_client_with_codigo(codigo),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults ==  "Data updated sucessfully":
        return {
            "success": True,
            "msg": "Cliente atualizado com sucesso",
            "data": {
                "codigo": client.codigo,
                "id": client.id
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
