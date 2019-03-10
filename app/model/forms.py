from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, EqualTo
from app.model.models import User

# small invalid length validator


def length(min_len=0, max_len=10, message=None):
    if not message:
        message = 'Must be between {} and {} characters'.format(min_len, max_len)

    def _length(form, field):
        i = field.data and len(field.data) or 0
        if i < min_len or i > max_len:
            raise ValidationError(message)

    return _length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Regexp('([0-9]+)+', message='Must match pattern'), length(2, 8, "Custom invalid length message")
    ])
    password = PasswordField('Password',  validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Regexp('([0-9]+)+', message='Must match pattern'), length(2, 8, "Custom invalid length message")
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):  # validate_<field_name> --> WTForms adds this method as a validator to field
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is already taken. Please choose another one!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is already taken. Please use another adress!')

