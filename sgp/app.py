from flask import Flask,render_template,request,redirect
import json


def load_model_dev():
    f = "../models_dev/models.json"
    with open(f, "r") as fp:
        data = json.load(fp)
        print(data)
    return dict(data)
    



app = Flask(__name__)


@app.get("/")
def index():
    pedidos = load_model_dev()
    return render_template("index.html",title_page="Pagina Inicial",pedidos=pedidos.items())

@app.route("/criar")
def criar_pedido():
    return render_template("product.html",title_page="Criar Pedido")
    pass


if __name__ == "__main__":
    app.run(debug=True)