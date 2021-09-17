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

        self.loader.change_weight_matrix_diagonal()

        output_filename = basename + ".opt"
        print("Save data to ", output_filename)
        self.loader.write_json(output_filename)
        print("Dataset successfully loaded!")

    def solve(self, filename, method, percentage, maxsteps, size):
        self.loader.read_json(filename)
        solver = Solver(self.loader.data, percentage, maxsteps, size)

        print("Solving the Travelling Salesman Problem with ", method, "method...")
        if method == "exact":
            solver.exact_solver()
        elif method == "nearest-neighbors":
            solver.nearest_neighbors_solver()
        elif method == "genetic":
            solver.genetic_solver()

        self.loader.data["solutions"].append({"method": method, "resulting_path": solver.resulting_path})

        print("Problem successfully solved!")
        self.loader.write_json(filename)
        print("file successfully written to ", filename)

    def display(self, solution):
        self.loader.read_json(solution)
        display = Graphic(self.loader.data)
        display.display()
