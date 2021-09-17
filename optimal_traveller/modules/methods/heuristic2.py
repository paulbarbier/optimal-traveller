import random
random.seed()


class Heuristic:
    def __init__(self, percentage):
        self.percentage = percentage
        self.population = []

    def fitness(self, weight, path):
        fitness = 0
        for i in range(len(self.population[path])-1):
            fitness += weight[self.population[path][i]][self.population[path][i+1]]
        self.population[path][0] = fitness

    def random_path_generator(self, nodes, weight):
        path = [0]
        while len(nodes) != 0:
            indice = random.randrange(len(nodes))
            path.append(nodes[indice])
            nodes.remove(indice)
        self.population.append(path)
        self.fitness(weight, self.population[-1])

    def path_mixer(self, path1, path2, weight):
        indice1 = random.randrange(len(self.population[path1]))
        indice2 = random.randrange(len(self.population[path2]))
        self.population[path1][indice1], self.population[path2][indice2] = self.population[path2][indice2], self.population[path1][indice1]
        self.fitness(weight, self.population[path1])
        self.fitness(weight, self.population[path2])

    def path_modifier(self, path, weight):
        indice1 = random.randrange(len(self.population[path]))
        indice2 = random.randrange(len(self.population[path]))
        while indice1 == indice2:
            indice2 = random.randrange(len(self.population[path]))
        self.population[path][indice1], self.population[path][indice2] = self.population[path][indice2], self.population[path][indice1]
        self.fitness(weight, self.population[path])

    def give_fitness(self, path):
        return self.population[path][0]

    def sort_population(self):
        self.population.sort(key=self.give_fitness())

    def select_population(self, percentage):
        limit = int(percentage*len(self.population))
        for i in range(limit):
            self.population.remove(0)

    def population_generator(self, nodes):
        for i in range(20):
            self.random_path_generator(nodes)

    def Heuristic(self, steps, nodes, percentage, weight):
        self.population_generator(nodes)
        self.sort_population()
        self.select_population(percentage)
        iteration = 1
        while iteration < steps:
            
