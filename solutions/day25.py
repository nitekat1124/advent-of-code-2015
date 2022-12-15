from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        d = data[0].split()
        r = int(d[-3][:-1])
        c = int(d[-1][:-1])

        r1 = (r * (r - 1)) // 2 + 1
        rc = r1 + (((r + 1) + (r + 1 + c - 2)) * (c - 1)) // 2
        # print(rc)

        s = 20151125
        for i in range(rc - 1):
            s = (s * 252533) % 33554393
        return s

    def part2(self, data):
        return "Merry Christmas!"
