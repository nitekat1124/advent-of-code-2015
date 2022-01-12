import math, itertools
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
            if func(i) == int(r[0]):
                print(f"test {test_counter} passed")
            else:
                print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        return sum(sum(a := [*map(int, i.split("x"))]) ** 2 - sum(i * i for i in a) + min([math.prod(i) for i in itertools.combinations(a, 2)]) for i in data)

    def part2(self, data):
        return sum(2 * sum((a := sorted(map(int, i.split("x"))))[:2]) + math.prod(a) for i in data)
