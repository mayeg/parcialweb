# -*- coding: utf-8 -*-
import hashlib

from flask import session, render_template, redirect, url_for
from flask.helpers import flash


class Login:

    def __init__(self):
        pass

    @staticmethod
    def get_home_usuario():
        return render_template('index.html')

