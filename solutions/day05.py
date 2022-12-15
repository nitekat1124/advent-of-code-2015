from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        apply_rule1 = [i for i in data if sum(1 for c in i if c in "aeiou") > 2]
        apply_rule2 = [i for i in apply_rule1 if sum(1 if c == d else 0 for c, d in zip(i, i[1:])) > 0]
        apply_rule3 = [i for i in apply_rule2 if sum(1 if c + d in ["ab", "cd", "pq", "xy"] else 0 for c, d in zip(i, i[1:])) < 1]
        return len(apply_rule3)

    def part2(self, data):
        apply_rule1 = [i for i in data if sum(1 if i.count(c + d) > 1 else 0 for c, d in zip(i, i[1:])) > 0]
        apply_rule2 = [i for i in apply_rule1 if sum(1 if c == d else 0 for c, d in zip(i, i[2:])) > 0]
        return len(apply_rule2)
