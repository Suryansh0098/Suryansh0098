# Fitness And Calorie Tracker CLI

A modular Python Command Line Interface (CLI) application designed to help users manage their health goals. The application enables tracking of nutritional intake exercise activities, calorie deficits/surpluses, target goals and historical fitness data persistence via CSV formatting.

## Overview Of The Project

The Fitness And Calorie Tracker provides an easy-to-use command-line environment for everyday health monitoring. By integrating meal intake logging with exercise tracking the system dynamically calculates nutrition, macronutrients and calories burned. Furthermore it measures your real-time performance against targets and saves historic summaries for long-term health tracking.

This project uses Python libraries and modular structure separating business logic for diet tracking, workout logging, target goals and persistent history management into distinct Python modules.

## Features

* Meal And Nutrition Tracking (diet.py):

* Log meals with macro attributes: Calories, Protein (g) Carbs (g) and Fats (g).

* Summarize calorie intake and breakdown of macros for the day.

* Workout Logging (workout.py):

* Track physical exercises by activity type, duration (minutes) and intensity (medium high).

* Automatically calculates burned calories based on intensity multipliers.

* Daily Dashboard (main.py):

* Provides an aggregated view displaying total consumed calories, macro distributions and total calories burned.

* Goal And Target Management (goals.py):

* Customize calorie intake targets and target weight goals (in kg).

* Real-time progress check displaying percentage, remaining calories and limit warnings.

* Persistent Historical Logging (history_logger.py):

* Export and append fitness metrics (date, calories_in, calories_out) into a local CSV file (fitness_history.csv).

*. Inspect stored historical progress directly from the command line.

## Technologies / Tools Used

* Programming Language: Python 3.x

* Standard Libraries:

* csv (for data storage and file I/O operations)

* datetime (for fetching system date timestamps

* Version Control And Repository: Git / GitHub

## Steps To Install And Run The Project

### Prerequisites

Make sure you have Python installed on your system (Python 3.6 or higher is recommended).

### Installation. Execution

1. Clone The Repository:
   

```bash

git clone https://github.com/Suryansh0098/Fitness-and-Calorie-Tracker

cd Fitness-and-Calorie-Tracker

```


2. Verify Project Structure:

Ensure all.py files are in the working directory:

```

├── main.py

├── diet.py

├── workout.py

├── goals.py

└── history_logger.py

```

3. Run The Application:

Execute the entry point file:

```bash

python main.py

```

## Instructions For Testing

To test and verify all features of the application follow this sequence after launching main.py:

1. Option 4: Set Target Goals

* Enter 2000 for goal and 70.0, for weight. Verify success message.

2. Option 1: Log a Meal

* Enter food name (Oatmeal) calories (300) protein (10) carbs (50) fats (5).

3. Option 2: Log a Workout

* Enter exercise (Running) duration (30 minutes) intensity (high). Verify calculated burned calories (360 calories).

4. Option 3: View Daily Dashboard

* Verify that consumed calories and burned calories correctly reflect your entries.

5. Option 5: View Goal Progress

* Check progress percentage. Remaining allowable calories.

6. Option 6: Save Day To History Log

* Save session. Confirm fitness_history.csv is. Updated in your folder directory.

7. Option 7: View History Log

* Verify that todays date and stored values display correctly from the CSV file.

8. Option 8: Exit

* Confirm program exit.
