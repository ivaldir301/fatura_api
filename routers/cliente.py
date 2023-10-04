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

router = APIRouter()

@router.post("/cliente", status_code=201, tags=["Cliente"])
def create_new_client(cliente: Cliente2 = Body(...), username: str = Depends(check_entity_credencials)):
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
        generateDateTimeInFormat(),
        generateDateTimeInFormat(),
        cliente.estado,
        cliente.pessoa_contacto,
        cliente.is_cliente_validado,
        cliente.pr_enquadramento_id,
        cliente.glb_user_id,
        cliente.entidade_id
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                '62.171.139.24',
                'faturacao',
                'phpmyadmin',
                'Opentec20202019aaeio##',
                newClientQuery.insert_new_client_in_database(),
                0
    )
     
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        raise HTTPException(
                status_code=status.HTTP_201_CREATED,
                detail="Operação bem sucedida",
                headers={"WWW-Authenticate": "Basic"},
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.put("/cliente/{id}", status_code = 201, tags=["Cliente"])
def update_client_with_id(id: str, client: Cliente2 = Body(...), username: str = Depends(check_entity_credencials)):
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
        generateDateTimeInFormat(),
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
        raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail="Operação bem sucedida",
                headers={"WWW-Authenticate": "Basic"},
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_client_with_id(id: str, username: str = Depends(check_entity_credencials)):
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
        raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail="Operação bem sucedida",
                headers={"WWW-Authenticate": "Basic"},
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )
