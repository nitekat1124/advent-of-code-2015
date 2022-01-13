import hashlib
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
        key = data[0]
        return self.find_num(key, 5)

    def part2(self, data):
        key = data[0]
        return self.find_num(key, 6)

    def find_num(self, key, digits):
        i = 1
        while True:
            if hashlib.md5((key + str(i)).encode()).hexdigest().startswith("0" * digits):
                return i
            i += 1
