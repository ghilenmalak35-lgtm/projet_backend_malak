from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import Fournisseur
from .schema import Create_fournisseur
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/fournisseurs", tags=["fournisseurs"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/creatfournisseur")
def CreateFournisseur(fournisseur_data:Create_fournisseur, db: Session = Depends(get_db)):
    fournisseur = Fournisseur(nom=fournisseur_data.nom,email=fournisseur_data.email,telephone=fournisseur_data.telephone,adresse=fournisseur_data.adresse)
    db.add(fournisseur)
    db.commit()
    db.refresh(fournisseur)
    return fournisseur
@router.get("/fournisseurList")
def get_fournisseurs(db: Session = Depends(get_db)):
    return db.query(Fournisseur).all()
@router.get("/fournisseursss/{fournisseur_id}", response_model=Create_fournisseur)
def get_fournisseur(fournisseur_id: int, db: Session = Depends(get_db)):
    fournisseurs = db.query(Fournisseur).filter(Fournisseur.id_fournisseur == fournisseur_id).first()
    if not fournisseurs:
        raise HTTPException(status_code=404, detail="fournisseurs non trouvé")
    return fournisseurs
@router.get("/fournisseur/{fournisseur_name}", response_model=Create_fournisseur)
def get_fournisseurname(fournisseur_name:str, db: Session = Depends(get_db)):
    fournisseure = db.query(Fournisseur).filter(Fournisseur.nom == fournisseur_name).first()
    if not  fournisseure:
        raise HTTPException(status_code=404, detail=" fournisseur non trouvé")
    return  fournisseure

#methode patch
@router.patch("/fournisseure/{Fournisseur_id}", response_model=Create_fournisseur)
def update_Fournisseur(Fournisseur_id: int, user_update:Create_fournisseur, db: Session = Depends(get_db)):
    fournisseures = db.query(Fournisseur).filter(Fournisseur.id_fournisseur ==Fournisseur_id).first()
    if not fournisseures:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(fournisseures, key, value)

    db.commit()
    db.refresh(fournisseures)
    return fournisseures
#delete 
@router.delete("/fournisseurree/{Fournisseur_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Fournisseur(Fournisseur_id: int, db: Session = Depends(get_db)):
    Fournisseures = db.query(Fournisseur).filter(Fournisseur.id_fournisseur == Fournisseur_id).first()
    if not  Fournisseures:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    db.delete( Fournisseures)
    db.commit()