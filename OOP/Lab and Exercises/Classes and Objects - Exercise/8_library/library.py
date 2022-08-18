
from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {author: [books_available_per_author]}
        self.rented_books = {}  # {username: {book_name: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.books_available[author].remove(book_name)
                user.books.append(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user, book_days in self.rented_books.items():
            for book, days in book_days.items():
                if book_name == book:
                    return f'The book "{book_name}" is already rented and will be available in {days} days!'



    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
            return
        return f"{user.username} doesn't have this book in his/her records!"
