from book_Get_data import get_data 
from book_Add_data import add_book as add
from book_Display_data import display_book as display
from book_Search_data import search_data as search
from book_Update_data import update_book as update
from book_Sort_data import sort_book_by_isbn as sort
from book_Delete_data import delete_book as delete

books = get_data("library data.txt")

while True:
    print("==========| Library Management System |==========")
    print("|            1. Add Book                        |")
    print("|            2. Display All Book                |")
    print("|            3. Search Book                     |")
    print("|            4. Update Book                     |")
    print("|            5. Sort Book                       |")
    print("|            6. Delete Book                     |")
    print("|            0. Exit System                     |")
    print("=================================================")

    try:
        choice = int(input("Enter your choice: "))
        print("\n")
    except ValueError:
        print("\n")
        print("=================================")
        print("|  Error: PLEASE INPUT NUMBER   |")
        print("=================================")
        print("\n")
        continue  

    if choice == 1:
        add(books)
        print("\n")
    elif choice == 2:
        display(books)
        print("\n")
    elif choice == 3:
        search(books)
        print("\n")
    elif choice == 4:
        update(books)
        print("\n")
    elif choice == 5:
        sort(books)
        print("\n")
    elif choice == 6:
        delete(books)
        print("\n")
    elif choice == 0:
        print("Exiting... Bye!")
        break

    else:
        print("Invalid choice. Please enter 0-6.")

 