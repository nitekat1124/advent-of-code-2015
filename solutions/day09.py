import re
from itertools import permutations
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
        return min(self.calc_possible_distances(data))

    def part2(self, data):
        return max(self.calc_possible_distances(data))

    def calc_possible_distances(self, data):
        locations = set()
        distances = {}

        for line in data:
            loc1, loc2, dist = re.findall(r"(.*?)\sto\s(.*?)\s=\s(\d+)", line)[0]
            # g.add_edge(loc1, loc2, dist=int(dist))
            # g.add_edge(loc2, loc1, dist=int(dist))
            locations.add(loc1)
            locations.add(loc2)
            distances[(loc1, loc2)] = int(dist)
            distances[(loc2, loc1)] = int(dist)

        possible_routes = list(permutations(locations, len(locations)))

        travel_distances = []
        for route in possible_routes:
            distance = 0
            for i in range(len(route) - 1):
                distance += distances[(route[i], route[i + 1])]
            travel_distances += [distance]
        return travel_distances
