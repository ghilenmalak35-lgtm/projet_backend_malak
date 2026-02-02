from pydantic import BaseModel
class Create_client(BaseModel):
    firstname: str
    lastname:str
    email: str
    tel:str
    adresse:str