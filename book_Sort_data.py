from book_Save_data import save_data as save
def sort_book_by_isbn(books):
    if not books:
        print("No book found!")
        return

    while True:
        print("\n=============| Sort Book (ISBN) |============")
        print("|          1. Ascending Order               |")
        print("|          2. Descending Order              |")
        print("|          0. Back to menu                  |")
        print("============================================")

        try:
            sort_choice = int(input("Enter Choice [0-2]: "))
        except ValueError:
            print("\n")
            print("=================================")
            print("|  Error: PLEASE INPUT NUMBER   |")
            print("=================================")
            print("\n")
            continue  

        if sort_choice == 0:
            return

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
            print(f"ISBN: {b['isbn']} | Title: {b['title']} | Type: {b['type']} | Author: {b['author']}")
        print("======================================")
        return
