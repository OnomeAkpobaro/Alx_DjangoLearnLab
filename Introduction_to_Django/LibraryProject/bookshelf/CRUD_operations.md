#CRUD_operations

#create
'''python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

#Expected Outcome = A Book instance is successfully created.

#retrieve

retrieved_books = Book.objects.all()
for b in retrieved_books:
    print(b.title, b.author, b.publication_year)


#Expected Output: 1984 George Orwell 1949

#update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

#Expected Output: Title updated to "Nineteen Eighty-Four".

#delete
book.delete()
remaining_books = Book.objects.all()
print(remaining_books)

#Expected Outcome: No books found (Empty QuerySet in output)
