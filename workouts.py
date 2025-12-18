from datetime import datetime, timedelta

def log_workout(workouts: list, workout_data: dict) -> dict:
    workout_data["id"] = str(len(workouts) + 1) #listedeki yerine göre id verdik antrenmana
    workouts.append(workout_data) #daha sonra bunu listeye ekledik
    return workout_data

def update_workout(workouts: list, workout_id: str, updates: dict) -> dict:
    for w in workouts:
        if w["id"] == workout_id: #uyuşan workoutu bulduk
            w.update(updates)
            return w
    raise ValueError #workout not found

def delete_workout(workouts: list, workout_id: str) -> bool:
    for i, w in enumerate(workouts):
        if w["id"] == workout_id:
            workouts.pop(i)
            return True
    return False

def weekly_workout_summary(workouts: list, user_id: str, week_start: str) -> dict:
    start = datetime.fromisoformat(week_start) 
    end = start + timedelta(days=7)
   
    selected = [w for w in workouts if w["user_id"] == user_id and start <= datetime.fromisoformat(w["date"]) < end]
    #eğer hem id uyuyosa hem de daha bitmediyse süresi
    return {
        "count": len(selected),
        "total_minutes": sum(w.get("duration", 0) for w in selected)
    }

def personal_records(workouts: list, user_id: str) -> dict:
    records = {}
    for w in workouts:
        if w["user_id"] == user_id:
            for ex in w.get("exercises", []):
                name = ex["name"]
                weight = ex.get("weight", 0)
                records[name] = max(records.get(name, 0), weight)
    return records