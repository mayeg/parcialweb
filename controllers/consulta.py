from dto.cliente import Cliente
from dao.producto import ProductoDao
from dto.venta import Venta
from dao.venta_dao import VentaDao
from dao.detalle_venta_dao import DetalleVentaDao
from dto.detalle_venta import DetalleVenta
from flask import render_template, redirect, url_for



class ConsultarP:

    def get_inventario(self):
        detalleventa = DetalleVentaDao().get_total_cantidad()
        return render_template("inventario.html", detalles=detalleventa)










