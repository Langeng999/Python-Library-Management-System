def display_book(books):
    print("==============| Display All Books |===========")
    print("-" * 46)
    for b in books:
        print(f"ISBN  : {b['isbn']}")
        print(f"Title : {b['title']}")
        print(f"Type  : {b['type']}")
        print(f"Author: {b['author']}")
        print("----------------------------------------------")