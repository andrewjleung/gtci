class CannotMoveWindowException(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(self.reason)


class SlidingWindow:
    # CONSTRAINT: all operations on the window must be constant time.

    def __init__(self, arr):
        if len(arr) < 1:
            raise ValueError("Cannot create sliding window over empty array")

        self.arr = arr
        self.window_start = 0
        self.window_end = 1
        self.window_sum = self.arr[self.window_start]

    def is_at_end(self):
        return self.window_end == len(self.arr)

    def is_at_start(self):
        return self.window_start == 0

    def is_minimum_window(self):
        return len(self) == 1

    def slide_right(self):
        self.extend_right()
        self.retract_left()

    def slide_left(self):
        self.extend_left()
        self.retract_right()

    def extend_right(self):
        if self.is_at_end():
            raise CannotMoveWindowException(
                "Window is at the rightmost position")

        self.window_sum += self.arr[self.window_end]
        self.window_end += 1

    def extend_left(self):
        if self.is_at_start():
            raise CannotMoveWindowException(
                "Window is at the leftmost position")

        self.window_start -= 1
        self.window_sum += self.arr[self.window_start]

    def retract_right(self):
        if self.is_minimum_window():
            raise CannotMoveWindowException(
                "Window cannot be smaller than 1 element")

        self.window_end -= 1
        self.window_sum -= self.arr[self.window_end]

    def retract_left(self):
        if self.is_minimum_window():
            raise CannotMoveWindowException(
                "Window cannot be smaller than 1 element")

        self.window_sum -= self.arr[self.window_start]
        self.window_start += 1

    def __len__(self):
        return self.window_end - self.window_start


class FixedSlidingWindow(SlidingWindow):
    def __init__(self, arr, size):
        super().__init__(arr)
        self.size = size

    def __iter__(self):
        for i in range(self.size - 1):
            self.extend_right()

        return self

    def __next__(self):
        if self.is_at_start() and self.is_at_end():
            return self.window_sum

        if self.is_at_end():
            raise StopIteration()

        result = self.window_sum
        self.slide_right()
        return result
