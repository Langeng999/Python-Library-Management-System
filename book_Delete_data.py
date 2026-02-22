from book_Save_data import save_data 

#color
RED = "\033[31m"
RESET = "\033[0m"


def delete_book(books):
    print("=============| Delete by ISBN |============")

    delete_isbn = input("Enter ISBN to Delete: ").strip()
    if delete_isbn == "": #avoiding blank input
        print("ERROR: ISBN cannot be blank.")
        return

    try:
        delete_isbn = int(delete_isbn)
    except ValueError:
        print("\n")
        print("=================================")
        print("| TRY AGAIN: PLEASE INPUT NUMBER |")
        print("=================================")
        print("\n")

    for i, b in enumerate(books):
        if int(b["isbn"]) == delete_isbn:
            print(f"Deleted: ISBN: [{b['isbn']}] Title: {b['title']}")
            books.pop(i)
            save_data(books)
            return
    if not books:
        print(f"Book ISBN {RED}{delete_isbn}{RESET} NOT FOUND")
