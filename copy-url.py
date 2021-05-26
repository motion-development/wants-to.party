try:
    import requests, pyperclip
except ImportError:
    print("You need pyperclip to run this code.")
    print("You can install it with: pip3 install pyperclip")
    exit()

SUBDOMAIN = "USERNAME"
API_KEY = "KEY"
FILE_NAME = "path/to/file"

response = requests.post(
    f"https://{SUBDOMAIN}.wants-to.party/upload", 
    headers={"key": API_KEY}, 
    files={"file": (FILE_NAME, open(FILE_NAME, "rb").read())}
)

pyperclip.copy(response.json()["url"])
print("Link Copied!")
