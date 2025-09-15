class AppendFile:
    """
    A simple context manager that appends content to a file.

    This context manager allows writing content inside a file,
    and after exiting the context, appends a predefined string
    to the same file.

    Example:
        with AppendFile("test.txt", "---\n") as f:
            f.write("Line 1\n")
            f.write("Line 2\n")
    """
    def __init__(self, file_name, string):
        """
            Initialize append string to file.

            Args:
                file_name (str): The name of the file to open.
                string (str): The txt that will be appended to the file.
        """
        self.file_name = file_name
        self.string = string
        self.file = None

    def __enter__(self) -> open:
        """
            Enter the runtime context and open the file.

            Returns:
                open: The opened file object.
        """
        self.file = open(self.file_name, 'a')
        return self.file

    def __exit__(self, exc_type: type | None, exc_val: BaseException | None, exc_tb: object | None) -> None:
        """
            Exit the runtime context and close the file.

            Args:
                exc_type (type | None): The type of the exception.
                exc_val (BaseException | None): The exception instance.
                exc_tb (object | None): Traceback object.
        """
        self.file.write(self.string)
        self.file.close()


if __name__ == '__main__':
    with AppendFile('test.txt', f'{"*" * 40}\n') as f:
        f.write('First line\n')
        f.write('Second line\n')
        f.write('Third line\n')
