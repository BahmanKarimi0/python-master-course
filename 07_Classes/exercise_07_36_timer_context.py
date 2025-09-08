from time import perf_counter


class Timer:
    """A simple context manager that measures elapsed time."""

    def __enter__(self) -> 'Timer':
        """
            Start the timer when entering the context.

            Returns:
                Timer: self instance
        """
        self.start: float = perf_counter()
        return self

    def __exit__(self, exe_type: type | None, exe_value: BaseException | None, traceback: object | None) -> None:
        """
        Stop the timer when exiting the context and print elapsed time.

        Args:
            exc_type (type | None): Exception type if raised.
            exc_value (BaseException | None): Exception instance if raised.
            traceback (object | None): Traceback object if exception occurred.
        """
        self.end: float = perf_counter()
        print(f'Finished in {self.end - self.start:.3f} seconds')

if __name__ == '__main__':
    with Timer():
        for i in range(100000000):
            pass
