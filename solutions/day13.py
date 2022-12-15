from itertools import permutations
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        guest = self.parse_guest(data)
        return self.calc_max_happiness(guest)

    def part2(self, data):
        guest = self.parse_guest(data)

        me = {}
        for i in guest:
            guest[i]["me"] = 0
            me[i] = 0
        guest["me"] = me

        return self.calc_max_happiness(guest)

    def parse_guest(self, data):
        guest = {}
        for line in data:
            parts = line.split()
            happy = [-1, 1][parts[2] == "gain"] * int(parts[3])
            if parts[0] not in guest:
                guest[parts[0]] = {}
            guest[parts[0]][parts[10][:-1]] = happy
        return guest

    def calc_max_happiness(self, guest):
        guest_len = len(guest)
        arrangements = list(permutations(guest.keys()))
        total_changed = []
        for arrangement in arrangements:
            changed = sum(guest[v][arrangement[(i + 1) % guest_len]] + guest[v][arrangement[i - 1]] for i, v in enumerate(arrangement))
            total_changed += [changed]
        return max(total_changed)
