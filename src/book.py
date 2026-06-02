class Book:
    
    def __init__(self, id, title, author):
        self.id=id
        self.title=title
        self.author=author
        self._is_available=True

    @property
    def is_available(self)->bool:
         return self._is_available
        
        
    def borrow_book(self):
        if self._is_available:
            self._is_available=False
        else:
            raise ValueError(f"{self.title} is not available for borrowing")    

    def _return_book(self):
        self._is_available=True

if __name__=="__main__":  # this code save from being executed when the model is imported as a module in another file
    print("pelınnn")