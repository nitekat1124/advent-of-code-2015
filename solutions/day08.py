import re
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
        code_len = 0
        memory_size = 0
        for line in data:
            code_len += len(line)

            decoded = line[1:-1].replace("\\\\", "/").replace('\\"', '"')
            hex_chars = re.findall(r"\\x[0-9a-f]{2}", decoded)
            for i in hex_chars:
                decoded = decoded.replace(i, bytes.fromhex(i[2:]).decode("latin1"), 1)

            memory_size += len(decoded)
        return code_len - memory_size

    def part2(self, data):
        code_len = 0
        new_code_len = 0

        for line in data:
            code_len += len(line)
            new_code = ""
            for c in line:
                if c == "\\":
                    new_code += "\\\\"
                elif c == '"':
                    new_code += '\\"'
                else:
                    new_code += c

            new_code_len += len(new_code) + 2
        return new_code_len - code_len
