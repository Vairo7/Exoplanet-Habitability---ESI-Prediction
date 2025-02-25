import requests

url = 'http://127.0.0.1:5000/ayy'

# Correct format as expected by the API
planet = {
    'features': [1.2, 0.95, 0.78, 0.74, -0.42]  # Values in a list
}

response = requests.post(url, json=planet)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
