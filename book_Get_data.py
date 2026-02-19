import os

file_name = "library data.txt"
SEP = "|"

def get_data(file_name):
    books = []

    if not os.path.exists(file_name):
        print("Data not found")
        return books  

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(SEP)

            if parts[0].lower() == "isbn":
                continue

            if len(parts) != 4:
                continue 

       
            isbn, title, book_type, author= parts

            books.append({
                "isbn": isbn,
                "title": title,
                "type": book_type,
                "author": author,
        
            })

    return books
