import re
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
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
