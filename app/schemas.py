from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


#Pydantic is a data validation and parsing library
class CreateUser(BaseModel):
    email:EmailStr
    password: str
    
    
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    
    class Config:
        orm_mode=True
        
class UserLogin(BaseModel):
    email:EmailStr
    password: str
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id: Optional[str] = None



class PostBase(BaseModel):
    title:str
    content: str
    published:bool=True
    #rating: Optional[int] = None
    
class CreatePost(PostBase):
    pass 
    
class UpdatePost(BaseModel):
    title:str
    content: str
    published:bool
    
class PostResponse(PostBase):
    id: int
    created_at: datetime
    # owner_id: int
    owner: UserResponse
    
    class Config:
        orm_mode=True
        
        
