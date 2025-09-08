class FileManager:
    """A simple context manager for handling file operations."""

    def __init__(self, file_name: str, mode: str) -> None:
        """
            Initialize FileManager with a file name and mode.

            Args:
                file_name (str): The name of the file to open.
                mode (str): The mode in which to open the file ('r', 'w', 'a', etc.).
        """
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> open:
        """
            Enter the runtime context and open the file.

            Returns:
                open: The opened file object.
        """
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exe_type, exe_value, traceback) -> None:
        """
            Exit the runtime context and close the file.

            Args:
                exc_type (type | None): The type of the exception.
                exc_value (BaseException | None): The exception instance.
                traceback (object | None): Traceback object.
        """
        if self.file:
            self.file.close()


if __name__ == '__main__':
    with FileManager('text.txt', 'w') as f:
        f.write('Hello World')
