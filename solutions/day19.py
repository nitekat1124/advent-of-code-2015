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
        replacements = data[:-2]
        molecule = data[-1]
        new_molecules = set()

        for replacement in replacements:
            a, b = replacement.split(" => ")
            for i in range(len(molecule)):
                if molecule[i : i + len(a)] == a:
                    new_molecule = molecule[:i] + b + molecule[i + len(a) :]
                    new_molecules.add(new_molecule)

        return len(new_molecules)

    def part2(self, data):
        molecule = data[-1]
        replacements = {i[1]: i[0] for i in [i.split(" => ") for i in data[:-2]]}
        count = 0

        # matching from the left seems not work, tried from the right and it works
        while molecule != "e":
            matched = []
            for rep in replacements:
                if replacements[rep] == "e" and rep != molecule:
                    continue
                if rep in molecule:
                    matched += [(rep, molecule.rindex(rep))]
            matched = sorted(matched, key=lambda i: i[1])
            right_most = matched[-1][0]

            molecule = replacements[right_most].join(molecule.rsplit(right_most, 1))
            count += 1

        return count
