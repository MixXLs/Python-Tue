def analyze_user_activity(log_file_path: str) -> dict:
    action_count = {}
    actions_by_user = {}
    login_time = {}
    user = set()

    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:

            box = line.strip().split()
            if len(box) != 4:
                continue

            timestamp, user_id, action, duration = box
            
            user.add(user_id)
            action_count[action] = action_count.get(action, 0) + 1
            actions_by_user[user_id] = actions_by_user.get(user_id, 0) + 1
            
            if action == "login":
                login_time[user_id] = login_time.get(user_id, 0.0) + float(duration)

    total_user = len(user)
    total_time = sum(login_time.values())
    average_session_time = total_time / len(user) if len(user) > 0 else 0

    most_active_user = (max(login_time, key=login_time.get) if login_time else None)

    return {
        "total_users":total_user,
        "action_counts":action_count,
        "most_active_user":most_active_user,
        "average_session_time":average_session_time,
    }



if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint

    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}