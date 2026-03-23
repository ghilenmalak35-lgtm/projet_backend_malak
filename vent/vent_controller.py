from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import Vent
from .schema import Create_vent, AchatResponse
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/vents", tags=["vents"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/creatvent")
def CreateVent(vent_dat:Create_vent, db: Session = Depends(get_db)):
    vent = Vent(date_vent=vent_dat.date_vent,quantite=vent_dat.quantite,prix_total=vent_dat.prix_total)
    db.add(vent)
    db.commit()
    db.refresh(vent)
    return vent
@router.get("/ventList")
def get_vents(db: Session = Depends(get_db)):
    return db.query(Vent).all()
@router.get("/ventsss/{id}", response_model=AchatResponse)
def get_achatss(id: int, db: Session = Depends(get_db)):
    ventts = db.query(Vent).filter(Vent.id_vent == id).first()
    if not ventts:
        raise HTTPException(status_code=404, detail="vents non trouvé")
    return ventts
@router.get("/ventes/{vent_date}", response_model=Create_vent)
def get_ventdate(vent_date:str, db: Session = Depends(get_db)):
    vente = db.query(Vent).filter(Vent.date_vent == vent_date).first()
    if not  vente:
        raise HTTPException(status_code=404, detail=" votre vent est non trouvé")
    return vente

#methode patch
@router.patch("/Vente/{id}", response_model=AchatResponse)
def update_vent(id: int, user_update:Create_vent, db: Session = Depends(get_db)):
    Ventes = db.query(Vent).filter(Vent.id_vent ==id).first()
    if not Ventes:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(Ventes, key, value)

    db.commit()
    db.refresh(Ventes)
    return Ventes
#delete 
@router.delete("/venteee/{Vent_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Achat(Vent_id: int, db: Session = Depends(get_db)):
    ventees = db.query(Vent).filter(Vent.id_vent == Vent_id).first()
    if not  ventees:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    db.delete( ventees)
    db.commit()