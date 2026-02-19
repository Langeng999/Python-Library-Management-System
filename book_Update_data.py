from  book_Add_data import save_data
RED = "\033[31m"
RESET = "\033[0m"
def update_book(books):
    
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
    
    if not books:
            print(f"Book ISBN: {update_isbn} NOT FOUND")
    

    for b in books:
        if int(b["isbn"]) == update_isbn:

            print("\nBook Found!")
            print("===========| Update New Information |==========")

           
            while True: 
                new_title = input("Enter New Book Title: ").strip()
                if any(b["title"].strip().casefold() == new_title.casefold() for b in books):
                    print(f"Error: Book Title {RED}{new_title}{RESET} already exists. Please enter a different title.")
                    continue
          
                break  
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

   
