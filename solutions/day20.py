from functools import reduce
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
        target = int(data[0]) // 10
        n = 1
        while 1:
            # s = sum(i for i in range(1, n + 1) if n % i == 0) * 10
            s = sum(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))
            if s >= target:
                return n
            n += 1

    def part2(self, data):
        target = int(data[0])
        n = 1
        while 1:
            s = sum(set(reduce(list.__add__, ([i if n // i < 51 else 0, n // i if i < 51 else 0] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))) * 11
            if s >= target:
                return n
            n += 1
