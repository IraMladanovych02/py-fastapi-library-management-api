from pydantic import BaseModel
from datetime import date


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    book_id: int


class Author(AuthorBase):
    id: int
    books: Book

    class Config:
        orm_mode = True
