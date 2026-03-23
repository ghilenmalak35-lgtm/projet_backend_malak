from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import Produit
from .schema import Create_produit
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/produits", tags=["produits"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/createproduit")
def CreateProduit(produit_data:Create_produit, db: Session = Depends(get_db)):
    produit = Produit(title=produit_data.title,description=produit_data.description, quantite_initial=produit_data. quantite_initial,quantite_restant=produit_data.quantite_restant, image=produit_data.image,prix_hors_tax=produit_data.prix_hors_tax,prix_ttc=produit_data.prix_ttc,tva=produit_data.tva)
    db.add(produit)
    db.commit()
    db.refresh(produit)
    return produit

@router.get("/produitList")
def get_produits(db: Session = Depends(get_db)):
    return db.query(Produit).all()
@router.get("/produitss/{produit_id}", response_model=Create_produit)
def get_produit(produit_id: int, db: Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit
@router.get("/produites/{produit_title}", response_model=Create_produit)
def get_produit_title(produit_title:str, db: Session = Depends(get_db)):
    produite = db.query(Produit).filter(Produit.title == produit_title).first()
    if not produite:
        raise HTTPException(status_code=404, detail="user non trouvé")
    return produite
#methode patch
@router.patch("/produite/{Produit_id}", response_model=Create_produit)
def update_Produit(Produit_id: int, produit_update:Create_produit, db: Session = Depends(get_db)):
    produitee = db.query(Produit).filter(Produit.id == Produit_id).first()
    if not produitee:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in produit_update.dict(exclude_unset=True).items():
        setattr(produitee, key, value)

    db.commit()
    db.refresh(produitee)
    return produitee
#delete 
@router.delete("/produitees/{Produit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Produit(Produit_id: int, db: Session = Depends(get_db)):
    Produites = db.query(Produit).filter(Produit.id == Produit_id).first()
    if not Produites:
        raise HTTPException(status_code=404, detail="Votre Produit est  non trouvé")

    db.delete(Produites)
    db.commit()

