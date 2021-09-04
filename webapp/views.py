from flask import (
    render_template, send_from_directory, safe_join
)
from webapp import app


@app.route('/')
def root():
    return render_template("index.j2")


@app.route('/favicon.ico')
def favicon():
    img_path = safe_join(app.static_folder, 'img')
    return send_from_directory(img_path, 'favicon.ico')
