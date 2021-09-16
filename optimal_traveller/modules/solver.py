from methods.dijkstra import Dijkstra
# from modules.methods.exact import Exact
from loader import Loader

class Solver:
    def __init__(self):
        pass

    # Fonction finale qui ajoute la solution dans data

    def solver_dijkstra(self, data, start_city):
        W = data["weight_matrix"]
        nb_cities = data['settings']['number_cities']
        Liste = [i for i in range(nb_cities)]
        solution = Dijkstra()
        Ordre = solution.Dijkstra(W, Liste, start_city)
        data['solutions'].append({"method": "Dijkstra", "resulting_path": Ordre})

    def exact_solver(self):
        test = Solver()
        test.exact_method('pyomo_data.txt')


def main():
    test = Loader()
    test.read_json('test.opt')
    set = test.data
    new = Solver()
    new.solver_dijkstra(set, 8)


main()
