import hashlib
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        key = data[0]
        return self.find_num(key, 5)

    def part2(self, data):
        key = data[0]
        return self.find_num(key, 6)

    def find_num(self, key, digits):
        i = 1
        while True:
            if hashlib.md5((key + str(i)).encode()).hexdigest().startswith("0" * digits):
                return i
            i += 1
