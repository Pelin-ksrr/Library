class Member:
    def __init__(self, id, name, borrowed_books=None):
        self.id=id
        self.name=name
        self.borrowed_books=borrowed_books if borrowed_books is not None else []

    def add_book(self,book):
        self.borrowed_books.append(book)
    
    def remove_book(self,book):
        self.borrowed_books.remove(book)
        