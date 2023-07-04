import openai

openai.api_key = secrets["api_key"]

def generate_text(prompt):
	model_engine = "text-davinci-002"
	response = openai.Completion.create(
		engine=model_engine,
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
	)
	message = response.choices[0].text
	return message.strip()
