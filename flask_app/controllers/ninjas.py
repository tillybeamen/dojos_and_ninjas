from flask_app import app, render_template, redirect, request 
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo





@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = Dojo.get_all())


#! CREATE

@app.route('/create_ninjas', methods=['post'])
def create_ninjas():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form ['age'],
        'dojo_id' : request.form ['dojo_id']
        }
    # print(request.form)
    Ninja.save(data)
    return redirect(f"/dojos/{request.form['dojo_id']}")
    


