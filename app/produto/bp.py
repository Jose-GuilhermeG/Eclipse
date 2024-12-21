from flask import Blueprint

produtos = Blueprint("produto", __name__)

from . import views