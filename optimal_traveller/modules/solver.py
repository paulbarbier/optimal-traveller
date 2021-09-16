from optimal_traveller.modules.methods.dijkstra import Dijkstra
from optimal_traveller.modules.methods.exact import Exact


class Solver:
    def __init__(self):
        pass

    # Fonction finale qui ajoute la solution dans data
    def Solver_Dijkstra(self):
        W = data["weight-matrix"]
        Liste = data['cities']
        Ordre = Dijkstra(W, Liste, 0)
        data['solutions'].append({"method": "Dijkstra", "resulting_path": Ordre})
