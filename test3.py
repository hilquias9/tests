from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str

app=FastAPI()

tipo=HTTPBearer()

MEU_TOKEN="TOKENSEGURO123"

def verificar_token_bearer(credentials:HTTPAuthorizationCredentials=Depends(tipo)):
    token=credentials.credentials
    teste=credentials
    print(token)
    print(teste)

@app.get("/login")
def login(usuario:dict=Depends(verificar_token_bearer)):
    return usuario