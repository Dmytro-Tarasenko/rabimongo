# INSERT INTO authors VALUES
# (1, 'J.D. Salinger'),
# (2, 'Harper Lee'),
# (3, 'George Orwell'),
# (4, 'Jane Austen'),
# (5, 'F. Scott Fitzgerald');
#
# INSERT INTO books VALUES
# (1, 'The Catcher in the Rye', 1, 'Fiction', 1951, 19.99),
# (2, 'To Kill a Mockingbird', 2, 'Fiction', 1960, 24.99),
# (3, '1984', 3, 'Dystopian', 1949, 14.99),
# (4, 'Pride and Prejudice', 4, 'Romance', 1813, 12.99),
# (5, 'The Great Gatsby', 5, 'Fiction', 1925, 18.99);
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Author, Book, Base
import json

def import_data():

    books = authors = []

    with open('authors.json', 'r', encoding='utf-8') as fin:
        data = json.load(fin)
        books = data['books']
        authors = data['authors']

    engine = create_engine("sqlite:///authors_books.sqlite")

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)

    with DBSession() as session:
        for author in authors:
            author_orm = Author(**author)
            session.add(author_orm)

        for book in books:
            book_orm = Book(**book)
            session.add(book_orm)

        session.commit()
