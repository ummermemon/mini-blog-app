from flask import Blueprint,render_template,request,jsonify,session,redirect,url_for
from app.forms.registration import RegistrationForm
from app.forms.login import LoginForm
from app.models.user import User
from app import db,bcrypt
from app.middlewares.auth import logout_required

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
@logout_required
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        user_exist = User.query.filter_by(email=email).first()
        if user_exist:
            form.email.errors.append('Email already registered.')
            return render_template('auth/signup.html', form=form)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(first_name=first_name,last_name=last_name,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        return redirect(url_for('panel.dashboard'))
    return render_template('auth/signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
@logout_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user:
            check_password = bcrypt.check_password_hash(user.password, password)
            if check_password:
                session['user_id'] = user.id
                return redirect(url_for('panel.dashboard'))
            else:
                form.password.errors.append('Incorrect Password')
                return render_template('auth/login.html', form=form)
        else:
            form.email.errors.append('User does not exist')
            return render_template('auth/login.html', form=form)
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))