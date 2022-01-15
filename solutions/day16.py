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
        tests = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split(
            "\n"
        )

        test_data = data
        new_data = []
        for t in tests:
            a, b = t.split(" ")
            for i in test_data:
                if a not in i or t in i:
                    new_data += [i]
            test_data = new_data
            new_data = []
        return test_data

    def part2(self, data):
        tests = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split(
            "\n"
        )

        test_data = data
        new_data = []
        for t in tests:
            a, b = t.split(" ")
            for i in test_data:
                if a not in i:
                    new_data += [i]
                else:
                    if a in ["cats:", "trees:"]:
                        thing = [k for k in i.split(": ", 1)[1].split(", ") if a in k]
                        if len(thing) < 1 or int(thing[0].split(": ")[1]) > int(b):
                            new_data += [i]
                    elif a in ["pomeranians:", "goldfish:"]:
                        thing = [k for k in i.split(": ", 1)[1].split(", ") if a in k]
                        if len(thing) < 1 or int(thing[0].split(": ")[1]) < int(b):
                            new_data += [i]
                    elif t in i:
                        new_data += [i]
            test_data = new_data
            new_data = []
        return test_data
