from flask import render_template,Blueprint,request
from models_dev import model



bp_pedido = Blueprint("pedido",__name__)


@bp_pedido.route("/pedidos",methods=["GET"])
def index():    
    return render_template("pedidos/index.html",title_page="Pedidos")
    


@bp_pedido.route("/pedidos/criar")
def create():
    return render_template("pedidos/create.html",title_page="Criação de Pedidos")


    
@bp_pedido.route("/pedido/<idd>",methods=["GET","POST"])
def view_pedido(idd):
    pedido = model.get_by_id((idd))
    if pedido is not None:
        return pedido
    else:
        return "Pedido não existe"
