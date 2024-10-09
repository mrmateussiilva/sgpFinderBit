from flask import render_template,Blueprint
from models_dev import model



bp_pedido = Blueprint("core",__name__)





@bp_pedido.route("/criar")
def criar_pedido():
    return render_template("product.html",title_page="Criar Pedido")


@bp_pedido.route("/pedido/<idd>",methods=["GET"])
def view_pedido(idd):
    pedido = model.get_by_id((idd))
    if pedido is not None:
        return pedido
    else:
        return "Pedido não existe"
