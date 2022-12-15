import re
from itertools import permutations
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        return min(self.calc_possible_distances(data))

    def part2(self, data):
        return max(self.calc_possible_distances(data))

    def calc_possible_distances(self, data):
        locations = set()
        distances = {}

        for line in data:
            loc1, loc2, dist = re.findall(r"(.*?)\sto\s(.*?)\s=\s(\d+)", line)[0]
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
