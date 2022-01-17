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
