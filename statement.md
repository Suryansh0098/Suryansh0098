# Project Statement: Fitness & Calorie Tracker CLI

## Problem Statement

In todays paced world keeping a healthy lifestyle means watching what you eat and how you move every day. Many health apps are too complicated. They need a lot of setup or the internet. People find it hard to find a clear and flexible tool that helps them track the calories they eat watch their fitness numbers set goals for their weight and save their past progress without extra stuff.

## Scope of the Project

The goal of this project is to build a Command-Line Interface (CLI) fitness and calorie tracking system using Python.

- **In-Scope**:

Record each meal with details about the nutrients it has (calories, protein, carbs and fats).

Record workouts by type how long they last and how hard they are. Calculate how many calories are burned automatically.

Show a summary with all the details in one place.

Set and watch personal health and weight goals.

Save and get past fitness summaries locally using CSV files.

- **Out-of-Scope**:

A graphical user interface (GUI) or a website or mobile app.

Connect with fitness devices like smartwatches.

Use a database or support multiple users online.

## Target Users

- **Fitness Beginners**: People who want a text-based tool to see how many calories they eat and how much energy they burn during the day.

- **Students & Developers**: Python learners or people who like to work on small projects. They can see an organized script with file I/O dictionaries, loops and modular imports.

- **CLI Enthusiasts**: People who like to use tools in the terminal instead of heavy software with a graphical interface.

## High-Level Features

1. **Modular Architecture**: parts of the program into different files (`diet.py` `workout.py` `goals.py` `history_logger.py` and `main.py`) so each part has a clear role.

2. **Comprehensive Dietary Tracking**: Record each meal and add up all the calories, proteins, carbs and fats for the day.

3. **Dynamic Workout Computation**: Automatically calculate how many calories are burned based on how long the workout's how hard it is (`low` `medium` `high`).

4. **Goal Progression Monitoring**: Check how many calories are eaten compared to the goals. Show progress with numbers and warnings if the limit is gone past.

5. **Persistent History Logging**: Save a summary with a time stamp into a CSV file (`fitness_history.csv`) to look back on progress, over time.
