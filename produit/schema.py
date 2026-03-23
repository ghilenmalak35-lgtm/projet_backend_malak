from pydantic import BaseModel
class Create_produit(BaseModel):
    title:str
    description :str
    quantite_initial :int
    quantite_restant:int
    image:str
    prix_hors_tax:float
    prix_ttc:float
    tva:float