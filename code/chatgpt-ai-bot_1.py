import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

print(secrets)
# {
#   "api_key": "YOUR_API_KEY"
# }
