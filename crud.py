from sqlalchemy.orm import Session
import models


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()
