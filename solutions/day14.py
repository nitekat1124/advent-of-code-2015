from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        reindeers = self.parse_reindeers(data)
        t = 1000 if len(reindeers) == 2 else 2503
        distances = [
            reindeers[i]["speed"] * (reindeers[i]["fly_time"] * (1 + ((t - reindeers[i]["fly_time"]) // (reindeers[i]["rest_time"] + reindeers[i]["fly_time"]))) + max(((t - reindeers[i]["fly_time"]) % (reindeers[i]["rest_time"] + reindeers[i]["fly_time"])) - reindeers[i]["rest_time"], 0))
            for i in reindeers
        ]
        return max(distances)

    def part2(self, data):
        reindeers = self.parse_reindeers(data)
        t = 1000 if len(reindeers) == 2 else 2503
        scores = [0] * len(reindeers)
        for s in range(1, t + 1):
            distances = [
                reindeers[i]["speed"] * (reindeers[i]["fly_time"] * (1 + ((s - reindeers[i]["fly_time"]) // (reindeers[i]["rest_time"] + reindeers[i]["fly_time"]))) + max(((s - reindeers[i]["fly_time"]) % (reindeers[i]["rest_time"] + reindeers[i]["fly_time"])) - reindeers[i]["rest_time"], 0))
                for i in reindeers
            ]
            max_dist = max(distances)
            max_idx = [i for i, v in enumerate(distances) if v == max_dist]
            for i in max_idx:
                scores[i] += 1

        return max(scores)

    def parse_reindeers(self, data):
        reindeers = {}
        for line in data:
            parts = line.split()
            reindeers[parts[0]] = {"speed": int(parts[3]), "fly_time": int(parts[6]), "rest_time": int(parts[13])}
        return reindeers
