from models.base_model import BaseModel
from models.review import Review

class User(BaseModel):
    _users = {}

    def __init__(self, email, password, first_name='', last_name=''):
        super().__init__()
        if email in User._users:
            raise ValueError("Email must be unique")
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        User._users[email] = self

    @classmethod
    def clear_users(cls):
        cls._users.clear()

    def create_review(self, place, content, rating):
        review = Review(user=self, place=place, content=content, rating=rating)
        return review

    def host_place(self, place):
        self.places.append(place)
        place.host = self

    def update(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        self.save()
