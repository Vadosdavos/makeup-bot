from utils.config_reader import config
from mistralai import Mistral
import logging
import json

api_key = config.api_key.get_secret_value()
model = "pixtral-12b-2409"

client = Mistral(api_key=api_key)

async def generate_recommendation_by_book(prompt) -> list:
    try:
        response = client.chat.complete(
            model= model,
            messages = [
                {
                    "role": "user",
                    "content": f'Представь, что ты опытный литературный критик, который прочитал почти все существующие книги. Посоветуй несколько книг, похожих на книгу: {prompt}.' + "Верни рекомендации в виде короткого JSON объекта вот с такой структурой: 'books': [{'title': string, 'author': string, 'description': string }]",
                },
            ],
            response_format = {
                "type": "json_object",
            }
        )
        books = json.loads(response.choices[0].message.content)['books']
        return books
    except Exception as e:
        logging.error(e)

async def generate_recommendation_by_genre(prompt) -> list:
    try:
        response = client.chat.complete(
            model= model,
            messages = [
                {
                    "role": "user",
                    "content": f'Представь, что ты опытный литературный критик, который прочитал почти все существующие книги. Посоветуй несколько книг из жанра: "{prompt}".' + "Верни рекомендации в виде короткого JSON объекта вот с такой структурой: 'books': [{'title': string, 'author': string, 'description': string }]",
                },
            ],
            response_format = {
                "type": "json_object",
            }
        )
        books = json.loads(response.choices[0].message.content)['books']
        return books
    except Exception as e:
        logging.error(e)