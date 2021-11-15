from flask import render_template, request

from app.auth import authentication
from app.auth.forms import RegistrationForm


@authentication.route('/register', methods=['GET', 'POST'])
def register_user():
    name = None
    email = None
    form = RegistrationForm()

    if request.method == 'POST':
        name = form.name.data
        email = form.email.data

    return render_template('registration.html', form=form, name=name, email=email)
