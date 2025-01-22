from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# Create a Blueprint for authentication routes using the imported Flask Blueprint class
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

# Query the user by email, if the user exists, check if the password is correct, if it is, log the user in, if not, flash an error message
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('veiws.home'))
            else:
                flash("Incorrect password, try again", category='error')
        else:
            flash("Email does not exist", category='error')
    # Render the login page
    return render_template("login.html", user=current_user)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        #checks if the email already exists, if the email is less than 4 characters, if the password is less than 6 characters, and if the two passwords entered match 
        if user:
            flash("Email already exists", category='error')
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(password1) < 6:
            flash("Password must be at least 6 characters", category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        else:
            # Create a new user with hashed password
            newUser = User(email=email, first_name=firstName, password= generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(newUser)
            db.session.commit()
            flash("Account created", category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/chats')
@login_required
def chats():
#render the chats
    return render_template("chats.html", user=current_user)

@auth.route('/courses')
@login_required
def courses():
    # Render the courses page
    return render_template("courses.html", user=current_user)