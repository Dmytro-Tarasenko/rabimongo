from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker

from .models import Author, Book, Base

from collections import namedtuple


engine = create_engine("sqlite:///authors_books.sqlite")

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def select_all_authors_and_book_count():
    with DBSession() as session:
        result = session.query(Author.author_name, func.count(Book.book_id))\
                .select_from(Author)\
                .join(Book)\
                .group_by(Author.author_id)\
                .all()
        for row in result:
            print(row)

# SELECT author_name, AVG(price) AS average_price
# FROM authors AS a
# JOIN books AS b ON a.author_id=b.author_id
# GROUP BY a.author_id
def select_avg_price_per_author():
    with DBSession() as session:
        result = session.query(Author.author_name, func.avg(Book.price))\
                .select_from(Author)\
                .join(Book)\
                .group_by(Author.author_id)\
                .all()
        for row in result:
            print(row)