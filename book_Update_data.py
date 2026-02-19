from  book_Add_data import save_data

def update_book(books):
    print("==============| Update Books |===============")
    found = False
    try:
        update_isbn = int(input("Enter Book ISBN to Update: "))
    except ValueError:
        print("\n")
        print("=================================")
        print("|  Error: PLEASE INPUT NUMBER   |")
        print("=================================")
        print("\n")
        return  
    if not found:
            print(f"Book ISBN: {update_isbn} NOT FOUND")
    

    for b in books:
        if int(b["isbn"]) == update_isbn:

            print("\nBook Found! Enter new information:")

            new_title = input("Enter New Book Title: ").strip()
            new_type = input("Enter New Book Type: ").strip()
            new_author = input("Enter New Book Author: ").strip()

            # Update values
            b["title"] = new_title
            b["type"] = new_type
            b["author"] = new_author

            save_data(books)   # Save updated list
            print("Book Updated Successfully!")

            found = True
            break

   
