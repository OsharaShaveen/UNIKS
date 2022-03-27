# UNIKS - UserBot
# Copyright (C) 2021-2022 TeamUNIKS
#
# This file is a part of < https://github.com/TeamUNIKS/UNIKS/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUNIKS/UNIKS/blob/main/LICENSE/>.
"""
✘ Commands Available -

• {i}unsplash <search query> ; <no of pics>
    Unsplash Image Search.
"""

from pyUltroid.functions.misc import unsplashsearch

from . import asyncio, download_file, get_string, os, UNIKS_cmd


@UNIKS_cmd(pattern="unsplash( (.*)|$)")
async def searchunsl(ult):
    match = ult.pattern_match.group(1).strip()
    if not match:
        return await ult.eor("Give me Something to Search")
    num = 5
    if ";" in match:
        num = int(match.split(";")[1])
        match = match.split(";")[0]
    tep = await ult.eor(get_string("com_1"))
    res = await unsplashsearch(match, limit=num)
    if not res:
        return await ult.eor(get_string("unspl_1"), time=5)
    CL = [download_file(rp, f"{match}-{e}.png") for e, rp in enumerate(res)]
    imgs = [z for z in (await asyncio.gather(*CL)) if z]
    await ult.client.send_file(
        ult.chat_id, imgs, caption=f"Uploaded {len(imgs)} Images!"
    )
    await tep.delete()
    [os.remove(img) for img in imgs]
