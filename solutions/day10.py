from itertools import groupby
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part{part_num}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part{part_num}")
        for i, r in zip(test_inputs, test_results):
            if len(r):
                if func(i) == int(r[0]):
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

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
