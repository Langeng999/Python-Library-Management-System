from  book_Add_data import save_data
RED = "\033[31m"
RESET = "\033[0m"

def input_not_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("ERROR: This field cannot be blank. Please input again.")
        else:
            return value
        
def update_book(books):
    print("===========| Update Book Information |==========")
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
   
    for b in books:
        if int(b["isbn"]) == update_isbn:
            print("\nBook Found!") 
            print("===========| Input New Information |==========")

           
            while True:  #if title duplicate it'll show message
                new_title = input_not_blank("Enter New Book Title: ").strip()
                if any(b["title"].strip().casefold() == new_title.casefold() for b in books):
                    print(f"Error: Book Title {RED}{new_title}{RESET} already exists. Please enter a different title.")
                    continue
                break
            
            
            while True: 
                #handle blank input 
                new_type = input_not_blank("Enter New Book Type: ").strip()
                #handle number input
                if new_type.isdigit():
                    print("Book Type can not be NUMBER")
                    continue
                break
            

            while True:
                #handle blank input
                new_author = input_not_blank("Enter New Book Author: ").strip()
                #handle number input
                if new_author.isdigit():
                    print("Book Author can not be Number")
                    continue
                break



            # Update values
            b["title"] = new_title
            b["type"] = new_type
            b["author"] = new_author

            save_data(books)   # Save updated list
            print("Book Updated Successfully!")

            found = True
            break

    if not found:
        print(f"Book ISBN: {RED} {update_isbn} {RESET}NOT FOUND")
   
