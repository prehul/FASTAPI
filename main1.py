from typing import List
from fastapi import Response, Depends, status, HTTPException, FastAPI
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
from routers import blog,user,authentication
# class Hash():
#     def bcrypt(password: str):
#         return pwd_cxt.hash(password)

#     def verify(hashed_password,plain_password):
#         return pwd_cxt.verify(plain_password,hashed_password)
# from blog.repository import blog
app = FastAPI()
# router = APIRouter(
#     prefix="/blog",
#     tags=['Blogs']
# )
# from sqlalchemy import create_engine

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
