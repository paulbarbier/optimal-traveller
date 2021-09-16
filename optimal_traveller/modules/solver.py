from modules.methods.dijkstra import *
from modules.methods.exact import *
from modules.loader import *

class Solver:
    def __init__(self):
        pass

    # Fonction finale qui ajoute la solution dans data

    def solver_dijkstra(self, data):
        W = data["weight_matrix"]
        Liste = data['cities']
        Ordre = Dijkstra(self, W, Liste, 0)
        data['solutions'].append({"method": "Dijkstra", "resulting_path": Ordre})

    def exact_solver(self):
        test = Solver()
        test.exact_method('pyomo_data.txt')
def main():
    test = Loader()
    test.read_json('test.opt')
    set = test.data()
    new = Solver()
    new.solver_dijkstra(set)


main()