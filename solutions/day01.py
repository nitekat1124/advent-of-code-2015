from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        return sum(1 if i == "(" else -1 for i in data[0])

    def part2(self, data):
        insts = [1 if i == "(" else -1 for i in data[0]]
        for i in range(1, len(insts) + 1):
            if sum(insts[:i]) == -1:
                return i
