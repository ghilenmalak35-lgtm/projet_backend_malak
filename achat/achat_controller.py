from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import Achat
from .schema import Create_achat, AchatResponse
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/achats", tags=["achats"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/creatachat")
def CreateAchat(achat_data:Create_achat, db: Session = Depends(get_db)):
    achat = Achat(date_achat=achat_data.date_achat,quantite=achat_data.quantite,prix_total=achat_data.prix_total)
    db.add(achat)
    db.commit()
    db.refresh(achat)
    return achat
@router.get("/achatList")
def get_achats(db: Session = Depends(get_db)):
    return db.query(Achat).all()
@router.get("/achatsss/{id}", response_model=AchatResponse)
def get_achatss(id: int, db: Session = Depends(get_db)):
    achatts = db.query(Achat).filter(Achat.id_achat == id).first()
    if not achatts:
        raise HTTPException(status_code=404, detail="fournisseurs non trouvé")
    return achatts
@router.get("/achates/{achat_date}", response_model=Create_achat)
def get_achatdate(achat_date:str, db: Session = Depends(get_db)):
    achate = db.query(Achat).filter(Achat.date_achat == achat_date).first()
    if not  achate:
        raise HTTPException(status_code=404, detail=" votre achat est non trouvé")
    return  achate

#methode patch
@router.patch("/Achate/{id}", response_model=AchatResponse)
def update_Achat(id: int, user_update:Create_achat, db: Session = Depends(get_db)):
    Achates = db.query(Achat).filter(Achat.id_achat ==id).first()
    if not Achates:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(Achates, key, value)

    db.commit()
    db.refresh(Achates)
    return Achates
#delete 
@router.delete("/achateee/{Achat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Achat(Achat_id: int, db: Session = Depends(get_db)):
    achatees = db.query(Achat).filter(Achat.id_achat == Achat_id).first()
    if not  achatees:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    db.delete( achatees)
    db.commit()