import requests

url = "https://api.agify.io/?name=antonio"

# Test connection
response = requests.get(url)
print("Status code:", response.status_code)

# Print raw response
print("\nRaw response:")
print(response.text)

# Convert to JSON
data = response.json()

# Formatted output
print("\nFormatted output:")
print("Name:", data["name"])
print("Predicted age:", data["age"])
print("Count:", data["count"])