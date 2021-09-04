from flask import (
    render_template, send_from_directory, safe_join,
    request, abort,
)
from linebot.exceptions import InvalidSignatureError
from webapp import app
from webapp import app
from webapp.linebot import handler


@app.route('/')
def root():
    return render_template("index.j2")


@app.route('/favicon.ico')
def favicon():
    img_path = safe_join(app.static_folder, 'img')
    return send_from_directory(img_path, 'favicon.ico')


@app.route('/line', methods=['POST'])
def line_webhook():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature.")
        print("Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
