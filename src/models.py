# CREATE TABLE authors (
#     author_id INT PRIMARY KEY,
#     author_name VARCHAR(50)
# );

# CREATE TABLE books (
#     book_id INT PRIMARY KEY,
#     title VARCHAR(100),
#     author_id INT,
#     genre VARCHAR(50),
#     publication_year INT,
#     price DECIMAL(10, 2),
#     FOREIGN KEY (author_id) REFERENCES authors(author_id)
# );
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Mapped, DeclarativeBase

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List


# declarative base class
class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"


    author_id: Mapped[int] = mapped_column(primary_key=True)
    author_name: Mapped[str]

    books: Mapped[List["Book"]] = relationship()



class Book(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    genre: Mapped[str] = mapped_column(String(50))
    publication_year: Mapped[int]
    price: Mapped[float]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.author_id"))


engine = create_engine("sqlite:///authors_books.sqlite")

Base.metadata.create_all(engine)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()
print("Session created")