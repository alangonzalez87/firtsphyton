
chosen_volume = input("Which volume of scripture would you like to learn about? ")



mayor_scripture= -1
libro_mayor=""

with open("archivos/books_and_chapters.txt") as libros:
    for libro in libros:
        new_libro=libro.split(":")
        book = new_libro[0].strip()
        chapter=int(new_libro[1])
        testamento=new_libro[2].strip()
        

        if testamento.lower() == chosen_volume.lower():
            print(f"Scripture: {book}, Book: {testamento}, Chapters: {chapter}")

            if chapter > mayor_scripture:
             mayor_scripture=chapter
             libro_mayor= book
    
            

            
print(f"The book with the most chapters is: {libro_mayor}")
print(f"It has {mayor_scripture} chapters.")
