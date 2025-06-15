from utils.llm import LLMHandler
from dotenv import dotenv_values

config = dotenv_values(".env")

handler = LLMHandler(model_name="gpt-4o",
                     api_key=config["OPENAI_API_KEY"],
                     temperature=0.8)

response = handler.query("What is your favorite color?")

print(response)
