import json
import numpy as np


class CITY:
    def __init__(self, name, latitude, longitude):  # initializer
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


class LOADER:
    def __init__(self, city_list):
        self.cities_list = np.array(city_list)

    def load_json(self, file_adress):                   # loads the data from a json file
        f = open(str(file_adress), "r")                 # opens the file
        data = json.load(f)                             # converts it into a string
        f.close()

        city_list = []
        print("entering data exploration")
        for location in data:  # for every city we get its name, latitude, longitude
            city_list.append(CITY(data[location]['capital'], float(data[location]['lat']), float(data[location]['long'])))
        print("data explored")

        self.cities_list = np.array(city_list)  # eventually we get a tabular with the cities' data
        print("data put into tabular")

    def distances(self):
        nb_villes = len(self.cities_list)
        self.W = np.zeros(nb_villes, nb_villes)
        for i in range(0, nb_villes):
            for j in range(0, i):
                self.W[i][j] = np.sqrt((self.cities_list[i].latitude - self.cities_list[j].latitude)*(self.cities_list[i].latitude - self.cities_list[j].latitude) + (self.cities_list[i].longitude - self.cities_list[j].longitude)*(self.cities_list[i].longitude - self.cities_list[j].longitude))
                self.W[j][i] = self.W[i][j]
