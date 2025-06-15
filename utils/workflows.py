from utils.llm import LLMHandler
from dotenv import dotenv_values

class LinearWorkflow:
    def __init__(self):
        self.config = dotenv_values(".env")

        self.handler = LLMHandler(model_name="gpt-4o",
                            api_key=self.config["OPENAI_API_KEY"],
                            temperature=0.8)