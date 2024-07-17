from flask import Blueprint, request, render_template, redirect, url_for, flash
from config.db import pgsqlConn, sql

publications = Blueprint('publications', __name__, template_folder='app/templates/publications')

#@publications.route('/publications')
def get_publications():
    cur = pgsqlConn.cursor()
    columns = ("id", "titulo", "descripcion")
    stmt = sql.SQL('SELECT {} FROM {} LIMIT 5').format(
                sql.SQL(',').join(map(sql.Identifier, columns)),
                sql.Identifier('publicaciones')
            )
    cur.execute(stmt)
    publicationsAll = cur.fetchall()
    return publicationsAll
#render_template('publications/publications.html', publications=publicationsAll)

@publications.route('/publications/new_publication')
def NewPublicacion():
    return render_template('publications/new_publications.html')

@publications.route('/publications/add_publications', methods=['POST'])
def add_publicacion():
        if request.method == 'POST':
            titulo = request.form['titulo']
            descripcion = request.form['descripcion']
            descripcion_full = request.form['descripcion_full']
            try:
                cur = pgsqlConn.cursor()
                cur.execute(
                    "INSERT INTO publicaciones (titulo, descripcion, descripcion_full) VALUES (%s,%s,%s)", (titulo, descripcion, descripcion_full))
                pgsqlConn.commit()
                flash('Publicacion Added successfully')
                return redirect(url_for('home.Home'))
            except Exception as e:
                flash(e.args[1])
                return redirect(url_for('home.Home'))

@publications.route('/publications/detail/<id>', methods=['GET'])
def get_publication_detail(id):
    cur = pgsqlConn.cursor()
    cur.execute('SELECT * FROM publicaciones WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('publications/detail_publications.html', publicacion=data[0])
