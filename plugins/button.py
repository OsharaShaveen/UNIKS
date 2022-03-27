# UNIKS - UserBot
# Copyright (C) 2021-2022 TeamUNIKS
#
# This file is a part of < https://github.com/TeamUNIKS/UNIKS/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUNIKS/UNIKS/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}button <text with button format`
   create button u can reply to pic also

Format:- `{i}button Hey There! @UseUNIKS 😎.
[UNIKS | t.me/theUNIKS][Support | https://t.me/httu2I8W94e9Lo3MmJl | same]
[TeamUNIKS | t.me/TeamUNIKS]`
"""
import os

from pyUltroid.functions.tools import create_tl_btn, get_msg_button
from telegraph import upload_file as uf
from telethon.utils import pack_bot_file_id

from . import HNDLR, get_string, mediainfo, UNIKS_cmd
from ._inline import something


@UNIKS_cmd(pattern="button")
async def butt(event):
    media, wut, text = None, None, None
    if event.reply_to:
        wt = await event.get_reply_message()
        if wt.text:
            text = wt.text
        if wt.media:
            wut = mediainfo(wt.media)
        if wut and wut.startswith(("pic", "gif")):
            dl = await wt.download_media()
            variable = uf(dl)
            media = "https://telegra.ph" + variable[0]
        elif wut == "video":
            if wt.media.document.size > 8 * 1000 * 1000:
                return await event.eor(get_string("com_4"), time=5)
            dl = await wt.download_media()
            variable = uf(dl)
            os.remove(dl)
            media = "https://telegra.ph" + variable[0]
        else:
            media = pack_bot_file_id(wt.media)
    try:
        text = event.text.split(maxsplit=1)[1]
    except IndexError:
        if not text:
            return await event.eor(
                f"**Please give some text in correct format.**\n\n`{HNDLR}help button`",
            )
    text, buttons = get_msg_button(text)
    if buttons:
        buttons = create_tl_btn(buttons)
    await something(event, text, media, buttons)
    await event.delete()
