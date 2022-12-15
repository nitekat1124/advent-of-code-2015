import math, itertools
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        return sum(sum(a := [*map(int, i.split("x"))]) ** 2 - sum(i * i for i in a) + min([math.prod(i) for i in itertools.combinations(a, 2)]) for i in data)

    def part2(self, data):
        return sum(2 * sum((a := sorted(map(int, i.split("x"))))[:2]) + math.prod(a) for i in data)
