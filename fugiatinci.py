import requests

# Define your API key (example)
api_key = 'your_openai_api_key_here'

# Define headers with API key
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Example payload for generating chat completion
prompt = "Hello, how can I help you today?"
payload = {
    'model': 'text-davinci-003',  # Specify the model you want to use
    'messages': [
        {'role': 'user', 'content': prompt}
    ]
}

# Send POST request to example API
response = requests.post("https://api.example.com/v1/chat/completions", headers=headers, json=payload)

# Handle response
if response.status_code == 200:
    data = response.json()
    # Process data as needed
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
