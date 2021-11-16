from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already exists')


class RegistrationForm(FlaskForm):
    name = StringField('Enter your name', validators=[DataRequired(),
                                                      Length(3, 15, 'must be between 3 and 15 characters')])
    email = StringField('Enter your email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 15, 'must be between 8 and 15 '
                                                                                   'characters'),
                                                     EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged in')
    submit = SubmitField('Log In')
