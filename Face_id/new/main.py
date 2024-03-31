import os
import webbrowser
import requests

path = os.getcwd() + "\\Face_id\\new\\"

def serverOpen():
    try:
        res = requests.get("http://localhost:3000")
        if res.status_code == 200:
            print("Yes")
        else:
            print("Error")
    except requests.ConnectionError:
        os.system(f"node {path}\\server.js")

    
if __name__ == "__main__":
    serverOpen()
    
    