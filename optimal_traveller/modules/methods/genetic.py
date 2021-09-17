import random
random.seed()


class Genetic:
    def __init__(self, percentage, size, steps, w):
        self.percentage = percentage
        self.population = []
        self.size = size
        self.steps = steps
        self.weight_matrix = w

    def fitness(self, path_ind):
        fitness = 0
        for i in range(len(self.population[path_ind])-1):
            fitness += self.weight_matrix[self.population[path_ind][i]][self.population[path_ind][i+1]]
        self.population[path_ind][0] = fitness

    def random_path_generator(self, nodes):
        path = [0]
        path.append(nodes[-1])
        nodes.remove(-1)

        while len(nodes) != 0:
            indice = random.randrange(len(nodes))
            path.append(nodes[indice])
            nodes.remove(indice)

        path.append(path[1])
        self.population.append(path)
        self.fitness(-1)

    # def path_crosser(self, path1, path2, weight):
    #    indice1 = random.randrange(len(self.population[path1]))
    #    indice2 = random.randrange(len(self.population[path2]))
    #    self.population[path1][indice1], self.population[path2][indice2] = self.population[path2][indice2], self.population[path1][indice1]
    #    self.fitness(weight, self.population[path1])
    #    self.fitness(weight, self.population[path2])

    def path_mutation(self, path_ind):
        new_path = self.population[path_ind].copy()

        indice1 = random.randint(2, len(self.population[path_ind])-2)
        indice2 = random.randint(2, len(self.population[path_ind])-2)
        while indice1 == indice2:
            indice2 = random.randrange(2, len(self.population[path_ind])-2)

        new_path[indice1] = self.population[path_ind][indice2]
        new_path[indice2] = self.population[path_ind][indice1]
        self.population.append(new_path)

        self.fitness(-1)

    def give_fitness(self, path_ind):
        return self.population[path_ind][0]

    def sort_population(self):
        self.population.sort(key=self.give_fitness)

    def select_population(self):
        limit = int(self.percentage*len(self.population))
        for i in range(limit):
            self.population.remove(-1)

    def population_generator(self, nodes):
        for i in range(self.size):
            self.random_path_generator(nodes)

    def solve_genetic(self, nodes):
        self.population_generator(nodes)
        self.sort_population()
        self.select_population()
        iteration = 1
        while iteration < self.steps:
            while len(self.population) <= self.size:
                self.path_mutation(self.population[random.randrange(len(self.population))])
            self.sort_population()
            self.select_population()
            iteration += 1
