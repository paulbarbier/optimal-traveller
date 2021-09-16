import random
random.seed()


class Heuristic:
    def __init__(self, percentage, steps):
        self.percentage = percentage
        self.steps = steps

    def random_path_generator(self, nodes):
        path = []
        while len(nodes) != 0:
            indice = random.randrange(len(nodes))
            path.append(nodes[indice])
            nodes.remove(indice)
        return path

    def path_mixer(self, path1, path2):
        indice1 = random.randrange(len(path1))
        indice2 = random.randrange(len(path2))
        path1[indice1], path2[indice2] = path2[indice2], path1[indice1]

    def path_changer(self, path):
        indice1 = random.randrange(len(path))
        indice2 = random.randrange(len(path))
        while indice1 == indice2:
            indice2 = random.randrange(len(path))
        path[indice1], path[indice2] = path[indice2], path[indice1]

    
