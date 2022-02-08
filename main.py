from library import Library


def print_separator():
    print("---------------------------------------------")


def get_name_input():
    return input("Type in your name: ").capitalize()


def get_book_input():
    return input("Book name: ").capitalize()


def display_books(lib, display_borrowed=False):
    if lib.get_available_books():
        print("Available books:- ")
        [print(f"-{book}") for book in lib.get_available_books()]
    else:
        print("No available books to display!")

    print_separator()

    if display_borrowed:
        if lib.get_borrowed_books():
            print("Borrowed Books:- ")
            for book_name, owner in lib.get_borrowed_books().items():
                print(f"-{book_name}: {owner}")
        else:
            print("No borrowed books to display!")


def main():
    book_list = ["Physics", "Chemistry", "Biology", "Maths", "Hindi", "English", "Geography"]
    lib = Library("Tanmay's Library", book_list)
    print(f"Welcome to {lib.name}!")

    while True:
        print(f"What would you like to do?")
        choice = input(
            "\t(1) to display all the books\n\t(2) to borrow a book\n\t(3) to return a book\n\t(4) to add a book\n\t("
            "5) to quit\n")

        if choice == "1":
            display_books(lib, True)

        elif choice == "2":
            display_books(lib)
            book_name = get_book_input()
            if lib.is_book_available(book_name):
                username = get_name_input()
                lib.borrow_book(book_name, username)
                print(f"{book_name} borrowed by {username}")
            elif lib.is_book_borrowed(book_name):
                print(f"{book_name} has already been borrowed by {lib.get_borrowed_books().get(book_name)}")
            else:
                print(f"Sorry, {book_name} is currently not available in the library!")

        elif choice == "3":
            if lib.get_borrowed_books():
                book_name = get_book_input()
                if lib.is_book_borrowed(book_name):
                    username = get_name_input()
                    if username == lib.get_book_owner(book_name):
                        lib.return_book(book_name)
                        print(f"{book_name} returned successfully!")
                    else:
                        print(f"{book_name} was borrowed by somebody else!")
                else:
                    print(f"{book_name} is not borrowed yet!")
            else:
                print("No book is currently borrowed!")
        
        elif choice == "4":
            book_name = get_book_input()
            if lib.is_book_available(book_name):
                print(f"{book_name} is already available in our Library!")
            else:
                lib.add_book(book_name)

        elif choice == "5":
            break
        else:
            print("Invalid choice.. Please try again!")

        print_separator()


if __name__ == "__main__":
    main()
