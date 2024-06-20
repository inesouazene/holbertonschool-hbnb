from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user, place, content, rating):
        super().__init__()
        self.user = user
        self.place = place
        self.content = content
        self.rating = rating

    def edit_review(self, new_content, new_rating):
        self.content = new_content
        self.rating = new_rating
        self.save()
