from itertools import combinations
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        eggnog = 25 if len(data) == 5 else 150
        containers = [*map(int, data)]
        return len(self.find_combinations(containers, eggnog))

    def part2(self, data):
        eggnog = 25 if len(data) == 5 else 150
        containers = [*map(int, data)]
        combs = self.find_combinations(containers, eggnog)
        min_combs = min(len(i) for i in combs)
        combs = [i for i in combs if len(i) == min_combs]
        return len(combs)

    def find_combinations(self, containers, eggnog):
        combs = []
        for i in range(2, len(containers) + 1):
            combs += list(combinations(containers, i))
        combs = [i for i in combs if sum(i) == eggnog]
        return combs
