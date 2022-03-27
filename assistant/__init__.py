# UNIKS - UserBot
# Copyright (C) 2021-2022 TeamUNIKS
#
# This file is a part of < https://github.com/TeamUNIKS/UNIKS/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUNIKS/UNIKS/blob/main/LICENSE/>.

from pyUltroid import *
from pyUltroid import _ult_cache
from pyUltroid._misc import owner_and_sudos
from pyUltroid._misc._assistant import asst_cmd, callback, in_pattern
from pyUltroid.functions.helper import *
from pyUltroid.functions.tools import get_stored_file
from telethon import Button, custom

from plugins import ATRA_COL
from strings import get_languages, get_string, language

OWNER_NAME = UNIKS_bot.full_name
OWNER_ID = UNIKS_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
