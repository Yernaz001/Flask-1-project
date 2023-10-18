from flask import render_template, redirect, request
from app import app, db
from app.models import ItemsModel, CategoriesModel


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def getList():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    sort_field = request.args.get('sort_field', 'id')
    sort_order = request.args.get('sort_order', 'asc')

    valid_sort_fields = ['id', 'name', 'quantity', 'price']

    if sort_field not in valid_sort_fields:
        sort_field = 'id' 

    query = ItemsModel.query
    
    if sort_field == 'id':
        if sort_order == 'asc':
             query = query.order_by(ItemsModel.id.asc())
        else:
             query = query.order_by(ItemsModel.id.desc())
    elif sort_field == 'name':
        if sort_order == 'asc':
             query = query.order_by(ItemsModel.name.asc())
        else:
             query = query.order_by(ItemsModel.name.desc())
    elif sort_field == 'quantity':
        if sort_order == 'asc':
             query = query.order_by(ItemsModel.quantity.asc())
        else:
             query = query.order_by(ItemsModel.quantity.desc())
    elif sort_field == 'price':
        if sort_order == 'asc':
             query = query.order_by(ItemsModel.price.asc())
        else:
             query = query.order_by(ItemsModel.price.desc())
        
    items = query.paginate(page, per_page, False)


    return render_template('list.html', items=items)


@app.route('/list-category')
def getListCategory():
    categories = CategoriesModel.query.all()

    if not categories:
        message = "No categories found in the database."
        return render_template('category.html', message=message)

    return render_template('category.html', categories=categories)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        categories = CategoriesModel.query.all()
        return render_template('create.html', categories=categories)
    if request.method == 'POST':
        supplier = request.form['supplier']
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        category_id = request.form['category'] 

        if category_id == 'new':
            new_category_name = request.form['new-category-name']
            existing_category = CategoriesModel.query.filter_by(name=new_category_name).first()
            if existing_category:
                category_id = existing_category.id
            else:
                new_category = CategoriesModel(name=new_category_name)
                db.session.add(new_category)
                db.session.commit()
                category_id = new_category.id

        items = ItemsModel(
            supplier=supplier,
            name=name,
            quantity=quantity,
            price=price,
            category_id=category_id
        )

        db.session.add(items)
        db.session.commit()

        return redirect('/')


@app.route('/<int:id>/edit',methods=['GET','POST'])
def update(id):
    items = ItemsModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        
        supplier = request.form['supplier']
        name = request.form['name']
        quantity=request.form['quantity']
        price=request.form['price']

        items.supplier=supplier
        items.name=name
        items.quantity=quantity
        items.price=price
        db.session.commit()
        return redirect("/")
        
    return render_template('update.html', items=items)


@app.route('/<int:id>/delete',methods=['GET', 'POST'])
def delete(id):
    dc = ItemsModel.query.get(id)
    db.session.delete(dc)
    db.session.commit()
    return redirect('/')
