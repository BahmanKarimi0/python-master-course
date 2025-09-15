from time import perf_counter


class ExecutionTimer:
    """Context manager for measuring execution time of a code block."""
    def __init__(self, label: str | None = None) -> None:
        """
        Initialize the ExecutionTimer.

        Args:
            label (str | None): Optional label to identify the block.
        """
        self.label = label
        self.start: float | None = None
        self.end: float | None = None

    def __enter__(self) -> 'ExecutionTimer':
        """Record the start time."""
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type: type | None, exc_val: BaseException | None, exc_tb: object | None) -> None:
        """Record the end time and display elapsed seconds."""
        self.end = perf_counter()
        run_time = (self.end - self.start)
        if self.label:
            print(f"[{self.label}] Execution time: {run_time:.3f} seconds")
        else:
            print(f"Execution time: {run_time:.3f} seconds")


with ExecutionTimer('Loop test'):
    for i in range(50000000):
        pass
