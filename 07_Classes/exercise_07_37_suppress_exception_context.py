class SuppressException:
    """A simple context manager that suppresses exceptions."""
    def __enter__(self) -> 'SuppressException':
        """Suppress the exception."""
        print('SuppressException was started successfully.')
        return self

    def __exit__(self, exc_type: type | None, exc_val: BaseException | None, exc_tb: object | None) -> bool:
        """Suppress the exception."""
        print('SuppressException was ended successfully.')
        return True


if __name__ == '__main__':
    with SuppressException():
        print(10 / 0)
        
