def log_workout(workouts, workout_data):
    workouts.append(workout_data)
    return workout_data


def update_workout(workouts, workout_id, updates):
    for workout in workouts:
        if workout['id'] == workout_id:
            workout.update(updates)
            return True
    return False


def delete_workout(workouts, workout_id):
    for workout in workouts:
        if workout['id'] == workout_id:
            workouts.remove(workout)
            return True
    return False


def weekly_workout_summary(workouts, user_id, week_start):
    total_workouts = 0
    total_duration = 0

    for workout in workouts:
        if workout['user_id'] == user_id:
            total_workouts += 1
            total_duration += workout.get('duration', 0)

    return {
        'total_workouts': total_workouts,
        'total_duration': total_duration
    }


def personal_records(workouts, user_id):
    records = {}

    for workout in workouts:
        if workout['user_id'] == user_id:
            for exercise in workout.get('exercises', []):
                name = exercise.get('name')
                weight = exercise.get('weight', 0)

                if name not in records:
                    records[name] = weight
                elif weight > records[name]:
                    records[name] = weight

    return records
