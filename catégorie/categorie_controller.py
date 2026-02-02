from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import Categorie
from .schema import Create_categorie
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/categories", tags=["categories"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/createcategorie")
def CreateCategorie(categorie_data:Create_categorie, db: Session = Depends(get_db)):
    categorie = Categorie(title=categorie_data.title,description=categorie_data.description)
    db.add(categorie)
    db.commit()
    db.refresh(categorie)
    return categorie

@router.get("/categorieList")
def get_categories(db: Session = Depends(get_db)):
    return db.query(Categorie).all()
@router.get("/catgoriess/{categorie_id}", response_model=Create_categorie)
def get_categorie(categorie_id: int, db: Session = Depends(get_db)):
    categories = db.query(Categorie).filter(Categorie.id == categorie_id).first()
    if not categories:
        raise HTTPException(status_code=404, detail="catégorie non trouvé")
    return categories
@router.get("/categories/{categorie_title}", response_model=Create_categorie)
def get_categorietitle(categorie_title:str, db: Session = Depends(get_db)):
    categori = db.query(Categorie).filter(Categorie.title == categorie_title).first()
    if not categori:
        raise HTTPException(status_code=404, detail="user non trouvé")
    return categori
#methode patch
@router.patch("/categoriie/{Categorie_id}", response_model=Create_categorie)
def update_Categorie(Categorie_id: int, categorie_update:Create_categorie, db: Session = Depends(get_db)):
    categoriie = db.query(Categorie).filter(Categorie.id == Categorie_id).first()
    if not categoriie:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in categorie_update.dict(exclude_unset=True).items():
        setattr(categoriie, key, value)

    db.commit()
    db.refresh(categoriie)
    return categoriie
#delete 
@router.delete("/categorieee/{Categorie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Categorie(Categorie_id: int, db: Session = Depends(get_db)):
    Categorieees = db.query(Categorie).filter(Categorie.id == Categorie_id).first()
    if not Categorieees:
        raise HTTPException(status_code=404, detail="les Catégories non trouvé")

    db.delete(Categorieees)
    db.commit()