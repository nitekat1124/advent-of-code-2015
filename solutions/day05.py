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
        apply_rule1 = [i for i in data if sum(1 for c in i if c in "aeiou") > 2]
        apply_rule2 = [i for i in apply_rule1 if sum(1 if c == d else 0 for c, d in zip(i, i[1:])) > 0]
        apply_rule3 = [i for i in apply_rule2 if sum(1 if c + d in ["ab", "cd", "pq", "xy"] else 0 for c, d in zip(i, i[1:])) < 1]
        return len(apply_rule3)

    def part2(self, data):
        apply_rule1 = [i for i in data if sum(1 if i.count(c + d) > 1 else 0 for c, d in zip(i, i[1:])) > 0]
        apply_rule2 = [i for i in apply_rule1 if sum(1 if c == d else 0 for c, d in zip(i, i[2:])) > 0]
        return len(apply_rule2)
