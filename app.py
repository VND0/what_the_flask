from typing import Literal

from flask import Flask, render_template

app = Flask(__name__)
OCCUPATIONS = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер о терраформированию",
    "климатолог",
    "специалист по радиационной защите",
    "астрогеолог",
    "гляциолог",
    "инженер жизнеобеспечения",
    "метеоролог",
    "оператор марсохода",
    "киберинженер",
    "штурман",
    "пилот дронов",
]


@app.get("/<title>")
@app.get("/index/<title>")
def index(title: str):
    return render_template("base.html", title=title)


@app.get("/list_prof/<lst>")
def list_prof(lst: Literal["ul", "ol"]):
    return render_template("occup_list.html", lst=lst, occupations=OCCUPATIONS)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
