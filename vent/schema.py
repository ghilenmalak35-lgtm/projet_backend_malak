from pydantic import BaseModel
from datetime import datetime

class AchatResponse(BaseModel):
    id_vent: int
    date_vent: datetime
    quantite: int
    prix_total: float

    class Config:
        from_attributes = True

class Create_vent(BaseModel):
    date_vent:datetime
    quantite:int
    prix_total:float