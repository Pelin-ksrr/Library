class Member:
    def __init__(self, id, name, borrowed_books=None):
        self.id=id
        self.name=name
        self.borrowed_books=borrowed_books if borrowed_books is not None else []
        self.max_limit=3



# inheritance test
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
