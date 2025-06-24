from pathlib import Path
import json

def get_fav():
    return input("Write your fav number : ")
def fav():
    file = Path('favnum.json')
    if file.exists():
        content = file.read_text()
        favnum = json.loads(content)
        print(f"I know ur fav num is : {favnum}")
    else:
        favnum = get_fav()
        content = json.dumps(favnum)
        file.write_text(content)
        print("next time i will remember".title())

fav()