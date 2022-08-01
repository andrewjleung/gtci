from math import inf


class ArrayReader:
    def __init__(self, nums):
        self.__nums = nums

    def get(self, index):
        if index >= len(self.__nums):
            return inf

        return self.__nums[index]
