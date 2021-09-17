from optimal_traveller.modules.methods.nearest_neighbors import NearestNeighbors
from optimal_traveller.modules.methods.exact import Exact
from optimal_traveller.modules.methods.genetic import Genetic


class Solver:
    def __init__(self, data):
        self.data = data
        self.resulting_path = []

    def nearest_neighbors_solver(self):
        solver = NearestNeighbors(self.data)
        solver.solve()
        self.resulting_path = solver.resulting_path

    def exact_solver(self, data):
        W = data["weight_matrix"]
        nb_cities = data['settings']['number_cities']
        build = Exact()
        solution = build.exact_method(W, nb_cities)
        print(solution)
        data['solutions'].append({"method": "Exact Method", "resulting_path": solution})

    def genetic(self):
        pass
