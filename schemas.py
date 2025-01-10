from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date


class BookCreate(BookBase):
    author_id: int


class BookDetail(BookBase):
    id: int
    author: Optional["AuthorBase"]

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List[BookBase] = []

    class Config:
        orm_mode = True
