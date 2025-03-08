from typing import Literal

from flask import Flask, render_template, redirect, url_for

from forms import DoubleProtection

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


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
