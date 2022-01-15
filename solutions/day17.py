from itertools import combinations
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
