from flask import render_template, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user

from app.auth import authentication
from app.auth.forms import RegistrationForm, LoginForm
from app.auth.models import User


@authentication.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    if form.validate_on_submit():  # check if POST request and invoke validators specified in form
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registration successful')
        return redirect(url_for('authentication.login'))

    return render_template('registration.html', form=form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()

        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html', form=form)


@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.display_books'))
