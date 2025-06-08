from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="NONE",
)

prompt = "What is your favorite color?"

response = client.chat.completions.create(
                                            model="lmistral-7b-instruct",
                                            messages=[
                                                {
                                                    "role": "user",
                                                    "content": prompt,
                                                }
                                            ],
                                            stream=False,
                                            max_tokens=100,
                                            temperature=0.2,
                                            top_p=0.5,
                                            frequency_penalty=0.5
                                        )

print(response.choices[0].message.content)
