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
        self.window_end = 0

    def __inc_accum_right__(self):
        pass

    def __dec_accum_right__(self):
        pass

    def __inc_accum_left__(self):
        pass

    def __dec_accum_left__(self):
        pass

    def is_at_end(self):
        return self.window_end == len(self.arr)

    def is_at_start(self):
        return self.window_start == 0

    def is_minimum_window(self):
        return self.window_start == self.window_end

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

        self.__inc_accum_right__()
        self.window_end += 1

    def extend_left(self):
        if self.is_at_start():
            raise CannotMoveWindowException(
                "Window is at the leftmost position")

        self.window_start -= 1
        self.__inc_accum_left__()

    def retract_right(self):
        if self.is_minimum_window():
            raise CannotMoveWindowException(
                "Cannot retract an empty window")

        self.window_end -= 1
        self.__dec_accum_right__()

    def retract_left(self):
        if self.is_minimum_window():
            raise CannotMoveWindowException(
                "Cannot retract an empty window")

        self.__dec_accum_left__()
        self.window_start += 1

    def __len__(self):
        return self.window_end - self.window_start


class IntegerSlidingWindow(SlidingWindow):
    def __init__(self, arr):
        # TODO: verify that array is of integers?
        super().__init__(arr)
        self.window_sum = 0

    def __inc_accum_right__(self):
        self.window_sum += self.arr[self.window_end]

    def __dec_accum_right__(self):
        self.window_sum -= self.arr[self.window_end]

    def __inc_accum_left__(self):
        self.window_sum += self.arr[self.window_start]

    def __dec_accum_left__(self):
        self.window_sum -= self.arr[self.window_start]


class FixedIntegerSlidingWindow(IntegerSlidingWindow):
    def __init__(self, arr, size):
        super().__init__(arr)
        self.size = size

    def __iter__(self):
        for i in range(self.size):
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
