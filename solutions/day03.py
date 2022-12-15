from utils.solution_base import SolutionBase


class Solution(SolutionBase):
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
