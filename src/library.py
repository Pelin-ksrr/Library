import sqlite3
from member import StandartMember, StudentMember, VIPMember
from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.members = {}     
        self.load_data_from_db()

    def load_data_from_db(self):
        self.books = []
        self.members = {}
        
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT id, title, author, is_available, borrowed_by_member_id FROM books")
        books_raw_data = cursor.fetchall()
        
        for row in books_raw_data:
            # row: (id, title, author, is_available, borrowed_by_member_id)
            db_book = Book(row[0], row[1], row[2])
            db_book.is_available = bool(row[3]) 
            self.books.append(db_book)
            
        self.books.sort(key=lambda x: x.title.lower())

        # 2. Üyeleri Veritabanından Yükle
        cursor.execute("SELECT id, name, member_type FROM members")
        for row in cursor.fetchall():
            m_id, m_name, m_type = row[0], row[1], row[2]
            if m_type == "1":
                new_member = StandartMember(m_id, m_name)
            elif m_type == "2":
                new_member = StudentMember(m_id, m_name)
            elif m_type == "3":
                new_member = VIPMember(m_id, m_name)
                
            self.members[m_name.lower()] = new_member
            
        
        for row in books_raw_data:
            book_id, borrowed_by = row[0], row[4]
            if borrowed_by is not None:
                # who borrowed the book
                for member in self.members.values():
                    if member.id == borrowed_by:
                        
                        target_book = next((b for b in self.books if b.id == book_id), None)
                        if target_book:
                            member.borrowed_books.append(target_book)

        conn.close()

    def add_book(self, book_title, book_author):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO books (title, author, is_available) VALUES (?, ?, 1)",
            (book_title, book_author)
        )
        
        conn.commit()
        conn.close()
        self.load_data_from_db()

    def register_member(self, name, member_type):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO members(name,member_type) VALUES(?,?)',
            (name, member_type)
        )
        conn.commit()
        conn.close()

        self.load_data_from_db()
        return self.members.get(name.lower())

    def search_book_binary(self, target_title):
        low = 0
        high = len(self.books) - 1
        
        while low <= high:
            mid = (low + high) // 2
            current_book_title = self.books[mid].title.lower()
            
            if current_book_title == target_title.lower():
                return self.books[mid]
            elif current_book_title < target_title.lower():
                low = mid + 1
            else:
                high = mid - 1
        return None

    def is_book_available(self, book):
        return book in self.books and book.is_available

    def borrow_book(self, member, book):
        """TÜM KONTROL ARTIK BURADA"""
        if not self.is_book_available(book):
            print(f"Error: {book.title} is not available")
            return
        
        if member.max_limit is not None and len(member.borrowed_books) >= member.max_limit:
            print(f"Sorry {member.name}, you can't borrow more than {member.max_limit} books")
            return
        
        book.is_available = False                      
        member.borrowed_books.append(book)            

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE books SET is_available = 0, borrowed_by_member_id = ? WHERE id = ?",
            (member.id, book.id)
        )
        conn.commit()
        conn.close()

        print(f"Success: {member.name} borrowed the {book.title}")

    def return_book(self, member, book):
        
        if book in member.borrowed_books:
            member.borrowed_books.remove(book) 
            book.is_available = True 

            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE books SET is_available = 1, borrowed_by_member_id = NULL WHERE id = ?",
                (book.id,)
            )
            conn.commit()
            conn.close()

            print(f"Success: {member.name} returned the {book.title}")
        else:
            print(f"Error: {book.title} is not borrowed by {member.name}")