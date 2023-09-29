import sys

sys.path.insert(1, "/Users/ivaldir/Desktop/coding/ApiFaturacao")

from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi import Depends, HTTPException, status
from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from utils.hasher import verifyHash

security = HTTPBasic()

def check_entity_credencials(credentials: HTTPBasicCredentials = Depends(security)):    
    correctEntityId = check_entity_id_in_db(credentials.username)
    correct_password = check_entity_password_in_db(correctEntityId)
            
    if correctEntityId != None and correct_password != None:
        if verifyHash(credentials.password, correct_password):
            return credentials.username
        else: 
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="ID da entidade ou password enviada  está incorrecta",
                headers={"WWW-Authenticate": "Basic"},
            )
            

def check_entity_id_in_db(entity_id: str):
    query = "SELECT (ID) FROM entidade WHERE ID = '{}';".format(entity_id)
    
    getId = DatabaseConnectorAndQuery(
        '127.0.0.1',
        'faturacao',
        'root',
        '',
        query,
        2
    )
    
    entity_id = getId.connect_to_database()
    
    entity_id = (((str(entity_id).replace("'", "", 2)).replace('(', '', 2)).replace(')', '', 2)).replace(',', '', 2)
    
    if entity_id is None:
        return None
    else:
        return entity_id

def check_entity_password_in_db(id: str):
    query = "SELECT (API_ACCESS_CODE) FROM entidade WHERE ID = '{}';".format(id)
    
    getPassword = DatabaseConnectorAndQuery(
        '127.0.0.1',
        'faturacao',
        'root',
        '',
        query,
        2
    )
    
    password = getPassword.connect_to_database()
    
    password = (((str(password).replace("'", "", 2)).replace('(', '', 2)).replace(')', '', 2)).replace(',', '', 2)
    
    if password is None:
        return None
    else:
        return password