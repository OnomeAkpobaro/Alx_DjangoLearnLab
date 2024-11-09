from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_name):
    #Get the author name using filter to avoid raising an exception if not found
    author = Author.objects.filter(name=author_name).first()        #returns None if no match is found

    if author:
            #use the reverse relation to get all books for the author
        books = Book.objects.filter(author=author)      #filter books by the author

        for book in books:
            print(book.title)
    else:
        print(f"No author found with {author_name}")

def book_in_library(library_name):
    #Get the library object using filter to avoid exceptions
    library = Library.objects.filter(name=library_name).first()

    if library:
        #filter books associated with the library
        books = Book.objects.filter(library=library)        #filter books by the library

        for book in books:
            print(book.title)

    else:
        print(f"No library found with name {library_name}")

def librarian_for_library(library_name):
    #Get the library object using filter to avoid exceptions
    library = Library.objects.filter(name=library_name).first()

    if library:
        #Get the librarian using filter to avoid exceptions
        librarian = Librarian.objects.filter(library=library).first()

        if librarian:
            print(f"The librarian for {library.name} is {librarian.name}")

        else:
            print(f"No librarian found for {library_name}")

    else:
        print(f"No library found with {library_name}")