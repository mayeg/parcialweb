from flask.json import jsonify

from dao.cliente_dao import ClienteDao
from dto.cliente import Cliente
from dao.producto import ProductoDao
from dto.venta import Venta
from dao.venta_dao import VentaDao
from dao.detalle_venta_dao import DetalleVentaDao
from dto.detalle_venta import DetalleVenta
from flask import render_template, redirect, url_for


class DetalleVentaController:

    def crear_venta(self, error="", success=""):
        clientes = ClienteDao().get_clientes()
        productos = ProductoDao().get_productos()
        return render_template("ventas/registro.html", clientes=clientes,
                               productos=productos, error=error, success=success)

    def get_cliente(self, id):
        cliente = ClienteDao().get_cliente(id).get_dict()
        return jsonify(cliente)


    def registrar_venta(self, formulario):
        try:
            id_cliente = formulario.get('cliente', None)
            if id_cliente is None:
                return
            productos = ProductoDao().get_productos()
            productos_modificados = list()
            detalle_venta = list()
            total = 0
            total_descuentos = 0
            total_iva = 0
            for producto in productos:
                cantidad = formulario.get('producto_' + producto.getId(), None)
                if cantidad is not None and int(cantidad) > 0:
                    if producto.getExistencias >= cantidad:
                        producto.setExistencias(producto.getExistencias() - cantidad)
                        productos_modificados.append(producto)
                        detalle = DetalleVenta(
                            producto.getId(), cantidad=int(cantidad))
                        detalle = self.calcular_iva_descuento(producto, detalle)
                        detalle.setTotal(int(cantidad)*producto.getPrecioVenta +
                                         detalle.getValorIva() - detalle.getValorDescuentos())
                        detalle_venta.append(detalle)
                        total += detalle.getTotal()
                        total_descuentos += detalle.getValorDescuentos()
                        total_iva += detalle.getValorIva()
                    else:
                        return self.crear_venta(
                            error="No existen cantidades suficientes del "
                                  "producto {}.".format(producto.getNombre()))

            venta = Venta(idcliente=id_cliente, valortotal=total,
                          valoriva=total_iva, valordescuentos=total_descuentos)

            if VentaDao().crear_venta(venta):

                venta = VentaDao().get_ultima_venta()
                for detalle in detalle_venta:
                    detalle.setIdFactura(venta.getNumeroFactura())
                    DetalleVentaDao().crearDetalleVenta(detalle)
                for producto in productos_modificados:
                    ProductoDao().modificar_existencias(producto)

            return self.crear_venta(success="La venta se realizo correctamente.")
        except Exception as e:
            print e.message
            return self.crear_venta(error="Error en el servidor.")

    def calcular_iva_descuento(self, producto, detalle):

        if producto.getTipo() == "Electrodomesticos":
            detalle.setValorIva(0.10)
            detalle.setValorDescuentos(0.05)

        elif producto.getTipo() == "Medicamentos":
            detalle.setValorIva(0.04)
            detalle.setValorDescuentos(0.1)

        elif producto.getTipo() == "Frutas y Verduras":
            detalle.setValorIva(0)
            detalle.setValorDescuentos(0.1)

        elif producto.getTipo() == "Vestir":
            detalle.setValorIva(0.08)
            detalle.setValorDescuentos(0)

        elif producto.getTipo() == "Bebidas Alcoholicas y cigarrillos":
            detalle.setValorIva(0.2)
            detalle.setValorDescuentos(0)

        return detalle

