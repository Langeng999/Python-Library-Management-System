from book_Save_data import save_data

def input_not_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("ERROR: This field cannot be blank. Please input again.")
        else:
            return value

def add_book(books):
    print("==============| Add Book |===============")

    while True:
        try:
            isbn = int(input("Enter Book ISBN: "))
        except ValueError:
            print("ERROR: ISBN must be a number. Try again.")
            continue

        if any(int(b["isbn"]) == isbn for b in books):
            print("ERROR: This ISBN already exists. Try another one.")
            continue

        break 

    title  = input_not_blank("Enter Book Title: ")
    btype  = input_not_blank("Enter Book Type: ")
    author = input_not_blank("Enter Book Author: ")

    new_book = {
        "isbn": isbn,
        "title": title,
        "type": btype,
        "author": author,
    }

    books.append(new_book)
    save_data(books)
    print("Book Successfully Added!")
