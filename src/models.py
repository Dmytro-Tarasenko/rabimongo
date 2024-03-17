from sqlalchemy import String, ForeignKey, create_engine
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship, sessionmaker
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

def create_models():
    engine = create_engine("sqlite:///authors_books.sqlite")

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    # Session = sessionmaker(bind=engine)
    # session = Session()