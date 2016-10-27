from flask.blueprints import Blueprint
from flask import request, redirect, url_for
from flask.globals import session
from controllers.index import Login
from controllers.venta import DetalleVentaController
from controllers.consulta import ConsultarP

facturas = Blueprint("facturas", __name__)


@facturas.route("/", methods=["GET"])
def get_home():
        return Login().get_home_usuario()


@facturas.route("/registro_venta", methods=["GET","POST"])
def get_view_registro():
    if request.method == "GET":
        return DetalleVentaController().crear_venta()
    return DetalleVentaController().registrar_venta(request.form)


@facturas.route("/get_cliente/<id>", methods=["GET"])
def get_cliente(id):
    return DetalleVentaController().get_cliente(id)

@facturas.route("/inventario", methods=["GET"])
def inventario():
    return ConsultarP().get_inventario()


