from itertools import combinations, product
import math
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
        player, boss, equipments = self.get_game_data(data)
        costs = []
        for equip in equipments:
            player["damage"] = equip[0]["damage"] + equip[1]["damage"] + equip[2][0]["damage"] + equip[2][1]["damage"]
            player["armor"] = equip[0]["armor"] + equip[1]["armor"] + equip[2][0]["armor"] + equip[2][1]["armor"]
            if self.battle(player, boss):
                costs += [equip[0]["cost"] + equip[1]["cost"] + equip[2][0]["cost"] + equip[2][1]["cost"]]
        return min(costs)

    def part2(self, data):
        player, boss, equipments = self.get_game_data(data)
        costs = []
        for equip in equipments:
            player["damage"] = equip[0]["damage"] + equip[1]["damage"] + equip[2][0]["damage"] + equip[2][1]["damage"]
            player["armor"] = equip[0]["armor"] + equip[1]["armor"] + equip[2][0]["armor"] + equip[2][1]["armor"]
            if not self.battle(player, boss):
                costs += [equip[0]["cost"] + equip[1]["cost"] + equip[2][0]["cost"] + equip[2][1]["cost"]]
        return max(costs)

    def get_game_data(self, data):
        player = {
            "hp": 100,
            "damage": 0,
            "armor": 0,
        }
        boss = {
            "hp": int(data[0].split(": ")[1]),
            "damage": int(data[1].split(": ")[1]),
            "armor": int(data[2].split(": ")[1]),
        }
        weapons = {
            "dagger": {"cost": 8, "damage": 4, "armor": 0},
            "shortsword": {"cost": 10, "damage": 5, "armor": 0},
            "warhammer": {"cost": 25, "damage": 6, "armor": 0},
            "longsword": {"cost": 40, "damage": 7, "armor": 0},
            "greataxe": {"cost": 74, "damage": 8, "armor": 0},
        }
        armors = {
            "none": {"cost": 0, "damage": 0, "armor": 0},
            "leather": {"cost": 13, "damage": 0, "armor": 1},
            "chainmail": {"cost": 31, "damage": 0, "armor": 2},
            "splintmail": {"cost": 53, "damage": 0, "armor": 3},
            "bandedmail": {"cost": 75, "damage": 0, "armor": 4},
            "platemail": {"cost": 102, "damage": 0, "armor": 5},
        }
        rings = {
            "none1": {"cost": 0, "damage": 0, "armor": 0},
            "none2": {"cost": 0, "damage": 0, "armor": 0},
            "damage1": {"cost": 25, "damage": 1, "armor": 0},
            "damage2": {"cost": 50, "damage": 2, "armor": 0},
            "damage3": {"cost": 100, "damage": 3, "armor": 0},
            "defense1": {"cost": 20, "damage": 0, "armor": 1},
            "defense2": {"cost": 40, "damage": 0, "armor": 2},
            "defense3": {"cost": 80, "damage": 0, "armor": 3},
        }

        rings_combinations = list(combinations(rings.values(), 2))
        equipments = list(product(weapons.values(), armors.values(), rings_combinations))

        return player, boss, equipments

    def battle(self, player, boss):
        boss_hp = boss["hp"]
        player_hp = player["hp"]
        boss_attack = max(1, boss["damage"] - player["armor"])
        player_attack = max(1, player["damage"] - boss["armor"])
        boss_turns = math.ceil(boss_hp / player_attack)
        player_turns = math.ceil(player_hp / boss_attack)
        return player_turns >= boss_turns
