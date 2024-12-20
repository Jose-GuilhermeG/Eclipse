from flask import render_template
from .bp import main
from ..models import user

@main.route('/')
def index():
    return render_template("index.html")