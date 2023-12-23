from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators, IntegerField, SelectField
from wtforms.validators import DataRequired


class GenForm(FlaskForm):
    example = "Du bist ein Mathematik-Tutor, beantworte deshalb nur Fragen zu Mathematik. Halte deine Antworten kurz. Wenn andere Fragen gestellt werden oder die Frage nicht mit dem Jugendschutz vereinbar ist, antworte: 'Ich kann diese Frage nicht beantworten.'"
    #api_key = StringField('API-Key von OpenAI: ', validators=[DataRequired()])
    context = TextAreaField('Kontextinformationen (hier mit Beispieltext):',
                            [validators.optional(), validators.length(max=512)], default=example, render_kw={"rows": 7})
    submit = SubmitField('Generiere Link')

class GenPicForm(FlaskForm):
    #vals = SelectField("Anzahl Links:", choices=[(str(num), str(num)) for num in range(1, 34)])
    vals = IntegerField('Anzahl Links:',[validators.DataRequired(), validators.NumberRange(min=1, max=33)])
    submit = SubmitField('Generiere Links')