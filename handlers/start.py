from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.formatting import Text, Bold, as_list, as_marked_section

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    content = as_list(
        Text("Привет, ",
        Bold(message.from_user.full_name), "!"),
        as_marked_section(
            Bold("В боте доступны команды:"),
            " /meme",
            marker='    '
        ),
        sep="\n\n"
    )
    await message.answer(**content.as_kwargs())