class NearestNeighbors:
    def __init__(self):
        pass

    # Fonctions auxiliaires_Dijkstra
    def choix_plus_proche_voisin(self, w, noeuds_restants, noeud_actuel):
        min = noeuds_restants[0]
        for i in range(1, len(noeuds_restants)):
            if w[noeud_actuel][noeuds_restants[i]] < w[noeud_actuel][min]:
                min = noeuds_restants[i]
        return min

    def supprime(self, liste, noeud):
        indice = 0
        for i in range(0, len(liste)):
            if liste[i] == noeud:
                indice = i
        del liste[indice]

    # Fonction presque finale
    def nearest_neighbour(self, weight, noeuds_restants, noeud_depart):
        nb_villes = len(noeuds_restants)
        solution = [noeud_depart]
        self.supprime(noeuds_restants, noeud_depart)
        while len(solution) < nb_villes:
            new_noeud = self.choix_plus_proche_voisin(weight, noeuds_restants, solution[-1])
            solution.append(new_noeud)
            self.supprime(noeuds_restants, new_noeud)

        for i in range(nb_villes):
            solution[i]+=1
        solution.append(solution[0])
        print(solution)
        return solution
