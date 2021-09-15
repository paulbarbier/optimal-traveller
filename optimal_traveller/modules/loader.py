import json
import numpy as np

class city:
    def __init__(self, name, latitude, longitude):      #initializer
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class loader:
    def __init__(self, city_list):
        self.cities_list = np.array(city_list)

    def load_json(self, file_adress):                   #loads the data from a json file
        f = open(str(file_adress), "r")                 #opens the file
        data = json.load(f)                             #converts it into a string
        print("json data loaded")
        f.close()

        city_list = []
        for location in data:                           #for every city we get its name, latitude, longitude
            city_list.append(city(location['capital'], float(location['lat']), float(location['long'])))
        print("data explored")

        self.cities_list = np.array(city_list)          #eventually we get a tabular with the cities' data
        print("data put into tabular")

def main():
    print("main started")
    test = loader.load_json("~/2A/projet_rentree/optimal-traveller/data/capitals.json")
    print("data loaded")
    print(test.cities_list)
