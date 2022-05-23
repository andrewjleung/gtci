
class SlidingWindow:
    """
    Time Complexity:  O(N)
    Space Complexity: O(1)
    """

    def __init__(self, arr, size):
        # TODO: verify content of array
        # TODO: verify size of array
        # TODO: verify window size
        self.arr = arr
        self.size = size
        self.window_start = 0
        self.window_sum = 0

    def __iter__(self):
        for i in range(self.size):
            self.window_sum += self.arr[i]

        return self

    def __next__(self):
        if self.window_start == 0:
            self.window_start += 1
            return self.window_sum

        if self.window_start + self.size - 1 >= len(self.arr):
            raise StopIteration

        self.window_sum -= self.arr[self.window_start - 1]
        self.window_sum += self.arr[self.window_start + self.size - 1]
        self.window_start += 1
        return self.window_sum
