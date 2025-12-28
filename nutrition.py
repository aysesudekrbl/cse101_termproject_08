def log_meal(meals, meal_data):
    meals.append(meal_data)
    return meal_data


def update_meal(meals, meal_id, updates):
    for meal in meals:
        if meal['id'] == meal_id:
            meal.update(updates)
            return True
    return False


def delete_meal(meals, meal_id):
    for meal in meals:
        if meal['id'] == meal_id:
            meals.remove(meal)
            return True
    return False


def daily_calorie_summary(meals, user_id, date):
    total = 0

    for meal in meals:
        if meal['user_id'] == user_id and meal['date'] == date:
            total += meal.get('calories', 0)

    return {
        'date': date,
        'total_calories': total
    }


def macro_breakdown(meals, user_id, date_range):
    start_date, end_date = date_range
    protein = 0
    carbs = 0
    fat = 0

    for meal in meals:
        if meal['user_id'] == user_id:
            if start_date <= meal['date'] <= end_date:
                protein += meal.get('protein', 0)
                carbs += meal.get('carbs', 0)
                fat += meal.get('fat', 0)

    return {
        'protein': protein,
        'carbs': carbs,
        'fat': fat
    }
