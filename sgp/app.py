from flask import Flask,render_template,request,redirect
from models_dev import model
from pedidos import core








app = Flask(__name__)
app.register_blueprint(core.bp_pedido)

@app.get("/")
def index():
    pedidos = model.get_all_pedidos()
    return render_template(
        "index.html"
        ,title_page="Pagina Inicial"
        ,pedidos=pedidos.items())


if __name__ == "__main__":
    app.run(debug=True)