# from relationship_app.models import Author, Book, Library, Librarian


# def books_by_author(author_name):
#     #Get the author name using filter to avoid raising an exception if not found
#     author = Author.objects.get(name=author_name)       #returns None if no match is found

#     if author:
#             #use the reverse relation to get all books for the author
#         books = Book.objects.filter(author=author)      #filter books by the author

#         for book in books:
#             print(book.title)
#     else:
#         print(f"No author found with {author_name}")

# def book_in_library(library_name):
#     #Get the library object using filter to avoid exceptions
#     library = Library.objects.get(name=library_name)
#         #filter books associated with the library
#     books = library.books.all()       #filter books by the library

#     for book in books:
#             print(book.title)


# def librarian_for_library(library_name):
#     #Get the library object using filter to avoid exceptions
#     library = Library.objects.get(name=library_name)


#         #Get the librarian using filter to avoid exceptions
#     librarian = Librarian.objects.get(library='')

#     if librarian:
#             print(f"The librarian for {library.name} is {librarian.name}")

#     else:
#             print(f"No librarian found for {library_name}")

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author_name = Book.objects.filter(author=author)
    author = Author.objects.get(name=author_name)
    books = author.books.all()

    for book in books:
        print(book.title)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()

    for book in books:
        print(book.title)

    
def librarian_for_library(library_name):
    library = Librarian.objects.get(library='')
    librarian = library.librarian
    print(f"The librarian for {library.name} is {librarian.name}")