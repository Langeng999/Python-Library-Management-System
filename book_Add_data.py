from book_Save_data import save_data

RED = "\033[31m"
RESET = "\033[0m"
GREEN = "\033[32m"

#function use for avoiding blank option
def input_not_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("ERROR: This field cannot be blank. Please input again.")
        else:
            return value

def add_book(books):
    print("==============| Add Book |===============")

    # ----- Step 1: Input unique ISBN -----
    while True:
        try:
            isbn = int(input("Enter Book ISBN: "))
        except Exception :
            print("ERROR: ISBN must be a number. Try again.")
            continue

        if any(int(b["isbn"]) == isbn for b in books):
            print(f"ERROR: ISBN {RED}{isbn}{RESET} already exists. Try another one.")
            continue

        break  

    # ----- Step 2: Input unique title -----
    #handle blank field and duplicate title
    while True:
        title = input_not_blank("Enter Book Title: ") #check blank 
        if any(b["title"].strip().casefold() == title.casefold() for b in books):
            print(f"Error: Book Title {RED}{title}{RESET} already exists. Please enter a different title.")
            continue
        break  

    # ----- Step 3: Input other fields -----
    #handle number input
    while True: 
        btype  = input_not_blank("Enter Book Type: ")
        #handle number input
        if btype.isdigit():
            print("Book Type can not be Number")
            continue    
        break
    
    #handle number input
    while True:
        author = input_not_blank("Enter Book Author: ")
        if author.isdigit():
            print("Book Author can not be Number")
            continue
        break

    #save new input book to file
    new_book = {
        "isbn": isbn,
        "title": title,
        "type": btype,
        "author": author,
    }

    #add new book to file
    books.append(new_book)
    save_data(books)
    print(f"Book '{GREEN}{title}{RESET}' Successfully Added!")
