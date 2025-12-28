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

            if choice == "1":
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

            elif choice == "2":
                email = input("Email: ")
                pin = input("PIN: ")

                user = authenticate_user(users, email, pin)
                if user:
                    current_user = user
                    print("Login successful.")
                else:
                    print("Invalid credentials.")

            elif choice == "3":
                save_state("data", users, workouts, meals, metrics_list)
                print("Program exited.")
                break

            else:
                print("Invalid choice.")

        else:
            print(f"\n--- USER MENU ({current_user['email']}) ---")
            print("1 - Add workout")
            print("2 - Update workout")
            print("3 - Delete workout")
            print("4 - Add meal")
            print("5 - Update meal")
            print("6 - Delete meal")
            print("7 - Add metric")
            print("8 - Logout")

            choice = input("Choice: ")

            # ADD WORKOUT
            if choice == "1":
                wid = input("Workout id: ")
                date = input("Date (YYYY-MM-DD): ")
                duration = int(input("Duration (minutes): "))

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
            elif choice == "2":
                wid = input("Workout id to update: ")
                new_duration = int(input("New duration: "))

                updates = {
                    "duration": new_duration
                }

                if update_workout(workouts, wid, updates):
                    print("Workout updated.")
                else:
                    print("Workout not found.")

            # DELETE WORKOUT
            elif choice == "3":
                wid = input("Workout id to delete: ")

                if delete_workout(workouts, wid):
                    print("Workout deleted.")
                else:
                    print("Workout not found.")

            # ADD MEAL
            elif choice == "4":
                mid = input("Meal id: ")
                date = input("Date (YYYY-MM-DD): ")
                calories = int(input("Calories: "))

                meal = {
                    "id": mid,
                    "user_id": current_user["email"],
                    "date": date,
                    "calories": calories
                }

                log_meal(meals, meal)
                print("Meal added.")

            # UPDATE MEAL
            elif choice == "5":
                mid = input("Meal id to update: ")
                new_calories = int(input("New calories: "))

                updates = {
                    "calories": new_calories
                }

                if update_meal(meals, mid, updates):
                    print("Meal updated.")
                else:
                    print("Meal not found.")

            # DELETE MEAL
            elif choice == "6":
                mid = input("Meal id to delete: ")

                if delete_meal(meals, mid):
                    print("Meal deleted.")
                else:
                    print("Meal not found.")

            # ADD METRIC
            elif choice == "7":
                mid = input("Metric id: ")
                mtype = input("Metric type: ")
                date = input("Date (YYYY-MM-DD): ")
                value = float(input("Value: "))

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
            elif choice == "8":
                current_user = None
                print("Logged out.")

            else:
                print("Invalid choice.")

