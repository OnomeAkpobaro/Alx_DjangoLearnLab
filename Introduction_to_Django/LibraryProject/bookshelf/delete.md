#Delete the book
'''python
book.delete()
remaining_books = Book.objects.all()
print(remaining_books)

#Expected Outcome: No books found (Empty QuerySet in output)