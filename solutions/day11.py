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
                if func(i) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(func(i))
                    print(r[0])
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        c = data[0]
        c = self.next_password(c)

        while not self.valid_password(c):
            c = self.next_password(c)

        return c

    def part2(self, data):
        c = self.part1(data)
        return self.part1([c])

    def next_password(self, password):
        chars = "abcdefghjkmnpqrstuvwxyz"
        password = list(password)[::-1]
        add = 1
        for i in range(len(password)):
            c = password[i]
            idx = chars.index(c) + add
            add = 0
            if idx >= len(chars):
                password[i] = "a"
                add = 1
            else:
                password[i] = chars[idx]
                break
        return "".join(password[::-1])

    def valid_password(self, password):
        chars = "abcdefghijklmnopqrstuvwxyz"
        rule1 = sum(1 for i in range(len(password) - 2) if password[i : i + 3] in chars) > 0
        rule2 = sum(1 for i in password if i in "iol") < 1
        rule3 = sum(len(list(j)) // 2 for i, j in groupby(password)) > 1
        return rule1 and rule2 and rule3
