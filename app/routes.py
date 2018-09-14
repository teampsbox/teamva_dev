from flask import render_template, redirect
from app import app, db
from app.forms import ClientForm
from app.models import Va, Client


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ClientForm()
    va_keira = Va.query.get(1).username
    if form.validate_on_submit():
        client = Client(first_name=form.first_name.data, last_name=form.last_name.data, va=va_keira)
        db.session.add(client)
        db.session.commit()
    return render_template('home.html', form=form)
