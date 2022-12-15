from copy import deepcopy
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        player, boss = self.get_game_data(data)
        self.costs = None
        self.play(player, boss, {}, 0, True)
        return self.costs

    def part2(self, data):
        player, boss = self.get_game_data(data)
        self.costs = None
        self.play(player, boss, {}, 0, True, True)
        return self.costs

    def get_game_data(self, data):
        player = {
            "hp": 50,
            "armor": 0,
            "mana": 500,
        }
        boss = {
            "hp": int(data[0].split(": ")[1]),
            "damage": int(data[1].split(": ")[1]),
        }
        self.spells = {
            "missile": {"cost": 53, "damage": 4, "armor": 0, "heal_hp": 0, "heal_mana": 0, "turns": 0},
            "drain": {"cost": 73, "damage": 2, "armor": 0, "heal_hp": 2, "heal_mana": 0, "turns": 0},
            "shield": {"cost": 113, "damage": 0, "armor": 7, "heal_hp": 0, "heal_mana": 0, "turns": 6},
            "poison": {"cost": 173, "damage": 3, "armor": 0, "heal_hp": 0, "heal_mana": 0, "turns": 6},
            "recharge": {"cost": 229, "damage": 0, "armor": 0, "heal_hp": 0, "heal_mana": 101, "turns": 5},
        }
        return player, boss

    def play(self, player, boss, active_spells, spent_mana, player_turn=True, part2=False):
        active_spells_this_turn = deepcopy(active_spells)
        player_this_turn = deepcopy(player)
        boss_this_turn = deepcopy(boss)

        if player_turn and part2:
            player_this_turn["hp"] -= 1
            if player_this_turn["hp"] <= 0:
                return False

        for spell in active_spells_this_turn:
            player_this_turn["mana"] += active_spells_this_turn[spell]["heal_mana"]
            player_this_turn["hp"] += active_spells_this_turn[spell]["heal_hp"]
            boss_this_turn["hp"] -= active_spells_this_turn[spell]["damage"]
            active_spells_this_turn[spell]["turns"] -= 1

        active_spells2_keys = list(active_spells_this_turn.keys())
        for spell in active_spells2_keys:
            if active_spells_this_turn[spell]["turns"] <= 0:
                player_this_turn["armor"] -= active_spells_this_turn[spell]["armor"]
                del active_spells_this_turn[spell]

        if boss_this_turn["hp"] <= 0:
            if self.costs is None or spent_mana < self.costs:
                self.costs = spent_mana
            return True

        if self.costs is not None and spent_mana >= self.costs:
            return False

        if player_turn:
            for spell in self.spells:
                if spell in active_spells_this_turn:
                    continue
                else:
                    if self.spells[spell]["cost"] <= player_this_turn["mana"]:
                        active_spells_next_turn = deepcopy(active_spells_this_turn)
                        player_next_turn = deepcopy(player_this_turn)

                        player_next_turn["mana"] -= self.spells[spell]["cost"]
                        player_next_turn["armor"] += self.spells[spell]["armor"]
                        active_spells_next_turn[spell] = {
                            "damage": self.spells[spell]["damage"],
                            "armor": self.spells[spell]["armor"],
                            "heal_hp": self.spells[spell]["heal_hp"],
                            "heal_mana": self.spells[spell]["heal_mana"],
                            "turns": self.spells[spell]["turns"],
                        }
                        self.play(player_next_turn, boss_this_turn, active_spells_next_turn, spent_mana + self.spells[spell]["cost"], False, part2)
        else:
            player_this_turn["hp"] -= max(1, boss_this_turn["damage"] - player_this_turn["armor"])
            if player_this_turn["hp"] > 0:
                self.play(player_this_turn, boss_this_turn, active_spells_this_turn, spent_mana, True, part2)
