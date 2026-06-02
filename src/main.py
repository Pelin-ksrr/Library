from book import Book
from member import Member
from library import Library


def main():
    book1= Book(
    1, "The Great Gatsby", "F. Scott Fitzgerald"
    )

    book2= Book(
       2, "To Kill a Mockingbird", "Harper Lee"
    )

    book3= Book(
       3, "1984", "George Orwell"
    )

    member1= Member(1, "Pelin")

    print(book1.author)

    library=Library()
    library.add_book(book3,book2)


    library.add_member(member1)


    member1.add_book(book1)
    print(library.books)

if __name__=="__main__":
    main()
