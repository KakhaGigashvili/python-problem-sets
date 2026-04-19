import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    num = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a0469cc06b4a70542d1e1380b1302812f9c210675a331f18c308c44c4419486")
    response.raise_for_status()
    data = response.json()
except requests.RequestException:
    sys.exit("Request failed")

try:
    price = float(data["data"]["priceUsd"])
except (KeyError, ValueError, TypeError):
    sys.exit("Invalid data from API")

total = num * price

print(f"${total:,.4f}")
