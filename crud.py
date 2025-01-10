from sqlalchemy.orm import Session
import models


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()


def get_author(db: Session, author_id: int):
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == author_id).first()
