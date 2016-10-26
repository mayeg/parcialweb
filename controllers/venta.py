
from dto.cliente import Cliente
from dao.producto import ProductoDao
from dto.venta import Venta
from dao.venta_dao import VentaDao
from dao.detalleventa_dao import DetalleVentaDao
from dto.detalle_venta import DetalleVenta
from flask import render_template, redirect, url_for


class DetalleVentaController:

    def get_registro_venta(self):
        productos = DetalleVentaDao().get_productos()
        clientes = DetalleVentaDao().get_clientes()
        return render_template("registro.html", productos=productos, clientes=clientes)

    def registrarVenta(self, numerofactura, producto, cliente, cantidad):
        venta = Venta(numerofactura=numerofactura, idcliente=cliente)
        producto = ProductoDao().get_producto_nombre(producto)
        if producto.getExistencias() > cantidad:
            if VentaDao().crearVenta(venta):
                return True


    def registarDetalleVenta(self, numerofactura ,producto, cantidad):

        venta = VentaDao().get_venta_numero(numerofactura)
        detalle = DetalleVenta(idproducto=producto, idfactura=venta.getNumeroFactura(),
                               cantidad=cantidad)

        self.calcularIvaYDescuentos(producto, detalle)
        DetalleVentaDao().crearDetalleVenta(detalle)


    def calcularIvaYDescuentos(self,producto, detalle):

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


