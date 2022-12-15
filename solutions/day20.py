from functools import reduce
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        target = int(data[0]) // 10
        n = 1
        while 1:
            # s = sum(i for i in range(1, n + 1) if n % i == 0) * 10
            s = sum(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
            if s >= target:
                return n
            n += 1

    def part2(self, data):
        target = int(data[0])
        n = 1
        while 1:
            s = sum(set(reduce(list.__add__, ([i if n // i < 51 else 0, n // i if i < 51 else 0] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) * 11
            if s >= target:
                return n
            n += 1
