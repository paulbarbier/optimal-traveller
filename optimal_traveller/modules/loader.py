class loader:
    def __init__(self):
        pass

import numpy as np

def distances(list):
    nb_villes = len(list)
    W = np.zeros(nb_villes, nb_villes)
    for i in range(0, nb_villes):
        for j in range(0, i):
            if i != j:
                W[i][j] = np.sqrt((list[i].latitude - list[j].latitude)*(list[i].latitude - list[j].latitude) + (list[i].longitude - list[j].longitude)*(list[i].longitude - list[j].longitude))
                W[j][i] = np.sqrt((list[i].latitude - list[j].latitude)*(list[i].latitude - list[j].latitude) + (
                        list[i].longitude - list[j].longitude)*(list[i].longitude - list[j].longitude))
    return W
