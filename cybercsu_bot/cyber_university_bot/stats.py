import json
import os

STATS_FILE = "D:\\cybercsu_bot\\cyber_university_bot\\stats.json"

def load_stats() -> dict:
    if not os.path.exists(STATS_FILE):
        return {"users": []}
    with open(STATS_FILE, "r") as f:
        return json.load(f)


def save_user(user_id: int):
    stats = load_stats()
    if user_id not in stats["users"]:
        stats["users"].append(user_id)
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)


def get_user_count() -> int:
    stats = load_stats()
    return len(stats["users"])
