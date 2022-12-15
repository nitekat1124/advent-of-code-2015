from itertools import groupby
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        seq = data[0]
        for _ in range(40):
            seq = self.next_seq(seq)

        return len(seq)

    def part2(self, data):
        seq = data[0]
        for _ in range(50):
            seq = self.next_seq(seq)

        return len(seq)

    def next_seq(self, seq):
        next_seq = ""
        for i, g in groupby(seq):
            next_seq += str(len(list(g))) + i
        return next_seq
