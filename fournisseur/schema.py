from pydantic import BaseModel
class Create_fournisseur(BaseModel):
    nom:str
    email:str
    telephone:str
    adresse:str