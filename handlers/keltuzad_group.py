from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import FSInputFile

from filters.chat_type import ChatTypeFilter

router = Router()

@router.message(ChatTypeFilter(chat_type=["group", "supergroup"]), F.text)
async def cmd_keltuzad_in_group(message: Message, kel_image: FSInputFile, kel_id: list):
    print(','.join(kel_id))
    sub = 'ученые'
    text = message.text.lower()
    if sub in text:
        first_letter_index = text.index(sub)
        quote = f'{message.text[first_letter_index]}ченые'
        await message.answer('В говне моченые', reply_parameters={'message_id': message.message_id ,'quote': quote})
        if not kel_id:
            result = await message.answer_photo(kel_image)
            kel_id = kel_id.append(result.photo[-1].file_id)
        else:
            await message.answer_photo(kel_id[0])