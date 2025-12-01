import json

DEFAULT_USER_PATH = "users.json"

def load_users(path: str):
    with open (path,"r") as f:
        return json.load(f)
    

def save_users(path: str, users: list):
    
    with open(path, "w") as f:
        f.write(users)
        #users listesini verilen konuma kaydedecek??
    
def register_user(users: list, profile: dict):
    newuser = {
        #buraya profilden veri çekecek bir dictionary yazılması lazım
    }
    users.append(newuser)
    return newuser


def authenticate_user(users: list, email: str, pin: str):
    for user in users:
        if user.get("email") == email and user.get("pin") == pin:
             #kullanıcı bulundu
            return user
        else:
            #kullanıcı bulunamadı
            print("No user with that name or id.")
            return None


def update_goal(users: list, user_id: str, goal_data: dict):
    for user in users:
        # id ile uyuşan kullanıcıyı bulup onun goal'una erişmeliyiz
        if user_id == user.get("user_id"):
            user["goal"].update (goal_data)

