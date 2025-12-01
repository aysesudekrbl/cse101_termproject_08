def log_workout(workouts: list, workout_data: dict) -> dict: 
    pass 


def update_workout(workouts: list, workout_id: str, updates: dict) -> dict:
    for i in range(len(workouts)):
        if workouts[i] == workout_id:
            workouts[i] = updates


def delete_workout(workouts: list, workout_id: str) -> bool:
    for i in range(len(workouts)):
        if workouts[i] == workout_id:
            workouts.pop(i)


def weekly_workout_summary(workouts: list, user_id: str, week_start: str) -> dict:
    pass 

def personal_records(workouts: list, user_id: str) -> dict:
    pass