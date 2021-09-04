from webapp import line, handler

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply_text = event.message.text + "!!!"
    line.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text))
