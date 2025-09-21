import os


class ChangeDirectory:
    """Change the current working directory"""
    def __init__(self, new_path: str) -> None:
        """Initialise the class"""
        self.new_path = new_path
        self.current_dir: None | str = None

    def __enter__(self) -> str:
        """Enter the context manager"""
        self.current_dir = os.getcwd()
        os.chdir(self.new_path)
        return os.getcwd()

    def __exit__(self, exc_type: type | None, exc_val: BaseException | None, exc_tb: object | None) -> None:
        """Exit the context manager"""
        os.chdir(self.current_dir)


with ChangeDirectory(r"c:\\") as new_dir:
    print("Now in:", new_dir)

print("Back to:", os.getcwd())
