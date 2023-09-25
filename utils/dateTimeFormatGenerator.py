from datetime import datetime

def generateDateTimeInFormat() -> None:
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')
