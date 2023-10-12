import sys

sys.path.insert(1, "/Users/ivaldir/Desktop/coding/ApiFaturacao")

from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi import Depends, HTTPException, status
from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from utils.hasher import verifyHash

from os import environ as env
from dotenv import load_dotenv

load_dotenv()

security = HTTPBasic()

def check_entity_credencials(credentials: HTTPBasicCredentials = Depends(security)):    
    correctEntityEmail = check_entity_email_in_db(credentials.username)
    correct_password = check_entity_password_in_db(credentials.password)
            
    if correctEntityEmail != None and correct_password != None:
        if verifyHash(credentials.password, correct_password):
            return credentials.username
        else: 
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Dados enviados incorrectos",
                headers={"WWW-Authenticate": "Basic"},
            )
            

def check_entity_email_in_db(entity_email: str):
    query = "SELECT (email) FROM entidade WHERE email = '{}'".format(entity_email)
    
    getEmail = DatabaseConnectorAndQuery(
        env['DATABASE_IP_ADRESS'],
        env['DATABASE_PORT'],
        env["DATABASE_NAME"],
        env['DATABASE_USER_NAME'],
        env['DATABASE_PASSWORD'],
        query,
        2
    )
    
    entity_email = getEmail.connect_to_database()
    
    entity_email = (((str(entity_email).replace("'", "", 2)).replace('(', '', 2)).replace(')', '', 2)).replace(',', '', 2)
    
    if entity_email is None:
        return None
    else:
        return entity_email

def check_entity_password_in_db(email: str):
    query = "SELECT (API_ACCESS_CODE) FROM entidade WHERE email = '{}';".format(email)
    
    getPassword = DatabaseConnectorAndQuery(
        env['DATABASE_IP_ADRESS'],
        env['DATABASE_PORT'],
        env["DATABASE_NAME"],
        env['DATABASE_USER_NAME'],
        env['DATABASE_PASSWORD'],
        query,
        2
    )
    
    password = getPassword.connect_to_database()
    
    password = (((str(password).replace("'", "", 2)).replace('(', '', 2)).replace(')', '', 2)).replace(',', '', 2)
    
    if password is None:
        return None
    else:
        return password