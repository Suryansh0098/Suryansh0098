import csv

def save_summary(date, calories_in, calories_out):

    with open('fitness_history.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, calories_in, calories_out])
    print("\nSuccess: Today's data saved to history!")

def view_history():
    print("\n--- Historical Log ---")
    try:
        with open('fitness_history.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]} | Calories In: {row[1]} | Calories Burned: {row[2]}")
    except FileNotFoundError:
        print("No history found yet. Save a summary first!")