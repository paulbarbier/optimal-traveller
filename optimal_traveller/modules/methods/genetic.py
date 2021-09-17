import random
random.seed()


class Genetic:
    def __init__(self, percentage, size, steps, weight_matrix):
        self.percentage = percentage
        self.population = []
        self.size = size
        self.steps = steps
        self.weight_matrix = weight_matrix
        self.number_cities = len(weight_matrix)
        self.resulting_path = []

    def fitness(self, path_ind):
        fitness = 0
        for i in range(1, len(self.population[path_ind])-1):
            fitness += self.weight_matrix[self.population[path_ind][i]-1][self.population[path_ind][i+1]-1]
        self.population[path_ind][0] = fitness

    def random_path_generator(self, nodes):
        path = [0]
        path.append(nodes.pop())

        while len(nodes) != 0:
            indice = random.randrange(len(nodes))
            path.append(nodes.pop(indice))

        path.append(path[1])
        self.population.append(path)
        self.fitness(len(self.population)-1)

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
        for i in range(1,len(self.population)):
            ind = i
            while ind > 0 and self.population[ind][0] < self.population[ind-1][0]:
                self.population[ind], self.population[ind-1] = self.population[ind-1], self.population[ind]
                ind -= 1

    def select_population(self):
        limit = int((1-self.percentage)*len(self.population))
        for i in range(limit):
            self.population.pop(-1)

    def population_generator(self, nodes):
        for i in range(self.size):
            self.random_path_generator(nodes.copy())

    def solve(self):
        nodes = [i for i in range(self.number_cities)]
        self.population_generator(nodes.copy())
        self.sort_population()
        self.select_population()
        iteration = 1
        while iteration < self.steps:
            while len(self.population) <= self.size:
                self.path_mutation(random.randrange(len(self.population)))
            self.sort_population()
            self.select_population()
            iteration += 1
        self.resulting_path = self.population[0][1:]
