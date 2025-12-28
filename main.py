from profiles import *
from workouts import *
from nutrition import *
from metrics import *
from storage import *


def main():
    users, workouts, meals, metrics_list = load_state("data")
    current_user = None

    while True:
        if current_user is None:
            print("\n--- MAIN MENU ---")
            print("1 - Register user")
            print("2 - Login")
            print("3 - Exit")

            choice = input("Choice: ")

            match choice:
                case "1":
                    email = input("Email: ")
                    pin = input("PIN: ")

                    profile = {
                        "email": email,
                        "pin": pin
                    }

                    if register_user(users, profile):
                        print("User registered successfully.")
                    else:
                        print("This email already exists.")

                case "2":
                    email = input("Email: ")
                    pin = input("PIN: ")

                    user = authenticate_user(users, email, pin)
                    if user:
                        current_user = user
                        print("Login successful.")
                    else:
                        print("Invalid credentials.")

                case "3":
                    print("Saving data...")
                    save_state("data", users, workouts, meals, metrics_list)
                    print("Program exited.")
                    break

                case _:
                    print("Invalid choice.")

        else:
            # DASHBOARD (Task 5)
            print("\n--- DASHBOARD ---")
            print("Total workouts:", len(workouts))
            print("Total meals:", len(meals))
            print("Total metrics:", len(metrics_list))

            if len(workouts) == 0:
                print("Reminder: No workouts logged yet.")

            print(f"\n--- USER MENU ({current_user['email']}) ---")
            print("1 - Add workout")
            print("2 - Update workout")
            print("3 - Delete workout")
            print("4 - Add meal")
            print("5 - Update meal")
            print("6 - Delete meal")
            print("7 - Add metric")
            print("8 - Logout")
            print("9 - Help")

            choice = input("Choice: ")

            match choice:

                # ADD WORKOUT
                case "1":
                    wid = input("Workout id: ")

                    exists = False
                    for w in workouts:
                        if w["id"] == wid:
                            exists = True
                    if exists:
                        print("Workout with this id already exists.")
                        continue

                    date = input("Date (YYYY-MM-DD): ")
                    if len(date) != 10 or date[4] != "-" or date[7] != "-":
                        print("Invalid date format.")
                        continue
                    if date > "2025-01-01":
                        print("Future dates are not allowed.")
                        continue

                    duration = int(input("Duration (minutes): "))
                    if duration <= 0:
                        print("Duration must be positive.")
                        continue

                    workout = {
                        "id": wid,
                        "user_id": current_user["email"],
                        "date": date,
                        "duration": duration,
                        "exercises": []
                    }

                    log_workout(workouts, workout)
                    print("Workout added.")

                # UPDATE WORKOUT
                case "2":
                    wid = input("Workout id to update: ")
                    new_duration = int(input("New duration: "))
                    if new_duration <= 0:
                        print("Duration must be positive.")
                        continue

                    updates = {"duration": new_duration}

                    if update_workout(workouts, wid, updates):
                        print("Workout updated.")
                    else:
                        print("Workout not found.")

                # DELETE WORKOUT
                case "3":
                    wid = input("Workout id to delete: ")
                    confirm = input("Are you sure? (y/n): ")

                    if confirm == "y":
                        if delete_workout(workouts, wid):
                            print("Workout deleted.")
                        else:
                            print("Workout not found.")
                    else:
                        print("Delete cancelled.")

                # ADD MEAL
                case "4":
                    mid = input("Meal id: ")

                    exists = False
                    for m in meals:
                        if m["id"] == mid:
                            exists = True
                    if exists:
                        print("Meal with this id already exists.")
                        continue

                    date = input("Date (YYYY-MM-DD): ")
                    if len(date) != 10 or date[4] != "-" or date[7] != "-":
                        print("Invalid date format.")
                        continue

                    calories = int(input("Calories: "))
                    if calories <= 0:
                        print("Calories must be positive.")
                        continue

                    meal = {
                        "id": mid,
                        "user_id": current_user["email"],
                        "date": date,
                        "calories": calories
                    }

                    log_meal(meals, meal)
                    print("Meal added.")

                # UPDATE MEAL
                case "5":
                    mid = input("Meal id to update: ")
                    new_calories = int(input("New calories: "))
                    if new_calories <= 0:
                        print("Calories must be positive.")
                        continue

                    updates = {"calories": new_calories}

                    if update_meal(meals, mid, updates):
                        print("Meal updated.")
                    else:
                        print("Meal not found.")

                # DELETE MEAL
                case "6":
                    mid = input("Meal id to delete: ")
                    confirm = input("Are you sure? (y/n): ")

                    if confirm == "y":
                        if delete_meal(meals, mid):
                            print("Meal deleted.")
                        else:
                            print("Meal not found.")
                    else:
                        print("Delete cancelled.")

                # ADD METRIC
                case "7":
                    mid = input("Metric id: ")
                    mtype = input("Metric type: ")
                    date = input("Date (YYYY-MM-DD): ")

                    if len(date) != 10 or date[4] != "-" or date[7] != "-":
                        print("Invalid date format.")
                        continue

                    value = float(input("Value: "))
                    if value <= 0:
                        print("Value must be positive.")
                        continue

                    metric = {
                        "id": mid,
                        "user_id": current_user["email"],
                        "type": mtype,
                        "date": date,
                        "value": value
                    }

                    log_metric(metrics_list, metric)
                    print("Metric added.")

                # LOGOUT
                case "8":
                    current_user = None
                    print("Logged out.")

                # HELP
                case "9":
                    print("Enter the number of the option you want to use.")
                    print("You can add, update, or delete workouts, meals, and metrics.")

                case _:
                    print("Invalid choice.")

if __name__ == "__main__":
    main()
