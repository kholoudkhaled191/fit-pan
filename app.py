# from flask import Flask, render_template, request, jsonify
# import random

# app = Flask(__name__)

# # Fake database
# users_meal_plans = {}

# # Sample food items
# breakfast_options = ["Oatmeal with fruits", "Scrambled eggs with toast", "Greek yogurt with honey"]
# lunch_options = ["Grilled chicken salad", "Quinoa bowl with veggies", "Brown rice with fish"]
# dinner_options = ["Grilled salmon with veggies", "Chicken stir fry", "Lentil soup with bread"]

# def generate_meal_plan(calories):
#     # Simple logic: split calories between 3 meals
#     breakfast_cal = int(calories * 0.25)
#     lunch_cal = int(calories * 0.4)
#     dinner_cal = int(calories * 0.35)

#     plan = {
#         "breakfast": {"item": random.choice(breakfast_options), "calories": breakfast_cal},
#         "lunch": {"item": random.choice(lunch_options), "calories": lunch_cal},
#         "dinner": {"item": random.choice(dinner_options), "calories": dinner_cal}
#     }
#     return plan

# @app.route('/')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     data = request.json
#     user_id = data.get("user_id")
#     calories = int(data.get("calories"))

#     plan = generate_meal_plan(calories)
    
#     # Save in fake database
#     if user_id not in users_meal_plans:
#         users_meal_plans[user_id] = []
#     users_meal_plans[user_id].append(plan)

#     return jsonify(plan)

# @app.route('/history/<user_id>')
# def history(user_id):
#     return jsonify(users_meal_plans.get(user_id, []))

# if __name__ == "__main__":
#     app.run(debug=True)
