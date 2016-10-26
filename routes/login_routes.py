from flask.blueprints import Blueprint
from flask import request, redirect, url_for
from flask.globals import session
from controllers.index import Login
from controllers.venta import DetalleVentaController
from controllers.consulta import ConsultarP

login_r = Blueprint("login", __name__)


@login_r.route("/", methods=["GET"])
def get_home():
        return Login().get_home_usuario()


@login_r.route("/registroV", methods=["GET","POST"])
def registro():
    if request.method == "GET":
        return DetalleVentaController().get_registro_venta()

    if DetalleVentaController().get_registro_venta():
        pass


@login_r.route("/inventario", methods=["GET"])
def inventario():
    return ConsultarP().get_inventario()


