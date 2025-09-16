import requests

response = requests.get("https://api.github.com/users/MixXLs")

if response.status_code == 200:
    user_date = response.json()

    print(f"Username: {user_date["login"]}")
    print(f"Name: {user_date["name"]}")
    print(f"Bio: {user_date["bio"]}")
    print(f"Public Repos: {user_date["public_repos"]}")
    print(f"Followers: {user_date["followers"]}")
    print(f"Following: {user_date["following"]}")
else:
    print("Failed to retrieve data.")