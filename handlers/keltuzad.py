from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def cmd_keltuzad(message: Message):
    sub = 'ученые'
    text = message.text.lower()
    if sub in text:
        first_letter_index = text.index(sub)
        quote = f'{message.text[first_letter_index]}ченые'
        await message.answer('В говне моченые', reply_parameters={'message_id': message.message_id ,'quote': quote})