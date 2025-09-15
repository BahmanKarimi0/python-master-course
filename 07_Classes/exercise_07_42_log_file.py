class LogFile:
    def __init__(self, file_name: str, mode: str ="a") -> None:
        """Initialise the log file"""
        self.file_name = file_name
        self.mode = mode
        self.file: open | None = None

    def __enter__(self) -> open:
        """Open the log file"""
        self.file = open(self.file_name, self.mode)
        self.file.write('--- Log started ---\n')
        return self.file

    def __exit__(self, exc_type: type | None, exc_val: BaseException | None, exc_tb: object | None) -> None:
        """Close the log file"""
        if self.file:
            self.file.write('--- Log ended ---\n')
            self.file.close()


with LogFile("log.txt", 'w') as f:
    f.write("This is a log message.\n")
