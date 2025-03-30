import json
import os
from typing import Literal

from flask import Flask, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from forms import DoubleProtection, AddToCarousel

app = Flask(__name__)
app.config["SECRET_KEY"] = "382adc65b7fcd23c786cc733d7d2a1"
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


@app.get("/answer")
@app.get("/auto_answer")
def auto_answer():
    params = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True,
    }
    return render_template("auto_answer.html", **params)


@app.route("/login", methods=["POST", "GET"])
def double_protection():
    form = DoubleProtection()
    if form.validate_on_submit():
        print(form.astro_id.data)
        print(form.cap_id.data)
        return redirect("/Mars")
    return render_template("double_protection.html", title="Аварийный доступ", form=form)


@app.get("/training/<prof>")
def training(prof: str):
    # Я не в курсе, что за картинки надо все равно. Вставил вторую часть того, что нашел в интернете
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        title = "Инженерные тренажеры"
        img = url_for("static", filename="img/it.png")
    else:
        title = "Научные симуляторы"
        img = url_for("static", filename="img/ns.png")

    return render_template("training.html", title=title, img=img)


@app.get("/distribution")
def distribution():
    people = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин",
    ]
    return render_template("distribution.html", title="Размещение по каютам", room_name="Каюта №", people=people)


@app.route("/carousel", methods=["POST", "GET"])
def carousel():
    form = AddToCarousel()
    if form.validate_on_submit():
        add_to_carousel(form)
        return redirect("carousel")

    images = []
    for img in os.listdir(os.path.join(app.static_folder, "carousel")):
        images.append(url_for("static", filename=os.path.join("carousel", img)))

    return render_template("carousel.html", title="Красная планета", images=images, form=form)


def add_to_carousel(form: AddToCarousel):
    file = form.image.data
    file.save(os.path.join(app.static_folder, "carousel", secure_filename(file.filename)))


@app.get("/table/<gender>/<int:age>")
def rooms(gender: Literal["male", "female"], age: int):
    if age > 21:
        img_src = url_for("static", filename="img/adult.png")
    else:
        img_src = url_for("static", filename="img/child.png")

    if gender == "male":
        if age > 21:
            bg_col = "#027ff0"
        else:
            bg_col = "#b4c3dc"
    else:
        if age > 21:
            bg_col = "#eb5528"
        else:
            bg_col = "#f2a481"

    return render_template("room.html", title="Оформление каюты", bg_col=bg_col, img_src=img_src)


@app.get("/members")
def members():
    with open("templates/personalData.json") as f:
        as_json = json.load(f)
    return render_template("personal_card.html", data=as_json)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
