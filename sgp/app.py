from flask import Flask,render_template,request,redirect
import json

from models_dev import model







app = Flask(__name__)


@app.get("/")
def index():
    pedidos = model.load_model_dev()
    return render_template("index.html",title_page="Pagina Inicial",pedidos=pedidos.items())

@app.route("/criar")
def criar_pedido():
    return render_template("product.html",title_page="Criar Pedido")


@app.route("/pedido/<idd>",methods=["GET"])
def view_pedido(idd):
    pedido = model.get_by_id((idd))
    if pedido is not None:
        return pedido
    else:
        return "Pedido não existe"

if __name__ == "__main__":
    app.run(debug=True)