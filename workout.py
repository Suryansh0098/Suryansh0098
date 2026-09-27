daily_workouts = []

def log_workout():
    print("\n--- Log a Workout ---")
    exercise = input("Enter exercise name (e.g., running, weightlifting): ")
    duration = float(input("Enter duration in minutes: "))
    intensity = input("Enter intensity (low/medium/high): ").lower()

    multiplier = 5 
    if intensity == 'medium':
        multiplier = 8
    elif intensity == 'high':
        multiplier = 12

    calories_burned = duration * multiplier

    workout = {
        "exercise": exercise, 
        "duration": duration, 
        "calories_burned": calories_burned
    }
    daily_workouts.append(workout)
    print(f"Success: {exercise} logged! You burned roughly {calories_burned} calories.")

def get_total_calories_out():
    total_burned = 0
    for w in daily_workouts:
        total_burned += w["calories_burned"]
    return total_burned