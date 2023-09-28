from flask import Flask, redirect, jsonify, render_template, request, json, session

from config.bd import app, db
from modelos.Articulos import Articulos, ArticuloSchema
from modelos.User import User, UserSchema

articulo_schema = ArticuloSchema()
articulos_schema = ArticuloSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/', methods = ['GET'])
def index():
    
    return render_template("login.html")


@app.route('/ingresar', methods = ['POST'])
def ingresar():
    
    email = request.form['email']
    password = request.form['password']
    user = db.session.query(User.id).filter(User.email == email, User.password == password).all()
    resultado = users_schema.dump(user)

    if len(resultado)>0:
        session['email'] = email
        return redirect('/larticulos.html')
    else:
        return redirect('/')
    
@app.route('/larticulos', methods = ['GET'])
def larticulos():
    if 'usuario' in session:
        return render_template("larticulos.html", usuario = session['usuario'])
    else:
        return redirect ('/')


@app.route('/cerrar')
def cerrar():
    session.pop('usuario', None)
    return redirect ('/')

    
if __name__ == "__main__":
    app.run(debug=True)