from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__()
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        self.places.append(place)
