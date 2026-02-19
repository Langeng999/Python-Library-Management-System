from book_Save_data import save_data as data
RED = "\033[31m"
RESET = "\033[0m"
def delete_book(books):
    
    while True:
        print("=============| Delete Book |============")
        print("|            1. Delete By ISBN         |")
        print("|            2. Delete By Title        |")
        print("|            0. Back to menu           |")
        print("========================================")
        try:
            delete_choice = int(input("Enter Choice: "))
        except ValueError:
            print("\n")
            print("=================================")
            print("|  Error: PLEASE INPUT NUMBER   |")
            print("=================================")
            print("\n")
            continue  
        if delete_choice == "":
                print("=================================")
                print("| Error: TITLE CAN NOT BE BLANK |")
                print("=================================")
                continue
        if delete_choice == 1:
            print("=============| Delete by ISBN |============")
            try:
                delete_isbn = int(input("Enter ISBN to Delete: "))
            except:
                print("\n")
                print("Error: PLEASE INPUT NUMBER ONLY")
                return
            
            if delete_isbn == "":
                print("ERROR: Title cannot be blank.")
                continue

            for i, b in enumerate(books):
                if int(b["isbn"]) == delete_isbn:
                    print(f"Deleted: [{b['isbn']}] {b['title']}")
                    books.pop(i)
                    data(books)
                    return
                    
            print(f"Book ISBN {delete_isbn} NOT FOUND")
        elif delete_choice == 2:
            print("=============| Delete by Title |============")
            delete_title =input("Enter Title to Delete: ").strip()
            
            title = delete_title.casefold()
            if delete_title == "":
                print("ERROR: Title cannot be blank.")
                continue

            if not books: 
                print(f"Book Title '{delete_title}' NOT FOUND")
            for i, b in enumerate(books):
                if int(b["isbn"]) == title:
                    print(f"Deleted: [{b['isbn']}] {b['title']}")
                    books.pop(i)
                    data(books)
                    return
            
            if delete_title.isdigit():
                print("ERROR: Title Must Contain Letter.")
                continue

            print(f"Book Title: {RED}{delete_title}{RESET} NOT FOUND")
            return
        else:
            print("Invalid Choice...!")
