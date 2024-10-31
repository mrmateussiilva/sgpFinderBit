from flask import Flask,render_template,request,redirect
from models_dev import model
from pedidos import pedido


app = Flask(__name__)
app.register_blueprint(pedido.bp_pedido)


@app.get("/")
def index():
    return render_template(
        "index.html"
        ,title_page="Pagina Inicial"
        )


if __name__ == "__main__":
    app.run(debug=True)