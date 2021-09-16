import json
from math import sqrt


class Loader:
    def __init__(self):
        self.data = {}

    def load_txt(self, filename):
        pass

    def load_json(self, filename, metric):
        with open(filename) as json_file:
            input_json = json.load(json_file)

            self.data = {"settings": {"metric": metric,
                                      "filename": filename,
                                      "number_cities": 0},
                         "cities": [],
                         "weight_matrix": [],
                         "solutions": []}

            i = 1
            for location in input_json:
                self.data["cities"].append({"id": i,
                                            "name": input_json[location]['capital'],
                                            "latitude": float(input_json[location]['lat']),
                                            "longitude": float(input_json[location]['long'])})
                i += 1

            self.data["settings"]["number_cities"] = i-1

            self.data["weight_matrix"] = [[0 for k in range(i-1)] for l in range(i-1)]

    def read_json(self, filename):
        with open(filename, "r") as json_file:
            self.data = json.load(json_file)

    def write_json(self, filename):
        with open(filename, "w") as json_file:
            json_file.truncate(0)
            json.dump(self.data, json_file)

    def compute_euclidean_distances(self):
        row_number = 0
        for city_row in self.data["cities"]:
            column_number = 0
            for city_column in self.data["cities"][:row_number]:
                self.data["weight_matrix"][row_number][column_number] = sqrt((city_row["latitude"] - city_column["latitude"])**2 + (city_row["longitude"] - city_column["longitude"])**2)
                self.data["weight_matrix"][column_number][row_number] = self.data["weight_matrix"][row_number][column_number]
                column_number += 1
            row_number += 1
