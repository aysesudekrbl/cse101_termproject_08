import json
import os
import shutil

def load_state(base_dir):
    users = []
    workouts = []
    meals = []
    metrics = []

    try:
        file = open(base_dir + "/users.json", "r")
        users = json.load(file)
        file.close()
    except:
        pass

    try:
        file = open(base_dir + "/workouts.json", "r")
        workouts = json.load(file)
        file.close()
    except:
        pass

    try:
        file = open(base_dir + "/nutrition.json", "r")
        meals = json.load(file)
        file.close()
    except:
        pass

    try:
        file = open(base_dir + "/metrics.json", "r")
        metrics = json.load(file)
        file.close()
    except:
        pass

    return users, workouts, meals, metrics


def save_state(base_dir, users, workouts, meals, metrics):
    file = open(base_dir + "/users.json", "w")
    json.dump(users, file)
    file.close()

    file = open(base_dir + "/workouts.json", "w")
    json.dump(workouts, file)
    file.close()

    file = open(base_dir + "/nutrition.json", "w")
    json.dump(meals, file)
    file.close()

    file = open(base_dir + "/metrics.json", "w")
    json.dump(metrics, file)
    file.close()


def backup_state(base_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

    files = ["users.json", "workouts.json", "nutrition.json", "metrics.json"]
    backed_up = []

    for name in files:
        src = base_dir + "/" + name
        dst = backup_dir + "/" + name

        if os.path.exists(src):
            shutil.copy(src, dst)
            backed_up.append(name)

    return backed_up


def validate_workout_entry(entry):
    if 'user_id' not in entry:
        return False
    if 'date' not in entry:
        return False
    if 'duration' not in entry:
        return False
    return True
