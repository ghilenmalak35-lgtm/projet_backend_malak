from pydantic import BaseModel,constr
class Create_user(BaseModel):
    name: str
    email: str
    password:constr(min_length=8, max_length=72)
    role: str
  
class User_login(BaseModel):
    password:str
    email:str

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    last_login: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True
