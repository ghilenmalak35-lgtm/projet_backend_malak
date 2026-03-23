from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AchatResponse(BaseModel):
    id_achat: int
    date_achat: datetime
    quantite: int
    prix_total: float

    class Config:
        from_attributes = True

class Create_achat(BaseModel):
    id_achat: Optional[int] = None
    date_achat:datetime
    quantite:int
    prix_total:float
    class Config:
        from_attributes = True
