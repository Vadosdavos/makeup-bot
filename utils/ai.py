from utils.config_reader import config
from mistralai import Mistral
import logging

api_key = config.api_key.get_secret_value()
model = "pixtral-12b-2409"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

async def generate_recommendation(prompt) -> str:
    try:
        response = client.chat.complete(
            model= model,
            messages = [
                {
                    "role": "user",
                    "content": f'Посоветуй книгу похожую на книгу: {prompt}',
                },
            ]
        )
        print(response)
        print(f'Total tokens: {response.usage.total_tokens}')
        return response.choices[0].message.content
    except Exception as e:
        logging.error(e)
