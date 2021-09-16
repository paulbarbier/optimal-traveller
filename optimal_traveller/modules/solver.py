class Solver:
    def __init__(self):
        pass

    #####Fonctions auxiliaires_Dijkstra
    def distances_entre(self, W, city1, city2):
        return W[city1][city2]

    def choix_plus_proche_voisin(self, Liste, poids):
        min = 0
        for city in Liste:
            if poids[min] > poids[city]:
                min = city
        return (min)

    def supprime(self, Liste, noeud):
        indice = 0
        for i in range(0, len(noeud)):
            if Liste[i] == noeud:
                indice = i
        del Liste[i]

    def init_poids(self, Noeud_départ, Liste_villes):
        n = len(Liste_villes)
        poids = []
        for i in range(0, n):
            if i == Noeud_départ:
                poids[i] = 0
            else:
                poids[i] = float("inf")
        return poids

    #Fonction presque finale
    def Dijkstra(self, W, Liste_villes, Noeud_départ):
        En_cours = []
        Ordre = []
        poids = init_poids(Noeud_départ, Liste_villes)
        En_cours.append(Noeud_départ)
        while len(En_cours) != 0:
            new_noeud = choix_plus_proche_voisin(En_cours, poids)
            Ordre.append(new_noeud)
            supprime(Liste_villes, new_noeud)
            for city in Liste_villes:
                if poids[city] > poids[new_noeud] + distances_entre(W, city, new_noeud):
                    poids[city] = poids[new_noeud] + distances_entre(W, city, new_noeud)
                    En_cours.append(city)
            supprime(En_cours, new_noeud)
        return Ordre

    #Fonction finale qui ajoute la solution dans data
    def Solver_Dijkstra(self):
        W = data["weight-matrix"]
        Liste = data['cities']
        Ordre = Dijkstra(W, Liste, 0)
        data['solutions'].append({"method": "Dijkstra", "resulting_path": Ordre})
