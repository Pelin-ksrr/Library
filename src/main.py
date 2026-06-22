from book import Book
from member import StandartMember, StudentMember, VIPMember 
from library import Library

def main():
    library = Library()
    
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")
    
    

    while True:
        print("\n***Library Management System***")
        print("1. List all books")
        print("2. Register new member")
        print("3. Borrow Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"\nList of books:\n{library.books}")

        elif choice == "2":
            name = input("Enter member name: ")
            print("Select member type:\n1- Standard\n2- Student\n3- VIP")
            member_type = input("Enter your choice (1-3): ")
            
            
            new_member = library.register_member(name, member_type)
            
            if new_member is not None:
                print(f"Member {name} registered successfully with ID: {new_member.id}")
            else:
                print("Invalid member type. Registration failed.")

        elif choice == "3":
            print("\n--- Borrow a Book ---")
            member_name = input("Enter member name: ").lower()
            
            
            if member_name in library.members:
                #print(f"Available books: {library.books}")
                only_available=[book for book in library.books if book.is_available]
                print(f"available books:{only_available}")
                book_title = input("Enter the exact title of the book to borrow: ")
                
                # binary search
                target_book = library.search_book_binary(book_title)
                
                if target_book:
                    # logic of borrowing
                    member = library.members[member_name]
                    library.borrow_book(member, target_book)
                else:
                    print("Error: The requested book is not found in the library.")
            else:
                print("Error: No registered member found with that name.")

        elif choice == "4":
            print("\nShutting down the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()