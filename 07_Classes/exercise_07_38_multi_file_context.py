class MultiFileManager:
    """A simple context manager for handling multiple files at once."""

    def __init__(self, file_name_list: list[str], mode: str) -> None:
        """
            Initialize FileManager with a file name and mode.

            Args:
                file_name_list (list): The name of the file to open.
                mode (str): The mode in which to open the file ('r', 'w', 'a', etc.).
        """
        self.file_name_list = file_name_list
        self.mode = mode
        self.file = None
        self.file_list = []

    def __enter__(self) -> list[open]:
        """
            Enter the runtime context and open the file.

            Returns:
                open: The opened file object.
        """
        for file_name in self.file_name_list:
            self.file = open(file_name, self.mode)
            self.file_list.append(self.file)
        return self.file_list

    def __exit__(self, exc_type: type | None, exc_val: BaseException | None, exc_tb: type | None) -> None:
        """
            Exit the runtime context and close the file.

            Args:
                exc_type (type | None): The type of the exception.
                exc_val (BaseException | None): The exception instance.
                exc_tb (object | None): Traceback object.
        """
        if self.file_name_list:
            for file_name in self.file_list:
                file_name.close()


if __name__ == '__main__':
    with MultiFileManager(['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt'], mode='w') as file_list:
        for file_name in file_list:
            file_name.write('hello world')
