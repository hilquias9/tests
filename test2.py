from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
#python -m uvicorn test2:app --reload

class Login(BaseModel):
    username:str
    password:str


app=FastAPI()

header_key=APIKeyHeader(name="Authorization")

def verification(token: str=Depends(header_key)):
    valid_token="realtoken"
    if token!=valid_token:
        raise HTTPException(status_code=401,detail="NO AUTHORIZED!")
    return "CONNECTED"

@app.post("/login")
def login (user:Login,auth:str=Depends(verification)):
    if user.username=="Hilquias" and user.password=="123":
        return {"msg":"CONECTADO!"}
    else:
        raise HTTPException(status_code=401,detail="Usuário ou senha incorretos!")