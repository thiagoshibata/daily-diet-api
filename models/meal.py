from database import db

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  date_meal = db.Column(db.DateTime, nullable=False)
  is_diet = db.Column(db.Boolean, nullable=False)

  def to_dict(self):
    return {"id":self.id, "name":self.name, "description":self.description, "date_meal":self.date_meal, "is_diet":self.is_diet}