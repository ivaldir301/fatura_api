from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashString(word: str) -> str:
    return pwd_context.hash(word)

def verifyHash(plainString: str, hashedString) -> bool:
    # print(type(plainString), type(hashedString))
    response = None
    try:
        response = pwd_context.verify(plainString, hashedString)
    except:
        print("Error occurred")
        
    return response