from fastapi import FastAPI, Depends, HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import engine, Base, SessionLocal
from .model import User
from .schema import Create_user,User_login,UserResponse
from .securiter import create_access_token
from datetime import timedelta
app = FastAPI()
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/users", tags=["users"])
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
def hashPassword(password: str) -> str:
    return pwd_context.hash(password[:72])

def verifyPassword(password: str, hashed_password: str)  :
    return pwd_context.verify(password, hashed_password)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def loginuser(userlogin:User_login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email ==userlogin.email).first()
    if not user:
        return False
    if not verifyPassword(userlogin.password, user.password):
        return False
    access_token = create_access_token(
        data={"sub": user.email, "user_id": user.id},
        expires_delta=timedelta(minutes=30)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user":user
    }



@router.post("/createuser")
def CreateUser(user_data:Create_user, db: Session = Depends(get_db)):
    user = User(name=user_data.name,email=user_data.email,password=hashPassword(user_data.password),role=user_data.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
@router.get("/userList")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Users non trouvé")
    return user
@router.get("/user/{user_name}", response_model=UserResponse)
def get_username(user_name:str, db: Session = Depends(get_db)):
    usere = db.query(User).filter(User.name == user_name).first()
    if not usere:
        raise HTTPException(status_code=404, detail="user non trouvé")
    return usere
#methode patch
@router.patch("/usere/{User_id}", response_model=Create_user)
def update_Student(User_id: int, user_update:Create_user, db: Session = Depends(get_db)):
    useres = db.query(User).filter(User.id == User_id).first()
    if not useres:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(useres, key, value)

    db.commit()
    db.refresh(useres)
    return useres
#delete 
@router.delete("/useree/{User_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Student(User_id: int, db: Session = Depends(get_db)):
    Useres = db.query(User).filter(User.id == User_id).first()
    if not Useres:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    db.delete(Useres)
    db.commit()