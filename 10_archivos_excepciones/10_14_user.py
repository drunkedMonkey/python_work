import json
from pathlib import Path

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    path = Path("10_archivos_excepciones/username.json")
    username = get_stored_username(path)
    if username:
        response = ''
        while response not in ['y', 'n']:
            response = input(f"Is {username} your username? (y/n) ")
            if response not in ['y', 'n']:
                print("Please enter 'y' or 'n'")
        if response == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()