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
        steps, w, h = (100, 100, 100) if len(data) == 100 else (4, 6, 6)
        _map = [[*i] for i in data]

        for _ in range(steps):
            new_map = [list("." * w) for _ in range(h)]
            for y in range(h):
                for x in range(w):
                    neighbors = [_map[y + a][x + b] for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)] if 0 <= y + a < h and 0 <= x + b < w]
                    if _map[y][x] == "#":
                        new_map[y][x] = [".", "#"][neighbors.count("#") in [2, 3]]
                    else:
                        new_map[y][x] = [".", "#"][neighbors.count("#") == 3]
            _map = new_map

        return sum([i.count("#") for i in _map])

    def part2(self, data):
        steps, w, h = (100, 100, 100) if len(data) == 100 else (5, 6, 6)
        _map = [[*i] for i in data]

        for (y, x) in [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]:
            _map[y][x] = "#"

        for _ in range(steps):
            new_map = [list("." * w) for _ in range(h)]
            for y in range(h):
                for x in range(w):
                    if (y, x) in [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]:
                        new_map[y][x] = "#"
                    else:
                        neighbors = [_map[y + a][x + b] for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)] if 0 <= y + a < h and 0 <= x + b < w]
                        if _map[y][x] == "#":
                            new_map[y][x] = [".", "#"][neighbors.count("#") in [2, 3]]
                        else:
                            new_map[y][x] = [".", "#"][neighbors.count("#") == 3]
            _map = new_map

        return sum([i.count("#") for i in _map])
