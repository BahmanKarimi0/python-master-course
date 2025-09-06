class Library:
    """Class Library"""
    def __init__(self) -> None:
        """Class constructor"""
        self.book_list: list[str] = []

    def add_book(self, title:str) -> None:
        """Add a book"""
        if not isinstance(title, str):
            raise TypeError(f'Expected a string, got {type(title).__name__}')
        if not title:
            raise ValueError(f'Title cannot be empty')
        if title.casefold() in self.book_list:
            raise ValueError(f'Title "{title}" is already in library')
        self.book_list.append(title.casefold())
        print(f'Book "{title.title()}" added to library')

    def remove_book(self, title:str) -> None:
        """Remove a book"""
        if not isinstance(title, str):
            raise TypeError(f'Expected a string, got {type(title).__name__}')
        if title.casefold() in self.book_list:
            self.book_list.remove(title.casefold())
            print(f'Book "{title}" removed successfully')
        else:
            raise ValueError(f'Title "{title}" is not in library')

    def display_books(self):
        """Display books"""
        print()
        print(f'List of books'.center(50, '-'))
        for book in self.book_list:
            print(f'Title: {book.title()}')
        print('-'*50)


if __name__ == '__main__':
    my_book = Library()
    my_book.add_book('Python')
    my_book.add_book('C++')
    my_book.add_book('java')
    my_book.display_books()
    my_book.remove_book('python')
    my_book.display_books()


