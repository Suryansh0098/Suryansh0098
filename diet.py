daily_meals = []

def log_meal():
    print("\n--- Log a Meal ---")
    name = input("Enter food name: ")
    calories = float(input("Enter calories: "))
    protein = float(input("Enter protein (g): "))
    carbs = float(input("Enter carbs (g): "))
    fats = float(input("Enter fats (g): "))

    meal = {
        "name": name, 
        "calories": calories, 
        "protein": protein, 
        "carbs": carbs, 
        "fats": fats
    }
    daily_meals.append(meal)
    print(f"Success: {name} logged successfully!")

def get_total_calories_in():
    total_cal = 0
    for meal in daily_meals:
        total_cal += meal["calories"]
    return total_cal

def view_nutrition_summary():
    total_cal = 0
    total_p = 0
    total_c = 0
    total_f = 0
    
    for meal in daily_meals:
        total_cal += meal["calories"]
        total_p += meal["protein"]
        total_c += meal["carbs"]
        total_f += meal["fats"]
        
    print(f"Calories Consumed: {total_cal}")
    print(f"Macros -> Protein: {total_p}g | Carbs: {total_c}g | Fats: {total_f}g")