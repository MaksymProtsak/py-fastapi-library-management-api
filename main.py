from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.get("/authors/", response_model=list[schemas.Author])
def get_all_authors(db: Session = Depends(get_db)):
    return crud.get_all_authors(db=db)
