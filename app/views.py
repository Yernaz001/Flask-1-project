from flask import render_template, redirect, request
from app import app, db
from app.models import ItemsModel


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def getList():
    items=ItemsModel.query.all()
    return render_template('list.html',items=items)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
          return render_template('create.html')
    if request.method=='POST':
        supplier=request.form['supplier']
        name=request.form['name']
        quantity=request.form['quantity']
        price=request.form['price']

        items=ItemsModel(
            supplier=supplier,
            name=name,
            quantity=quantity,
            price=price
        )

        db.session.add(items)
        db.session.commit()

        return redirect('/')


@app.route('/<int:id>/edit',methods=['GET', 'POST'])
def update(id):
    items=ItemsModel.query.filter_by(id=id).first()

    if request.method=='POST':
        db.session.delete(items)
        db.session.commit()
        if items:
            supplier=request.form['supplier']
            name=request.form['name']
            quantity=request.form['quantity']
            price=request.form['price']

            items=ItemsModel(
                supplier=supplier,
                name=name,
                quantity=quantity,
                price=price
            )

            db.session.add(items)
            db.session.commit()
            return redirect('/')
        return f'Item with id ={id} does not exist'
    return render_template('update.html', items=items)


@app.route('/<int:id>/delete',methods=['GET', 'POST'])
def delete(id):
    dc = ItemsModel.query.get(id)
    db.session.delete(dc)
    db.session.commit()
    return redirect('/')
