def search_data(books):
    print("==============| Search Books |===============")

    try:
        search_isbn = int(input("Enter ISBN to Search: "))
    except ValueError:
        print("\n")
        print("=================================")
        print("|  Error: PLEASE INPUT NUMBER   |")
        print("=================================")
        print("\n")
        return 

    for b in books:
        if int(b["isbn"]) == search_isbn:
            print(f"ISBN  : {b['isbn']}")
            print(f"Title : {b['title']}")
            print(f"Type  : {b['type']}")
            print(f"Author: {b['author']}")
            print("----------------------------------------------")
            return

    print(f"Book ISBN: {search_isbn} NOT FOUND")
