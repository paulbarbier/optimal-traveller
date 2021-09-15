import json
import numpy as np

class city:
    def __init__(self, name, latitude, longitude):      #initializer
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class loader:
    def __init__(self):
        pass

    def load_json(self, file_adress):                   #loads the data from a json file
        f = open(str(file_adress), "r")                 #opens the file
        data = json.load(f)                             #converts it into a string
        f.close()

        city_list = []
        for location in data:                           #for every city we get its name, latitude, longitude
            city_list.append(city(location('capital'), float(location('lat')), float(location('long')))

        self.city_list = np.city_list()                 #eventually we get a tabular with the cities' data
