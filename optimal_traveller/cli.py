from modules.loader import Loader
from modules.solver import Solver
from modules.graphic import Graphic


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

    def solve(self, filename, method):
        self.loader.read_json(filename)
        #solver = Solver(self.loader.data)

        print("Solving the Travelling Salesman Problem with ", method, "method...")
        if method == "exact":
            pass
        elif method == "nearest-neighbors":
            set = self.loader.data
            new = Solver()
            new.solver_nn(set, 8)
        elif method == "genetic":
            pass

        print("Problem successfully solved!")
        self.loader.data = set
        self.loader.write_json(filename)
        print("file successfully written to ", filename)

    def display(self, solution):
        self.loader.read_json(solution)


test = Cli()
test.solve('modules/test.opt', 'nearest-neighbors')
