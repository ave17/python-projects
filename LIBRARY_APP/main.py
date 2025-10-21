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


def add_book():

    clear_screen()
    print("Add a new book")
    title = input("Insert book title: ").strip()
    while title == "":
        title = input(
            "Title cannot be empty. Please insert a book title: ").strip()

    author = input("Insert book author: ").strip()
    while author == "":
        author = input(
            "Author cannot be empty. Please insert book author: ").strip()

    new_book = {"title": title, "author": author}
    books.append(new_book)
    print("Book added successfully!")
    input("Press Enter to return to the main menu...")
    return


def delete_book(): 
    clear_screen()
    print("Delete a book: \n")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} - {book['author']}")
    print("0. Back")

    choice = input("Please specify which book should be deleted: ")
    if choice == '0':
        return #back to menu
    else:
        try:
            index = int(choice) - 1 #convert choice to list index.
            if 0 <= index < len(books):
                deleted_book = books.pop(index)
                print(f"Deleted: {deleted_book['title']} - {deleted_book['author']}")
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")
        input("Press Enter to return to the main menu.")
        return
    

while True:
    show_menu()
    choice = input("Enter your selection: ")
    if choice == "1":
        see_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid selection, please try again.")
