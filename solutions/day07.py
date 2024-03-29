from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def part1(self, data):
        insts = [i.split(" -> ") for i in data]
        wires = {}

        while len(insts):
            done = []
            for i in insts:
                parts = i[0].split(" ")
                matched = False
                if len(parts) == 1:
                    if parts[0].isdigit():
                        wires[i[1]] = int(parts[0])
                        matched = True
                    elif parts[0] in wires:
                        wires[i[1]] = wires[parts[0]]
                        matched = True
                elif len(parts) == 2 and parts[0] == "NOT" and parts[1] in wires:
                    wires[i[1]] = int("".join([["0", "1"][d == "0"] for d in bin(wires[parts[1]])[2:].rjust(16, "0")]), 2)
                    matched = True
                elif len(parts) == 3:
                    if parts[1] == "AND" and (parts[0] in wires or parts[0].isdigit()) and (parts[2] in wires or parts[2].isdigit()):
                        wires[i[1]] = (int(parts[0]) if parts[0].isdigit() else wires[parts[0]]) & (int(parts[2]) if parts[2].isdigit() else wires[parts[2]])
                        matched = True
                    elif parts[1] == "OR" and (parts[0] in wires or parts[0].isdigit()) and (parts[2] in wires or parts[2].isdigit()):
                        wires[i[1]] = (int(parts[0]) if parts[0].isdigit() else wires[parts[0]]) | (int(parts[2]) if parts[2].isdigit() else wires[parts[2]])
                        matched = True
                    elif parts[1] == "LSHIFT" and parts[0] in wires and parts[2].isdigit():
                        wires[i[1]] = wires[parts[0]] << int(parts[2])
                        matched = True
                    elif parts[1] == "RSHIFT" and parts[0] in wires and parts[2].isdigit():
                        wires[i[1]] = wires[parts[0]] >> int(parts[2])
                        matched = True
                if matched:
                    done += [i]

            for i in done:
                insts.remove(i)

        return wires["a"]

    def part2(self, data):
        new_b = self.part1(data)
        new_data = [i for i in data if i[-2:] != " b"]
        new_data += [f"{new_b} -> b"]
        return self.part1(new_data)
