from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from .model import Client
from .schema import Create_client
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/clients", tags=["clients"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/createclient")
def CreateClient(client_data:Create_client, db: Session = Depends(get_db)):
    client = Client(firstname=client_data.firstname,lastname=client_data.lastname,email=client_data.email,tel=client_data.tel,adresse=client_data.adresse)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.get("/clientList")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()
@router.get("/clientss/{client_id}", response_model=Create_client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="client non trouvé")
    return client
@router.get("/clientes/{client_firstname}", response_model=Create_client)
def get_clientname(client_firstname:str, db: Session = Depends(get_db)):
    cliente = db.query(Client).filter(Client.firstname == client_firstname).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="user non trouvé")
    return cliente
#methode patch
@router.patch("/cliente/{Client_id}", response_model=Create_client)
def update_Client(Client_id: int, client_update:Create_client, db: Session = Depends(get_db)):
    clientee = db.query(Client).filter(Client.id == Client_id).first()
    if not clientee:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in client_update.dict(exclude_unset=True).items():
        setattr(clientee, key, value)

    db.commit()
    db.refresh(clientee)
    return clientee
#delete 
@router.delete("/clientees/{Client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Student(Client_id: int, db: Session = Depends(get_db)):
    Clientes = db.query(Client).filter(Client.id == Client_id).first()
    if not Clientes:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    db.delete(Clientes)
    db.commit()

