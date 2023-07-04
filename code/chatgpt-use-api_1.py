import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# APIキーを設定
import openai
openai.api_key = secrets["api_key"]
