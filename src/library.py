from member import StandartMember, StudentMember, VIPMember

class Library:
    def __init__(self):
        self.books = []
        self.members = {}     # Key: üye ismi (küçük harf), Value: Üye nesnesi
        self.id_counter = 1   

    def add_book(self, *books):
        self.books.extend(books)
        self.books.sort(key=lambda x: x.title.lower())

    def register_member(self, name, member_type):
        new_member = None 
        if member_type == "1":
            new_member = StandartMember(self.id_counter, name)
        elif member_type == "2":
            new_member = StudentMember(self.id_counter, name)
        elif member_type == "3":
            new_member = VIPMember(self.id_counter, name)
        
        if new_member is not None:
            self.members[name.lower()] = new_member
            self.id_counter += 1
            return new_member
        return None

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
        # Kitap listede var mı ve is_available durumu True mu?
        return book in self.books and book.is_available

    def borrow_book(self, member, book):
        """TÜM KONTROL ARTIK BURADA"""
        # 1. Kitap müsait mi?
        if not self.is_book_available(book):
            print(f"Error: {book.title} is not available")
            return

        # 2. Üyenin limiti dolmuş mu? (Kontrolü artık merkez yapıyor!)
        if member.max_limit is not None and len(member.borrowed_books) >= member.max_limit:
            print(f"Sorry {member.name}, you can't borrow more than {member.max_limit} books")
            return

        # 3. Her şey okeyse işlemleri yap
        book.is_available = False                     # Kitabı kapattık
        member.borrowed_books.append(book)            # Üyenin sepetine ekledik
        print(f"Success: {member.name} borrowed the {book.title}")

    def return_book(self, member, book):
        """İADE MANTIĞI DA BURADA"""
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)        # Üyenin sepetinden çıkardık
            book.is_available = True                  # Kitabı tekrar boşa çıkardık
            print(f"Success: {member.name} returned the {book.title}")
        else:
            print(f"Error: {book.title} is not borrowed by {member.name}")