from flask import render_template,Blueprint,request
from models_dev import model



bp_pedido = Blueprint("core",__name__)


@bp_pedido.route("/criar",methods=["GET","POST"])
def criar_pedido():
    if request.method == "GET":
        return render_template("product.html",title_page="Criar Pedido")
    elif request.method == "POST":
        name = request.form.get("nameClient")
        
        return "SUcesso {}".format(name)
@bp_pedido.route("/pedido/<idd>",methods=["GET","POST"])
def view_pedido(idd):
    pedido = model.get_by_id((idd))
    if pedido is not None:
        return pedido
    else:
        return "Pedido não existe"
