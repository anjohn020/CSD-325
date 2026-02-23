import requests

url = "http://api.open-notify.org/astros.json"

# Test connection
response = requests.get(url)
print("Status code:", response.status_code)

# Get JSON data
data = response.json()

# Print raw response
print("\nRaw response:")
print(data)

# Formatted output
print("\nPeople currently in space:")
for person in data["people"]:
    print(person["name"], "-", person["craft"])