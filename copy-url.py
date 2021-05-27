try:
    import requests, pyperclip
except ImportError:
    print("You need pyperclip to run this code.")
    print("You can install it with:")
    print("pip3 install pyperclip")
    print("or")
    print("pip install pyperclip")
    exit()

SUBDOMAIN = input("Enter your subdomain/username: ")
API_KEY = input("Enter your API key (case sensitive): ")
FILE_NAME = input("Enter your file name: ")

response = requests.post(
    f"https://{SUBDOMAIN}.wants-to.party/upload", 
    headers={"key": API_KEY}, 
    files={"file": (FILE_NAME, open(FILE_NAME, "rb").read())}
)

try:
    pyperclip.copy(response.json()["url"])
    print("Link Copied!")
except:
    print("Something went wrong, here are possible fixes:")
    print("1. Recheck your username/subdomain")
    print("2. Recheck your API key")
    print("3. The file has no bytes (empty)")
