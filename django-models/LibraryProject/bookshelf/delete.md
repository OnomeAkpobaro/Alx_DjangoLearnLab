#Delete the book
'''python

from bookshelf.models import Book
book.delete()
remaining_books = Book.objects.all()
print(remaining_books)

#Expected Outcome: No books found (Empty QuerySet in output)