from webapp import line, handler

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello."))
