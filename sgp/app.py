from flask import Flask,render_template,request,redirect




app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index.html",title_page="Pagina Inicial")

@app.route("/criar")
def criar_pedido():
    return render_template("product.html",title_page="Criar Pedido")
    pass


if __name__ == "__main__":
    app.run(debug=True)