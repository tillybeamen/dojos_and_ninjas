from flask_app import app, redirect, session, render_template, request
# from flask_app import app
from flask_app.models.dojo import Dojo



@app.route('/')
def index():
    return redirect('/dojos')


#! CREATE
@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/create_dojo', methods = ['post'])
def create_dojo():
    data = {
        'name' : request.form['name']
        }
    
    Dojo.save(data)
    return redirect("/dojos")

#! READ

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojo(data)
    # print(dojo.ninjas)
    return render_template('show.html', dojo = dojo)

