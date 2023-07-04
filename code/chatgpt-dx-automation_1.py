import openai
import json

openai.api_key = "YOUR_API_KEY"

prompt = (f"User: Hello!\n"
		  f"AI: How can I help you today?\n"
		  f"User: Is there a trial version of your product?\n"
		  f"AI:")

response = openai.Completion.create(
	engine="davinci",
	prompt=prompt,
	temperature=0.5,
	max_tokens=1024,
	n=1,
	stop=None,
	frequency_penalty=0,
	presence_penalty=0
)

print(response.choices[0].text.strip())
