import sys
import requests

def main():

    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search", {"q": "monet"})
    except requests.HTTPError:
        print("Culdn't complate request!")
        sys.exit(1)

    contents = response.json()
    for artwork in contents["data"]:
        print(f"[*] {artwork["title"]}")

main()
