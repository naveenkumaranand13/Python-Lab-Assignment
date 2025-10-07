print("Welcome to daily calorie tracker")
print("Compare your daily calories")
meals = []
calories = []
num_meals = int(input("Enter number of meals: "))
for i in range(num_meals):
    meal_name = input(f"Enter {i+1} meal name: ")
    cal = float(input(f"Enter calories for {i+1} meal: "))
    meals.append(meal_name)
    calories.append(cal)
total_calories = sum(calories)
avg_calories = total_calories / num_meals
daily_limit = float(input("Enter your daily calorie limit: "))
print(f"\nTotal calories: {total_calories}")
print(f"Average calories per meal: {avg_calories}")
if total_calories > daily_limit:
    print("You exceeded your daily calorie limit!")
else:
    print("You are within your daily calorie limit.")