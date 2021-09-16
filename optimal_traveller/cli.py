from optimal_traveller.modules.loader import Loader
from optimal_traveller.modules.solver import Solver
from optimal_traveller.modules.graphic import Graphic


class Cli:
    def __init__(self):
        self.loader = Loader()

    def load(self, filename, metric):
        basename, extension = filename.split(".")

        if extension == "json":
            self.loader.load_json(filename)
            print("Loading ", filename, "...")
        elif extension == "txt":
            self.loader.load_txt(filename)

        if metric == "euclidean":
            print("Compute euclidean distances")
            self.loader.compute_euclidean_distances()
        elif metric == "orthodromic":
            print("Compute orthodromic distances")
            self.loader.compute_orthodromic_distances()

        output_filename = basename + ".opt"
        print("Save data to ", output_filename)
        self.loader.write_json(output_filename)
        print("Dataset successfully loaded!")

    def solve(self, graph, method):
        print("solve")

    def display(self, solution):
        print("display")

