from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot




async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/33193e0075fc37c000379.jpg",
                caption="š¹ **Tonic UserBot Has Been Actived**!!\nāāāāāāāāāāāāāāā\nā  **Userbot Version** - 5.0@master\nāāāāāāāāāāāāāāā\nā  **Powered By:** @PrimeSupportChannel ",
                buttons=[(Button.url("ź±į“į“į“į“Źį“", "https://t.me/PrimeSupportGroup"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
