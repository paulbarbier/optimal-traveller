import folium
import os

class Graphic:
    def __init__(self, data):
        self.cities = data["cities"]
        self.solutions = data["solutions"]
        self.longitude_center = float
        self.latitude_center = float
        self.filename = data["settings"]["filename"]

    def compute_center(self):
        latitudes = []
        longitudes = []
        for city in self.cities:
            latitudes.append(city["latitude"])
            longitudes.append(city["longitude"])
        self.longitude_center = (max(longitudes) + min(longitudes)) / 2
        self.latitude_center = (max(latitudes) + min(latitudes)) / 2

    def coordinates_from_id(self, index):
        for city in self.cities:
            if city['id'] == index:
                return [city["latitude"], city["longitude"]]

    def display(self):
        self.compute_center()

        for solution in self.solutions:
            path = [[]]

            for city in solution["resulting_path"]:
                path[0].append(self.coordinates_from_id(city))
            path[0].append(self.coordinates_from_id(solution["resulting_path"][0]))

            usa = folium.Map(location=[self.latitude_center, self.longitude_center], zoom_start=5)
            for city in self.cities:
                folium.Marker(location=[city["latitude"], city["longitude"]], popup=city["name"]).add_to(usa)
            folium.PolyLine(path, color='red').add_to(usa)
            display_filename = self.filename + "_" + solution["method"] + ".html"
            usa.save(display_filename)
            os.system("open " + display_filename)
