from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""hallo,gua adalaah  mussic santai bot, gua di buat untuk menemani waktu santai lu di vcg.

ini list perintah yang bisa lu gunakan, jika masih gk ngerti harap pc owner:

/play - play the replied audio file or YouTube video
/pause - pause the audio stream
/resume - resume the audio stream
/skip - skip the current audio stream
/mute - mute the userbot
/unmute - unmute the userbot
/stop - clear the queue and remove the userbot from the call""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'Group📌', url='https://t.me/wavyheartt',
                    ),
                    InlineKeyboardButton(
                        'Channel📌', url='https://t.me/calonpenyanyi',
                    ),
                    InlineKeyboardButton(

                        'owner📌', url='https://t.me/gksukaribett',
                ],
            ],
        ),
    )
