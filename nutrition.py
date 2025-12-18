from datetime import datetime

def log_meal(meals: list, meal_data: dict) -> dict:
    meal_data["id"] = str(len(meals) + 1) #listede olduğu yere göre id
    meals.append(meal_data)
    return meal_data

def update_meal(meals: list, meal_id: str, updates: dict) -> dict:
    for m in meals:
        if m["id"] == meal_id:
            m.update(updates)
            return m
    raise ValueError #meal not found

def delete_meal(meals: list, meal_id: str) -> bool:
    for i, m in enumerate(meals):
        if m["id"] == meal_id:
            meals.pop(i)
            return True
    return False

def daily_calorie_summary(meals: list, user_id: str, date: str) -> dict:
    total = sum(m.get("calories", 0) for m in meals if m["user_id"] == user_id and m["timestamp"].startswith(date))
    #eğer user id uyuşuyorsa ve zaman içerisindeysek hepsini topluyor
    return {"date": date, "calories": total}

def macro_breakdown(meals: list, user_id: str, date_range: tuple[str, str]) -> dict:
    #aldığımız inputu datetime haline getirdik
    start, end = map(datetime.fromisoformat, date_range)
    macros = {"protein": 0, "carbs": 0, "fat": 0}
    for m in meals:
        t = datetime.fromisoformat(m["timestamp"])
        #user id ve zaman uyuşuyorsa 
        if m["user_id"] == user_id and start <= t <= end:
            for k in macros:
                macros[k] += m.get(k, 0) #boşsa 0 ver!!
    return macros