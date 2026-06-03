from book import Book
from member import StandardMember, StudentMember, VIPMember 
from library import Library

def main():
    library = Library()
    
    book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
    book3 = Book(3, "1984", "George Orwell")
    library.add_book(book1, book2, book3)
    
    active_members = {}
    id_counter = 1


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
            
            new_member = None 

            if member_type == "1":
                new_member = StandardMember(id_counter, name)
            elif member_type == "2":
                new_member = StudentMember(id_counter, name)
            elif member_type == "3":
                new_member = VIPMember(id_counter, name)
            else:
                print("Invalid member type. Registration failed.")
            
            if new_member is not None:
                library.add_member(new_member)
                active_members[name.lower()] = new_member
                print(f"Member {name} registered successfully with ID: {id_counter}")
                id_counter += 1

        elif choice == "3":
            print("\n--- Borrow a Book ---")
            member_name = input("Enter member name: ").lower()
            
            if member_name in active_members:
                member = active_members[member_name]
                print(f"Available books: {library.books}")
                book_title = input("Enter the exact title of the book to borrow: ")
                
                target_book = None
                for b in library.books:
                    if b.title.lower() == book_title.lower():
                        target_book = b
                        break
                
                if target_book:
                    member.add_book(target_book)
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