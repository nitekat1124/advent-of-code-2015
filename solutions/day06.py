import re
from collections import defaultdict
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
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
