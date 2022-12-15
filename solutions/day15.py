import math
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        ingredients = list(self.parse_ingredients(data).values())
        choices = list(self.get_permutations_from_sum(len(ingredients), 100))
        return self.get_max_score(ingredients, choices)

    def part2(self, data):
        ingredients = list(self.parse_ingredients(data).values())
        choices = list(self.get_permutations_from_sum(len(ingredients), 100))
        return self.get_max_score(ingredients, choices, 500)

    def parse_ingredients(self, data):
        ingredients = {}
        for line in data:
            parts = line.split(": ")
            name = parts[0]
            ingredients[name] = {}
            parts2 = parts[1].split(", ")
            for part in parts2:
                parts3 = part.split(" ")
                ingredients[name][parts3[0]] = int(parts3[1])

        return ingredients

    def get_permutations_from_sum(self, length, total_sum):
        if length == 1:
            yield (total_sum,)
        else:
            for value in range(total_sum + 1):
                for permutation in self.get_permutations_from_sum(length - 1, total_sum - value):
                    yield (value,) + permutation

    def get_max_score(self, ingredients, choices, max_calories=-1):
        scores = []
        for choice in choices:
            s = [0, 0, 0, 0]
            calories = 0
            for i, n in enumerate(choice):
                s[0] += n * ingredients[i]["capacity"]
                s[1] += n * ingredients[i]["durability"]
                s[2] += n * ingredients[i]["flavor"]
                s[3] += n * ingredients[i]["texture"]
                calories += n * ingredients[i]["calories"]
            s = [max(0, i) for i in s]
            if max_calories in [-1, calories]:
                scores += [math.prod(s)]
        return max(scores)
