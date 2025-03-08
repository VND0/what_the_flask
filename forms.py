from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import PasswordField, IntegerField, SubmitField, FileField
from wtforms.validators import DataRequired


class DoubleProtection(FlaskForm):
    astro_id = IntegerField("ID астронавта", validators=[DataRequired()])
    astro_passwd = PasswordField("Пароль астронавта", validators=[DataRequired()])
    cap_id = IntegerField("ID капитана", validators=[DataRequired()])
    cap_passwd = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


class AddToCarousel(FlaskForm):
    image = FileField("Добавить картинку", validators=[FileRequired()])
    submit = SubmitField("Отправить")
