from book import Book
from member import Member
from library import Library


def main():
    book1= Book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    book2= Book(2, "To Kill a Mockingbird", "Harper Lee")
    book3= Book( 3, "1984", "George Orwell")

    member1= Member(1, "Pelin")
    member1.add_book(book1,book2,book3)


    library=Library()
    library.add_book(book3,book2)


    library.add_member(member1)
    print(library.books)
    print(f"total books pelin has: {len(member1.borrowed_books)}")

    print("--- test 1- the number of books ---")
    print(f"Pelin's books: {len(member1.borrowed_books)}")

    print("\n--- test 2: List Content ---")
    print(member1.borrowed_books)


if __name__=="__main__":
    main()


