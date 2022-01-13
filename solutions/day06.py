import re
from collections import defaultdict
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
        grid = defaultdict(int)
        for inst in data:
            op, coord1, coord2 = re.findall(r"(.*)\s(\d+\,\d+)\sthrough\s(\d+\,\d+)", inst)[0]

            x1, y1 = map(int, coord1.split(","))
            x2, y2 = map(int, coord2.split(","))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] = [1, 0, 1 - grid[(x, y)]][["turn on", "turn off", "toggle"].index(op)]

        return sum(grid.values())

    def part2(self, data):
        grid = defaultdict(int)
        for inst in data:
            op, coord1, coord2 = re.findall(r"(.*)\s(\d+\,\d+)\sthrough\s(\d+\,\d+)", inst)[0]

            x1, y1 = map(int, coord1.split(","))
            x2, y2 = map(int, coord2.split(","))

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[(x, y)] += [1, -1, 2][["turn on", "turn off", "toggle"].index(op)]
                    grid[(x, y)] = max(grid[(x, y)], 0)

        return sum(grid.values())
