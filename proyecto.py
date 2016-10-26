# -*- coding: utf-8 -*-
import os

from flask import Flask
from flaskext.mysql import MySQL

from routes.login_routes import login_r
from routes.usuario_routes import usuario

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views')
app = Flask(__name__, template_folder=tmpl_dir)
app.secret_key = 'proyecto_ufps'
mysql = MySQL()

# import routes
app.register_blueprint(login_r)

# MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'proyectoweb'
app.config['MYSQL_DATABASE_PASSWORD'] = 'proyectoweb'
app.config['MYSQL_DATABASE_DB'] = 'inventario'
app.config['MYSQL_DATABASE_HOST'] = 'sandbox2.ufps.edu.co'
mysql.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
