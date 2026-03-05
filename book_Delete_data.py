from book_Save_data import save_data 

#color
RED = "\033[31m"
RESET = "\033[0m"


def delete_book(books):
    print("=============| Delete by ISBN |============")
    
    if not books:
        print("No books available to delete.")
        return
    
    while True:  # Add retry loop
        delete_isbn = input("Enter ISBN to Delete: ").strip()
        if delete_isbn == "":
            print("ERROR: ISBN cannot be blank.")
            continue
        
        try:
            delete_isbn = int(delete_isbn)
            break  # Valid input, exit retry
        except ValueError:
            print("\n=================================")
            print("| TRY AGAIN: PLEASE INPUT NUMBER |")
            print("=================================\n")
    found = False
    for i, b in enumerate(books):
        if int(b["isbn"]) == delete_isbn:
            print(f"Deleted: ISBN: [{b['isbn']}] Title: {b['title']}")
            books.pop(i)
            found = True
            save_data(books)
            return
    if not found:
        print(f"Book ISBN {RED}{delete_isbn}{RESET} NOT FOUND")

        
   
