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
            print("\n--- ANA MENÜ ---")
            print("1 - Kullanıcı ekle")
            print("2 - Giriş yap")
            print("3 - Çıkış")

            choice = input("Seçim: ")

            if choice == "1":
                email = input("Email: ")
                pin = input("PIN: ")

                profile = {
                    "email": email,
                    "pin": pin
                }

                if register_user(users, profile):
                    print("Kullanıcı eklendi.")
                else:
                    print("Bu email zaten var.")

            elif choice == "2":
                email = input("Email: ")
                pin = input("PIN: ")

                user = authenticate_user(users, email, pin)
                if user:
                    current_user = user
                    print("Giriş başarılı.")
                else:
                    print("Hatalı bilgi.")

            elif choice == "3":
                save_state("data", users, workouts, meals, metrics_list)
                print("Program kapandı.")
                break

            else:
                print("Geçersiz seçim.")

        else:
            print(f"\n--- KULLANICI MENÜSÜ ({current_user['email']}) ---")
            print("1 - Workout ekle")
            print("2 - Workout güncelle")
            print("3 - Workout sil")
            print("4 - Meal ekle")
            print("5 - Meal güncelle")
            print("6 - Meal sil")
            print("7 - Metric ekle")
            print("8 - Çıkış yap")

            choice = input("Seçim: ")

            # WORKOUT EKLE
            if choice == "1":
                wid = input("Workout id: ")
                date = input("Tarih (YYYY-MM-DD): ")
                duration = int(input("Süre (dk): "))

                workout = {
                    "id": wid,
                    "user_id": current_user["email"],
                    "date": date,
                    "duration": duration,
                    "exercises": []
                }

                log_workout(workouts, workout)
                print("Workout eklendi.")

            # WORKOUT GÜNCELLE
            elif choice == "2":
                wid = input("Güncellenecek workout id: ")
                new_duration = int(input("Yeni süre: "))

                updates = {
                    "duration": new_duration
                }

                if update_workout(workouts, wid, updates):
                    print("Workout güncellendi.")
                else:
                    print("Workout bulunamadı.")

            # WORKOUT SİL
            elif choice == "3":
                wid = input("Silinecek workout id: ")

                if delete_workout(workouts, wid):
                    print("Workout silindi.")
                else:
                    print("Workout bulunamadı.")

            # MEAL EKLE
            elif choice == "4":
                mid = input("Meal id: ")
                date = input("Tarih (YYYY-MM-DD): ")
                calories = int(input("Kalori: "))

                meal = {
                    "id": mid,
                    "user_id": current_user["email"],
                    "date": date,
                    "calories": calories
                }

                log_meal(meals, meal)
                print("Meal eklendi.")

            # MEAL GÜNCELLE
            elif choice == "5":
                mid = input("Güncellenecek meal id: ")
                new_calories = int(input("Yeni kalori: "))

                updates = {
                    "calories": new_calories
                }

                if update_meal(meals, mid, updates):
                    print("Meal güncellendi.")
                else:
                    print("Meal bulunamadı.")

            # MEAL SİL
            elif choice == "6":
                mid = input("Silinecek meal id: ")

                if delete_meal(meals, mid):
                    print("Meal silindi.")
                else:
                    print("Meal bulunamadı.")

            # METRIC EKLE
            elif choice == "7":
                mid = input("Metric id: ")
                mtype = input("Metric türü: ")
                date = input("Tarih (YYYY-MM-DD): ")
                value = float(input("Değer: "))

                metric = {
                    "id": mid,
                    "user_id": current_user["email"],
                    "type": mtype,
                    "date": date,
                    "value": value
                }

                log_metric(metrics_list, metric)
                print("Metric eklendi.")

            # LOGOUT
            elif choice == "8":
                current_user = None
                print("Çıkış yapıldı.")

            else:
                print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
