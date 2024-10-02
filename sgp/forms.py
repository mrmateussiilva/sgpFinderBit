from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class EntregaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    data_entrega = DateField('Data de Entrega', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Enviar')