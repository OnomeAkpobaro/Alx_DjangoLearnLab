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
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"The librarian for {library.name} is {librarian.name}")