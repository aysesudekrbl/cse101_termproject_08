import json

def load_users(path):
    try:
        f = open(path, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return []


def save_users(path, users):
    f = open(path, "w")
    json.dump(users, f)
    f.close()


def register_user(users, profile):
    email_exists = False

    for u in users:
        if u.get("email") == profile.get("email"):
            email_exists = True

    if email_exists:
        return False

    if "goals" not in profile:
        profile["goals"] = {}

    users.append(profile)
    return True


def authenticate_user(users, email, pin):
    for u in users:
        if u.get("email") == email:
            if u.get("pin") == pin:
                return u
    return None


def update_goal(users, user_id, goal_data):
    for u in users:
        if u.get("email") == user_id:
            if "goals" not in u:
                u["goals"] = {}

            for key in goal_data:
                u["goals"][key] = goal_data[key]

            return True

    return False
