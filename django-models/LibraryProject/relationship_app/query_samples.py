from relationship_app.models import Author, Book, Library, Librarian

# def books_by_author(author_name):
#     author_name = Book.objects.filter(author=author)
#     author = Author.objects.get(name=author_name)
#     books = author.books.all()

#     for book in books:
#         print(book.title)

# def books_in_library(library_name):
#     library = Library.objects.get(name=library_name)
#     books = library.books.all()

#     for book in books:
#         print(book.title)

    
# def librarian_for_library(library_name):
#     library = Librarian.objects.get(library='')
#     librarian = library.librarian
#     print(f"The librarian for {library.name} is {librarian.name}")



def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()

    if author:

        books = Book.objects.filter(author=author)

        for book in books:
            print(book.title)
    else:
        print(f"No author found with {author_name}")

def book_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()

    if library:

        books = Book.objects.filter(library=library)

        for book in books:
            print(book.title)

    else:
        print(f"No library found with name {library_name}")

def librarian_for_library(library_name):

    library = Library.objects.filter(name=library_name).first()

    if library:

        librarian = Librarian.objects.filter(library=library).first()

        if librarian:
            print(f"The librarian for {library.name} is {librarian.name}")

        else:
            print(f"No librarian found for {library_name}")

    else:
        print(f"No library found with {library_name}")