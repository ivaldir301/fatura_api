import uuid
import sys

sys.path.insert(1, '/Users/ivaldir/Desktop/coding/ApiFaturacao')

from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

def verify_if_uiid_exists_in_database(uiid: str, uiidUseType) -> None:
    queryMaiorCodigoNaBaseDeDados = ""
    if uiidUseType == 1:
        queryMaiorCodigoNaBaseDeDados = "SELECT (ID) FROM `cliente` WHERE ID = '{}';".format(uiid)
    else:
        queryMaiorCodigoNaBaseDeDados = "SELECT (ID) FROM `produto` WHERE ID = '{}';".format(uiid)
        
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryMaiorCodigoNaBaseDeDados,
                1
    )
    
    result = mysqlDBTest.connect_to_database()
    
    return result

def get_new_uiid(uiidUseType: int) -> str:
    newUiid = str(uuid.uuid4())
    if verify_if_uiid_exists_in_database(newUiid, uiidUseType) == newUiid:
        get_new_uiid(uiidUseType)
    else:
        return newUiid
    
