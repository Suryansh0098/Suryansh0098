user_goals = {"calorie_goal": 2000, "weight_goal": 70.0}

def set_goals():
    print("\n--- Set Your Goals ---")
    cals = float(input("Enter daily calorie intake goal: "))
    weight = float(input("Enter target weight (kg): "))
    
    user_goals["calorie_goal"] = cals
    user_goals["weight_goal"] = weight
    print("Success: Goals updated!")

def check_progress(current_calories):
    print("\n--- Goal Progress ---")
    goal = user_goals["calorie_goal"]
    
    print(f"Target Weight: {user_goals['weight_goal']} kg")
    print(f"Calorie Goal: {goal}")
    print(f"Current Intake: {current_calories}")

    if current_calories > goal:
        print("Warning: You have exceeded your daily calorie goal!")
    else:
        remaining = goal - current_calories
        percent = (current_calories / goal) * 100
        print(f"You can still consume {remaining} calories today.")
        print(f"Progress Bar: {percent:.1f}% of daily goal reached.")