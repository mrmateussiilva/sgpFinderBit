from flask import Flask,render_template,request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from forms import EntregaForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'



@app.route('/', methods=['GET', 'POST'])
def formulario():
    form = EntregaForm()
    if form.validate_on_submit():
        nome = form.nome.data
        data_entrega = form.data_entrega.data
        return render_template("sucess_pedido.html",title_page="Pedido Sucess",name=nome,date=data_entrega)
    return render_template('formulario.html', form=form)

@app.route("/criar")
def criar_pedido():
    return render_template("product.html",title_page="Criar Pedido")
    


if __name__ == "__main__":
    app.run(debug=True)