class Member:
    def __init__(self, id, name, borrowed_books=None):
        self.id=id
        self.name=name
        self.borrowed_books=borrowed_books if borrowed_books is not None else []
        self.max_limit=3
    def add_book(self,*books):
        for book in books:
            if self.max_limit is None or len(self.borrowed_books) < self.max_limit:
                print(f"{book.title} successfully added to {self.name}'s borrowed books")
            else:
                print(f"Sorry {self.name}, you can't borrow more than 3 books")

    
    def remove_book(self,book):

        if book in self.borrowed_books:      
            self.borrowed_books.remove(book)
            print(f"{book.title} successfully removed from {self.name}'s borrowed books")
        else:
            print(f"Error.. {book.title} is not found in {self.name}'s borrowed books")


# ınherıtance test
class StandartMember(Member):
    def __init__(self, id,name,borrowed_books=None):
        super().__init__(id,name,borrowed_books)
        self.max_limit=3

class StudentMember(Member):
    def __init__(self, id,name,borrowed_books=None):
        super().__init__(id,name,borrowed_books)
        self.max_limit=5

class VIPMember(Member):
    def __init__(self, id,name,borrowed_books=None):
        super().__init__(id,name,borrowed_books)
        self.max_limit=None
