from flask import Flask, request, jsonify
from models.meal import Meal
from database import db


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet-api'

db.init_app(app)

@app.route('/meals', methods=['GET'])
def read_all_meals():
  meals = Meal.query.all()
  response = []
  
  for meal in meals: response.append(meal.to_dict())
  print(meals)
  return jsonify(response)

@app.route('/meal/<int:id_meal>', methods=['GET'])
def read_meal(id_meal):
  meal = Meal.query.get(id_meal)
  if meal:
    return jsonify(meal.to_dict())
  
  else:
    return jsonify({"message":"Refeição não encontrada"}), 404

@app.route('/meal', methods=['POST'])
def create_meal():
  
  data = request.json

  name = data.get("name")
  description = data.get("description")
  date_meal = data.get("date_meal")
  is_diet = data.get("is_diet")



  if name and description and date_meal:
    meal = Meal(name=name, description=description, date_meal=date_meal, is_diet=is_diet)
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message":"Dieta criada com sucesso!"})
  else:
    return jsonify({"message":"Não foi possível adicionar a refeição. Por favor preencha todos os campos"}), 400


@app.route('/hello-world/<name>', methods=['GET'])
def hello_world(name):
  return jsonify({ "message":f"Bem vindo, {name}"})

if __name__ == '__main__':
  app.run(debug=True)