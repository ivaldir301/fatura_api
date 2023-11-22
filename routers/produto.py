import sys
from authentication.autoDocumentationAuthentication import check_entity_credencials

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
def create_new_product(product: Produto2 = Body(...), username: str = Depends(check_entity_credencials)) -> None:
    newProductUUID = get_new_uiid(2)

    queryProductTest = queryProduto(
        newProductUUID,
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
        generateDateTimeInFormat(),
        generateDateTimeInFormat(),
        product.estado,
        product.desconto_comercial,
        product.foto_perfil
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryProductTest.insert_new_product_in_database(),
                0
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
        raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail=newProductUUID,
                headers={"WWW-Authenticate": "Basic"},
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )


@router.put("/produto/{id}", tags=["Produto"])
def update_product_with_id(id: str, product: Produto2 = Body(...), username: str = Depends(check_entity_credencials)):
    queryProductTest = queryProduto(
        id,
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
        generateDateTimeInFormat(),
        product.estado,
        product.desconto_comercial,
        product.foto_perfil
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryProductTest.update_product_with_id(),
                3
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data updated sucessfully":
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


@router.delete("/produto/{id}", tags=["Produto"])
def delete_product_with_id(id: str, username: str = Depends(check_entity_credencials)):
    deleteQueryTest = queryProduto(id)

    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                deleteQueryTest.delete_product_with_id(),
                4
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    if dbQueryResults == "Data deleted sucessfully":
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação bem sucedida",
                headers={"WWW-Authenticate": "Basic"},
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )