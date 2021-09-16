from optimal_traveller.modules.methods.dijkstra import Dijkstra
from optimal_traveller.modules.methods.exact import Exact


class Solver:
    def __init__(self):
        pass

    # Fonction finale qui ajoute la solution dans data

    def solver_dijkstra(self):
        W = data["weight-matrix"]
        Liste = data['cities']
        Ordre = Dijkstra(W, Liste, 0)
        data['solutions'].append({"method": "Dijkstra", "resulting_path": Ordre})

    def exact_solver(self):
        test = Solver()
        test.exact_method('pyomo_data.txt')
