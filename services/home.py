from flask import Blueprint, config, request, render_template, redirect, url_for, flash
from config.db import pgsqlConn, sql
from services.publications import get_publications

home = Blueprint('home', __name__, template_folder='app/templates/home')

@home.route('/')
def Home():
    publicationsAll = get_publications()
    print(publicationsAll)
    return render_template('home/home.html', publications=publicationsAll)
