from flask import (
    Flask,
    render_template,
    url_for
)
from pyhead import Head

from app.business_info import BusinessInfo
from app.favicons import favicons


def create_app():
    app = Flask(__name__, static_url_path="/")

    @app.get("/")
    def index():
        head = Head()
        head.set_title("Business Card")
        head.set_favicon(**favicons)
        head.set_link_tag(rel="stylesheet", href=url_for("static", filename="main.css"))

        return render_template(
            "index.html",
            head=head,
            business_info=BusinessInfo()
        )

    return app


def debug():
    app = create_app()
    app.run(debug=True, port=5000)
