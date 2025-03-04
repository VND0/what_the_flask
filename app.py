from flask import Flask, render_template

app = Flask(__name__)


@app.get("/<title>")
@app.get("/index/<title>")
def index(title: str):
    return render_template("base.html", title=title)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
