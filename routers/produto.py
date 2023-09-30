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

router = APIRouter()

@router.post("/produto", tags=["Produto"])
def create_new_product(product: Produto2 = Body(...), username: str = Depends(check_entity_credencials)) -> None:
    queryProductTest = queryProduto(
        get_new_uiid(2),
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
        product.dt_alteracao,
        product.estado,
        product.desconto_comercial,
        product.foto_perfil
    )
    
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryProductTest.insert_new_product_in_database(),
                2
    )
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    
    if dbQueryResults == "Data inserted sucessfully":
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


@router.put("/produto/{id}", tags=["Produto"])
def update_product_with_id(id: str, product: Produto2 = Body(...), username: str = Depends(check_entity_credencials)):
    queryProductTest = queryProduto(
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
                '127.0.0.1',
                'faturacao',
                'root',
                '',
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
                '127.0.0.1',
                'faturacao',
                'root',
                '',
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
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Operação não completa devido a um erro",
                headers={"WWW-Authenticate": "Basic"},
            )