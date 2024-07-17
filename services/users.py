from flask import Blueprint, config, request, render_template, redirect, url_for, flash
from config.db import pgsqlConn, sql

users = Blueprint('users', __name__, template_folder='app/templates/users')

@users.route('/users')
def Home():
    cur = pgsqlConn.cursor()
    columns = ("id", "firstname", "lastname", "email")
    stmt = sql.SQL('SELECT {} FROM {} LIMIT 5').format(
                sql.SQL(',').join(map(sql.Identifier, columns)),
                sql.Identifier('users')
            )
    cur.execute(stmt)
    usersAll = cur.fetchall()
    return render_template('users/users.html', users=usersAll)

@users.route('/users/new_user')
def NewUser():
    return render_template('users/new_user.html')

@users.route('/users/add_user', methods=['POST'])
def add_user():
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            password = request.form['password']
            try:
                cur = pgsqlConn.cursor()
                cur.execute(
                    "INSERT INTO users (firstname, lastname, email, password) VALUES (%s,%s,%s,%s)", (firstname, lastname, email, password))
                pgsqlConn.commit()
                flash('User Added successfully')
                return redirect(url_for('users.Home'))
            except Exception as e:
                flash(e.args[1])
                return redirect(url_for('users.Home'))

@users.route('/users/edit/<id>', methods=['POST', 'GET'])
def get_user(id):
    cur = pgsqlConn.cursor()
    cur.execute('SELECT * FROM users WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('users/edit_user.html', user=data[0])


@users.route('/users/update/<id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        cur = pgsqlConn.cursor()
        cur.execute("""
            UPDATE users
            SET firstname = %s,
                lastname = %s,
                email = %s
            WHERE id = %s
        """, (firstname, lastname, email, id))
        flash('User Updated Successfully')
        pgsqlConn.commit()
        return redirect(url_for('users.Home'))


@users.route('/users/delete/<string:id>', methods=['POST', 'GET'])
def delete_user(id):
    cur = pgsqlConn.cursor()
    cur.execute('DELETE FROM users WHERE id = {0}'.format(id))
    pgsqlConn.commit()
    flash('User Removed Successfully')
    return redirect(url_for('users.Home'))
