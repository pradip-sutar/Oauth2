import requests

# Replace <API_URL> with the URL of the API endpoint
api_url = "http://localhost:8000/myapp/api_protected/"

# Replace <your_token> with your actual token
token = "9dFVe1uZPpy6W4NMxDyUBU8KcVTXZm"

# Create the headers with the Authorization Bearer token
headers = {
    "Authorization": f"Bearer {token}"
}

# Send the GET request
response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response:", response.text)
