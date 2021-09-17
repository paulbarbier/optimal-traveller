import random


class NearestNeighbors:
    def __init__(self, data):
        self.weight_matrix = data["weight_matrix"]
        self.number_cities = data["settings"]["number_cities"]
        self.remaining_cities = [i for i in range(self.number_cities)]
        self.number_remaining_cities = self.number_cities
        self.resulting_path = []

    def get_nearest_neighbour(self):
        minimum = self.remaining_cities[0]
        for i in range(1, len(self.remaining_cities)):
            if self.weight_matrix[self.resulting_path[-1]][self.remaining_cities[i]] < \
                    self.weight_matrix[self.resulting_path[-1]][minimum]:
                minimum = self.remaining_cities[i]
        return minimum

    def delete_node(self, node):
        index = 0
        for i in range(len(self.remaining_cities)):
            if self.remaining_cities[i] == node:
                index = i
                break
        del self.remaining_cities[index]
        self.number_remaining_cities -= 1

    def solve(self):
        random_start_node = random.choice(self.remaining_cities)
        self.resulting_path.append(random_start_node)
        self.delete_node(random_start_node)
        while len(self.resulting_path) < self.number_remaining_cities:
            new_node = self.get_nearest_neighbour()
            self.resulting_path.append(new_node)
            self.delete_node(new_node)

        for city in self.resulting_path:
            city += 1
        self.resulting_path.append(self.resulting_path[0])
