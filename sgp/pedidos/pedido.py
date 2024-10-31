from flask import render_template,Blueprint,request
from models_dev import model



bp_pedido = Blueprint("pedido",__name__)


@bp_pedido.route("/pedidos",methods=["GET"])
def index():    
    return render_template("pedidos/index.html",title_page="Pedidos")
    


@bp_pedido.route("/pedidos/criar")
def create():
    number_os =  model.last_id()
    return render_template("pedidos/index obselt.html",title_page="Criação de Pedidos",number_os=number_os)


    
@bp_pedido.route("/pedido/<idd>",methods=["GET","POST"])
def view_pedido(idd):
    pedido = model.get_by_id((idd))
    if pedido is not None:
        return render_template("pedidos/view.html",pedido=pedido)
    else:
        return "Pedido não existe"
