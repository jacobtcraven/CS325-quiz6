class Editor:
    def add_book(self, book):
        self.book = []
        self.book.append(book)

    def remove_book(self, book):
        self.book.remove(book)

class Searcher:
    def search(self, book):
        self.book = ["book1", "book2", "book3"]
        if book in self.book:
            return True
        else:
            return False
        
class Lend:
    def __init__(self):
        self.checked_out = []

    def borrow(self, book):
        self.checked_out.append(book)
        print(f"Book {book} borrowed")
     
    def return_book(self, book):
        if book in self.checked_out:
            self.checked_out.remove(book)
            print(f"Book {book} returned")
        else:
            print(f"Book {book} not borrowed")

class Report:
    def __init__(self):
        self.borrowing = []
        self.today = "02-25-24"

    def reportBorrow(self, user):
        if user in self.borrowing:
            print(f"User {self.user} has checked out {self.book}")
    
    def reportOverdue(self, dueDate):
        if dueDate < self.today:
            print(f"User has overdue books")

    def popularBooks(self):
        popularBooks = ["book1", "book2", "book3"]
        for book in popularBooks:
            print(f"Book {book} is popular")

if __name__ == "__main__":
    editor = Editor()
    editor.add_book("book1")
    editor.remove_book("book1")
    searcher = Searcher()
    searcher.search("book1")
    lend = Lend()
    lend.borrow("book1")
    lend.return_book("book1")
    report = Report()
    report.reportBorrow("user1")
    report.reportOverdue("user1")
    report.popularBooks()

            
