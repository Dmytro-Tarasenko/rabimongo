from src.models import create_models
from src.import_data import import_data
from src.select_data import select_all_authors_and_book_count, select_avg_price_per_author

if __name__ == '__main__':
    # create_models()
    # import_data()
    select_all_authors_and_book_count()
    print(select_avg_price_per_author())