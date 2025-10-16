books = [{"title": "Gone with the Wind", "author": "Margaret Mitchell"},
         {"title": "The Grapes of Wrath", "author": "John Steinbeck"},
         {"title": "Great Work of Time", "author": "John Crowley"},
         {"title": "The Green Bay Tree", "author": "Louis Bromfield"}
         ]


def show_menu():
    print(""
          "1.See books\n"
          "2.Add book\n"
          "3.Delete book\n"
          "4.Exit\n"
          "Please enter your selection!")


def clear_screen():
    print("\n" * 50)


def see_books():

    clear_screen()

    if not books:
        print("There are no books in this library, insert 0 for going back or 1 for exiting the application.")
        choice = input("Enter your selection: ")
        if choice == "0":
            return  # back to menu
        elif choice == "1":
            exit()

    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} - {book['author']}")
    print("0. Back")
    choice = input("Enter your selection: ")
    if choice == '0':
        return


see_books()

# while True:
#     show_menu()
