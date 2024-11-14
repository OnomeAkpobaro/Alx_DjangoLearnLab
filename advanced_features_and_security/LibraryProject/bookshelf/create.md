#book instance

'''python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


#Expected Outcome = A Book instance is successfully created.