FILE_NAME = "books.txt"


def add_book():
    title = input("Book title: ")
    author = input("Author: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{title}|{author}\n")

    print("Book added successfully!\n")


def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

            if not books:
                print("No books found.\n")
                return

            print("\nLibrary Books")
            print("-" * 30)

            for i, book in enumerate(books, start=1):
                title, author = book.strip().split("|")
                print(f"{i}. {title} - {author}")

            print()

    except FileNotFoundError:
        print("No books found.\n")


def search_book():
    keyword = input("Enter title: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for book in file:
                title, author = book.strip().split("|")

                if keyword in title.lower():
                    print(f"{title} - {author}")
                    found = True

            if not found:
                print("Book not found.")

    except FileNotFoundError:
        print("Library is empty.")


def delete_book():
    keyword = input("Enter title to delete: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        with open(FILE_NAME, "w") as file:
            deleted = False

            for book in books:
                title, author = book.strip().split("|")

                if keyword != title.lower():
                    file.write(book)
                else:
                    deleted = True

        if deleted:
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    except FileNotFoundError:
        print("Library is empty.")


def menu():
    while True:

        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


menu()