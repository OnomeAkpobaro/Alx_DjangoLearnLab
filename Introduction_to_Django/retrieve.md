#Retrieve the Book
'''python
retrieved_books = Book.objects.all()
for b in retrieved_books:
    print(b.title, b.author, b.publication_year)


#Expected Output: 1984 George Orwell 1949
