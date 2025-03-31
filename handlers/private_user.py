from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

from lexicon.lexicon_ru import cmd

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(cmd['/start'])
