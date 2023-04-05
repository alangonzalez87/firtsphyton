with open("archivos/books.txt") as libros:
    for libro in libros:
        book=libro.strip()
        print(book)

    