import requests

url = 'https://api.github.com'
headers = {'Authorization': 'token <YOUR_TOKEN>'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
	print('Success!')
else:
	print('Failed.')
