import requests

api_key = "YOUR_API_KEY"
url = "https://api.openai.com/v1/engines/davinci-codex/completions"

def generate_text(prompt):
	headers = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {api_key}"
	}

	data = {
		"prompt": prompt,
		"max_tokens": 1024,
		"temperature": 0.5
	}

	response = requests.post(url, headers=headers, json=data)

	if response.status_code == 200:
		return response.json()["choices"][0]["text"]
	else:
		return None
    
