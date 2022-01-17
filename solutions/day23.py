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
        r = self.exec({"a": 0, "b": 0}, data)
        return r["b"]

    def part2(self, data):
        r = self.exec({"a": 1, "b": 0}, data)
        return r["b"]

    def exec(self, r, data):
        idx = 0
        while idx in range(len(data)):
            offset = 1
            inst, inst_data = data[idx].split(" ", 1)
            if inst == "hlf":
                r[inst_data] = r[inst_data] // 2
            elif inst == "tpl":
                r[inst_data] = r[inst_data] * 3
            elif inst == "inc":
                r[inst_data] += 1
            elif inst == "jmp":
                offset = int(inst_data)
            elif inst == "jie":
                p, o = inst_data.split(", ")
                if r[p] % 2 == 0:
                    offset = int(o)
            elif inst == "jio":
                p, o = inst_data.split(", ")
                if r[p] == 1:
                    offset = int(o)
            idx += offset
        return r
