from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DoubleProtection(FlaskForm):
    astro_id = IntegerField("ID астронавта", validators=[DataRequired()])
    astro_passwd = PasswordField("Пароль астронавта", validators=[DataRequired()])
    cap_id = IntegerField("ID капитана", validators=[DataRequired()])
    cap_passwd = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")
