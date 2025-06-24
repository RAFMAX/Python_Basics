from pathlib import Path
import json


file = Path("UserInfo.json")
def read():
    content = file.read_text()
    dict = json.loads(content)
    print(f"The Name is {dict['name']}, The Age is {dict['age']}, The Height is {dict['height']}")

def write():
    usernamedict = {}
    usernamedict['name'] = input("What's your name: ").title()
    usernamedict['age'] = input("What's your age: ")
    usernamedict['height'] = input("What's your height: ")
    content = json.dumps(usernamedict)
    file.write_text(content)

if file.exists():
    read()
else :
    write()