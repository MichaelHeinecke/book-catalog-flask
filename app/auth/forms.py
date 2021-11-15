from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Enter your name', validators=[DataRequired(),
                                                      Length(3, 15, 'must be between 3 and 15 characters')])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 15, 'must be between 8 and 15 '
                                                                                   'characters'),
                                                     EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
