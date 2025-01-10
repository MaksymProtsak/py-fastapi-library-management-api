from sqlalchemy.orm import Session
import models
import schemas


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()


def get_author(db: Session, author_id: int):
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == author_id).first()


def get_author_by_name(db: Session, name: str):
    return (
        db.query(models.DBAuthor).filter(models.DBAuthor.name == name).first()
    )


def create_author(
        db: Session,
        author: schemas.AuthorCreate
) -> models.DBAuthor:
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio,

    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def update_author(
        db: Session,
        db_author: models.DBAuthor,
        author: schemas.Author
) -> models.DBAuthor:
    for key, value in author.dict().items():
        if not (getattr(db_author, key) == getattr(author, key)):
            setattr(db_author, key, value)
            db.commit()
    return db_author


def delete_author(db: Session, author_id: int) -> models.DBAuthor:
    db_author = get_author(db, author_id)
    db.delete(db_author)
    db.commit()

    return db_author
