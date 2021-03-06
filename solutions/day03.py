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
            if func(i) == int(r[0]):
                print(f"test {test_counter} passed")
            else:
                print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        _map = data[0]
        locations = {(0, 0)}
        santa = (0, 0)
        directions = {
            "^": (0, 1),
            "v": (0, -1),
            "<": (-1, 0),
            ">": (1, 0),
        }
        for d in _map:
            santa = tuple(i + j for i, j in zip(santa, directions[d]))
            locations.add(santa)
        return len(locations)

    def part2(self, data):
        _map = data[0]
        locations = {(0, 0)}
        santas = [(0, 0), (0, 0)]
        directions = {
            "^": (0, 1),
            "v": (0, -1),
            "<": (-1, 0),
            ">": (1, 0),
        }
        for i, d in enumerate(_map):
            santas[i % 2] = tuple(i + j for i, j in zip(santas[i % 2], directions[d]))
            locations.add(santas[i % 2])
        return len(locations)
