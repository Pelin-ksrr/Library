class Library:
    def __init__ (self):
        self.books=[]
        self.members=[]

    def add_book(self, *books):
        self.books.extend(books)

    def add_member(self, member):
        self.members.append(member)

    def is_book_available(self,book):
        return book in self.books and getattr(book, "is_available", True)

    def borrow_book(self,member,book):
        if self.is_book_available(book):
            book.borrow_book()
            member.add_book(book)
            print(f"{member.name} borrowed the {book.title}")
        else:
            print(f"{book.title} is not available")


    def return_book(self,member,book):
        if book in member.borrowed_books:
            member.remove_book(book)
            book.return_book()
            print(f"{member.name} returned the {book.title}")
        else:
            print(f"{book.title} is not borrowed by {member.name}")