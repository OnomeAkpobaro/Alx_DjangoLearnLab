#Update the Title

'''python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

#Expected Output: Title updated to "Nineteen Eighty-Four".