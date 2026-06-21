from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    is_available: bool = True 

if __name__ == "__main__":
    print("pelinnn")





""" .......tradational OOP version.....

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title

if __name__ == "__main__":
    print("pelinnn")
"""


