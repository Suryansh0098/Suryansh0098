import diet
import workout
import goals
import history_logger
import datetime

def display_menu():
    print("\n" + "="*30)
    print(" FITNESS & CALORIE TRACKER ")
    print("="*30)
    print("1. Log a Meal")
    print("2. Log a Workout")
    print("3. View Daily Dashboard")
    print("4. Set Target Goals")
    print("5. View Goal Progress")
    print("6. Save Day to History Log")
    print("7. View History Log")
    print("8. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            diet.log_meal()
            
        elif choice == '2':
            workout.log_workout()
            
        elif choice == '3':
            print("\n=== Daily Dashboard ===")
            diet.view_nutrition_summary()
            burned = workout.get_total_calories_out()
            print(f"Calories Burned: {burned}")
            
        elif choice == '4':
            goals.set_goals()
            
        elif choice == '5':
            current_cals = diet.get_total_calories_in()
            goals.check_progress(current_cals)
            
        elif choice == '6':
            date_today = str(datetime.date.today())
            cals_in = diet.get_total_calories_in()
            cals_out = workout.get_total_calories_out()
            history_logger.save_summary(date_today, cals_in, cals_out)
            
        elif choice == '7':
            history_logger.view_history()
            
        elif choice == '8':
            print("Exiting Tracker. Have a healthy day!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()