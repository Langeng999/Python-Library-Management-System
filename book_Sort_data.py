from book_Save_data import save_data as save
def sort_book_by_isbn(books):
    if not books:
        print("No book found!")
        return

    while True: #menu chosing option sort book (from small to big or from big to small)
        print("\n=============| Sort Book (ISBN) |============")
        print("|          1. Ascending Order               |")
        print("|          2. Descending Order              |")
        print("|          0. Back to menu                  |")
        print("============================================")

        try:
            sort_choice = int(input("Enter Choice [0-2]: "))
        except ValueError: #if user input letter it will show error
            print("\n")
            print("=================================")
            print("|  Error: PLEASE INPUT NUMBER   |")
            print("=================================")
            print("\n")
            continue  

        if sort_choice == 0: #select 0 to back to main menu
            print("Back to menu...!")
            break

        if sort_choice == 1: 
            books.sort(key=lambda b: int(b["isbn"]))
        elif sort_choice == 2:
            books.sort(key=lambda b: int(b["isbn"]), reverse=True)
        else:
            print("Invalid choice. Please enter 0-2.")
            continue

        save(books)
        print("\n===========| Sorted Books |===========")
        for b in books:
            print(f"ISBN  : {b['isbn']}")
            print(f"Title : {b['title']}")
            print(f"Type  : {b['type']}")
            print(f"Author: {b['author']}")
            print("----------------------------------------------")
        
        return
