from flask import render_template, flash, url_for, redirect

from app.auth import authentication
from app.auth.forms import RegistrationForm
from app.auth.models import User


@authentication.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():  # check if POST request and invoke validators specified in form
        User.create_user(
            user=form.name.data,
            email=form.name.data,
            password=form.password.data
        )
        flash('Registration successful')
        return redirect(url_for('at.login_user'))

    return render_template('registration.html', form=form)
