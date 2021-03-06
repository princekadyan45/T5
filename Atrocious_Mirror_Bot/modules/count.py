# Implement By - @anasty17 (https://github.com/breakdowns/slam-tg-mirror-bot/pull/111)
# (c) https://github.com/breakdowns/slam-tg-mirror-bot
# All rights reserved

from telegram.ext import CommandHandler
from Atrocious_Mirror_Bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from Atrocious_Mirror_Bot.helper.telegram_helper.message_utils import deleteMessage, sendMessage
from Atrocious_Mirror_Bot.helper.telegram_helper.filters import CustomFilters
from Atrocious_Mirror_Bot.helper.telegram_helper.bot_commands import BotCommands
from Atrocious_Mirror_Bot import dispatcher


def countNode(update, context):
    args = update.message.text.split(" ", maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"Counting: <code>{link}</code>", context.bot, update)
        gd = GoogleDriveHelper()
        result = gd.count(link)
        deleteMessage(context.bot, msg)
        if update.message.from_user.username:
            uname = f'@{update.message.from_user.username}'
        else:
            uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
        if uname is not None:
            cc = f'\n\ncc: {uname}'
        sendMessage(result + cc, context.bot, update)
    else:
        sendMessage("Provide G-Drive Shareable Link to Count.", context.bot, update)

count_handler = CommandHandler(BotCommands.CountCommand, countNode, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(count_handler)
