file_name = "library data.txt"
SEP = "|"

def save_data(books): 
    #encoding is use for another language input 
    with open(file_name, "w", encoding="utf-8") as file:
       
        for b in books:
            isbn = str(b.get("isbn", "")).replace(SEP, "/")
            title = str(b.get("title", "")).replace(SEP, "/")
            book_type = str(b.get("type", "")).replace(SEP, "/")
            author = str(b.get("author", "")).replace(SEP, "/")

            file.write(f"{isbn}{SEP}{title}{SEP}{book_type}{SEP}{author}\n")
