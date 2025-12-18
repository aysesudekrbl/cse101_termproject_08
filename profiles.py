import json
def load_users(path: str) -> list:
    try: #get user data from path
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError: #file does not exist
        return []

def save_users(path: str, users: list) -> None:
    with open(path, "w") as f: #save user data to the given path
        json.dump(users, f, indent=2)

def register_user(users: list, profile: dict) -> dict:
    profile["id"] = str(len(users) + 1) #listede bulunduğu yere göre id atadık-- değiştir
    users.append(profile) #sonra bu dicti users listesine ekledik
    return profile

def authenticate_user(users: list, email: str, pin: str) -> dict | None:
    for u in users:
        if u.get("email") == email and u.get("pin") == pin: #email ve pin uyuştu mu
            return u
    return None

def update_goal(users: list, user_id: str, goal_data: dict) -> dict:
    for u in users:
        if u.get("id") == user_id: #eğer doğru pinse
            u["goal"] = goal_data #yeni datayla değiştirdik
            return u
    raise ValueError #user not found