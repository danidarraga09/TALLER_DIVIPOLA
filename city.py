from node import Node


class City(Node):

    def __init__(self, id, name, lat, lon):

        super().__init__(id, name)

        self.lat = float(str(lat).replace(',', '.'))
        self.lon = float(str(lon).replace(',', '.'))