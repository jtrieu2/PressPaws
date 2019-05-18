from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_homepage():
    """Homepage."""

    print(session)
    return render_template("landing.html")


@app.route('/landing-login', methods=['GET'])
def landing_login_form():
    """Homepage."""

    return render_template("landing.html")

@app.route('/landing-login', methods=['POST'])
def landing_login_process():
	"""Homepage."""

	# Get form variables
	email = request.form['email']
	password = request.form['password']

	user = User.query.filter_by(email=email).first()

	if not user:
		print('no such user')
		return redirect("/")

	if user.password != password:
		flash("Incorrect password")
		return redirect("/")

	session["user_id"] = user.user_id
	session["fname"] = user.fname

	print("logged in")

	return render_template("landing.html")

@app.route('/landing-registration', methods=['GET'])
def registration_form():
    """Homepage."""

    return render_template("landing.html")

@app.route('/landing-registration', methods=['POST'])
def registration_process():
	"""Homepage."""

	# Get form variables
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	password = request.form['password']
	zipcode = request.form['zipcode']
	
	new_user = User(fname = fname, lname = lname, email=email, password=password, zipcode=zipcode)
	print('new user added')

	db.session.add(new_user)
	db.session.commit()


	return jsonify(email)

@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]

    print("Logged Out.")
    return redirect("/")

@app.route('/search')
def search():

	return render_template("search.html")





# @app.route('/register', methods=['GET'])
# def register_form():
#     """Show form for user signup."""

#     return render_template("register_form.html")


# @app.route('/register', methods=['POST'])
# def register_process():
#     """Process registration."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]
#     age = int(request.form["age"])
#     zipcode = request.form["zipcode"]

#     new_user = User(email=email, password=password, age=age, zipcode=zipcode)

#     db.session.add(new_user)
#     db.session.commit()

#     flash(f"User {email} added.")
#     return redirect("/")


# @app.route('/login', methods=['GET'])
# def login_form():
#     """Show login form."""

#     return render_template("login_form.html")


# @app.route('/login', methods=['POST'])
# def login_process():
#     """Process login."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]

#     user = User.query.filter_by(email=email).first()

#     if not user:
#         flash("No such user")
#         return redirect("/login")

#     if user.password != password:
#         flash("Incorrect password")
#         return redirect("/login")

#     session["user_id"] = user.user_id

#     flash("Logged in")
#     return redirect(f"/users/{user.user_id}")


# @app.route('/logout')
# def logout():
#     """Log out."""

#     del session["user_id"]
#     flash("Logged Out.")
#     return redirect("/")


# @app.route("/users")
# def user_list():
#     """Show list of users."""

#     users = User.query.all()
#     return render_template("user_list.html", users=users)






if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")