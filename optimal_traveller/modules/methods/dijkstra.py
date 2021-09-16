class Dijkstra:
    def __init__(self):
        pass

    # Fonctions auxiliaires_Dijkstra
    def choix_plus_proche_voisin(self, W, noeuds_restants, noeud_actuel):
        min = noeuds_restants[0]
        for i in range(1, len(noeuds_restants)):
            if W[noeud_actuel][noeuds_restants[i]] < W[noeud_actuel][min]:
                min = noeuds_restants[i]
        return min

    def supprime(self, Liste, noeud):
        indice = 0
        for i in range(0, len(Liste)):
            if Liste[i] == noeud:
                indice = i
        del Liste[indice]

    # Fonction presque finale
    def Dijkstra(self, W, Noeuds_restants, Noeud_depart):
        nb_villes = len(Noeuds_restants)
        Ordre = [Noeud_depart]
        self.supprime(Noeuds_restants, Noeud_depart)
        while len(Ordre) < nb_villes:
            new_noeud = self.choix_plus_proche_voisin(W, Noeuds_restants, Ordre[-1])
            Ordre.append(new_noeud)
            self.supprime(Noeuds_restants, new_noeud)

        for i in range(nb_villes):
            Ordre[i]+=1
        Ordre.append(Ordre[0])
        print(Ordre)
        return Ordre
