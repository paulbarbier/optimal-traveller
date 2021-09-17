from optimal_traveller.modules.methods.nearest_neighbors import NearestNeighbors
from optimal_traveller.modules.methods.exact import Exact
from optimal_traveller.modules.methods.genetic import Genetic


class Solver:
    def __init__(self, data, percentage, maxsteps, size):
        self.data = data
        self.percentage = percentage
        self.maxsteps = maxsteps
        self.size = size
        self.resulting_path = []

    def nearest_neighbors_solver(self):
        solver = NearestNeighbors(self.data["weight_matrix"])
        solver.solve()
        self.resulting_path = solver.resulting_path

    def exact_solver(self):
        solver = Exact(self.data["weight_matrix"])
        solver.solve()
        self.resulting_path = solver.resulting_path

    def genetic_solver(self):
        solver = Genetic(self.percentage, self.size, self.maxsteps, self.data["weight_matrix"])
        solver.solve()
        self.resulting_path = solver.resulting_path
