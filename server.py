from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Avatar, Place, Event

from eventbrite import get_eventbrite_details, get_event_details
import os
import random
import requests

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined
registration_elements = ['fname','lname','email','password','zipcode'];
registration_titles = ['First Name', 'Last Name','Email', 'Password','Zipcode']
login_elements = ['email','password']
login_titles = ['Email','Password']

events_list = [];

@app.route('/')
def show_homepage():
    """Homepage."""
    [events,event_ids] = get_eventbrite_details(city = 'New York', num_events = 8)

    return render_template("landing.html", events = events,
									    	registration_elements = registration_elements,
									    	registration_titles = registration_titles,
									    	login_elements = login_elements,
									    	login_titles = login_titles, 
									    	event_ids = event_ids)

@app.route('/landing-login', methods=['GET','POST'])
def landing_login_process():
	"""Login Process"""

	# Get form variables
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		user = User.query.filter_by(email=email).first()

		if not user:
			flash('no such user')
			return jsonify({'error':'no such user'})
			# do something on javascript

		if user and user.password != password:
			flash("Incorrect password")
			# return redirect("/")

		if user and user.password == password:
			session["user_id"] = user.user_id
			session["fname"] = user.fname

	print("logged in")

	[events, event_ids] = get_eventbrite_details(city = 'New York', num_events = 8)
	return render_template("landing.html", events = events,
											 registration_elements = registration_elements,
											 registration_titles = registration_titles,
											 login_elements = login_elements,
											 login_titles = login_titles,
											 event_ids = event_ids)

@app.route('/landing-registration', methods=['GET','POST'])
def registration_process():
	"""Homepage."""

	if request.method == 'POST':
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

	[events, event_ids] = get_eventbrite_details(city = 'New York', num_events = 8)

	return render_template("landing.html", events = events,
											 registration_titles = registration_titles,
											 registration_elements = registration_elements,
											 login_elements = login_elements,
											 login_titles = login_titles,
											 event_ids = event_ids)

@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]

    print("Logged Out.")
    return redirect("/")

@app.route('/search')
def search():

	return render_template("search.html")

@app.route('/search.json')
def get_favorites():

	user_id = session["user_id"]
	# get the list of places saved by the user
	saved_places_list = User.query.get(user_id).places
	saved_events_list = User.query.get(user_id).events

	store_names = []
	events = []

	for place in saved_places_list:
		store_names.append(place.place_name)

	for event in saved_events_list:
		events.append(event.eventbrite_id)

	saved_data = {'places': store_names,
					'events': events }

	print(saved_data)

	return jsonify(saved_data)


@app.route('/profile')
def profile():

	if session.get('user_id',0) != 0:
		user_id = session['user_id']

	user = User.query.filter_by(user_id=user_id).first();

	# grab all places from the database and display to users profile page
	places = Place.query.all()
	events = Event.query.all()
	print(places)
	print(events)
	return render_template("profile.html", user=user, places = places, events = events)

@app.route('/profile-change-avatar')
def change_avatar():

	rand_num = random.randint(1,17)
	selected_avatar = Avatar.query.get(rand_num)
	selected_url = selected_avatar.url

	user_id = session["user_id"];
	user = User.query.get(user_id);
	user.url = selected_url
	db.session.commit()
	print('committed new profile pic')
	return selected_url


@app.route('/grab-data-from-frontend', methods=['POST'])
def showdata():

	if session.get('user_id',0) != 0:
		user_id = session['user_id']

	if request.form.get("store_name"):
		place_name = request.form.get("store_name")
		place_address = request.form.get("store_address")
		place_photo = request.form.get("store_photo")
		check_status = request.form.get("check_status")

		# check for an existing place
		place = Place.query.filter_by(user_id=user_id, place_name=place_name).first()
		
		if check_status:
			if not place:
				new_place = Place(user_id = user_id, place_name=place_name, place_address=place_address, place_imURL = place_photo)
				print('add place to database')
				db.session.add(new_place)
				print('added to database')

		if check_status=='false':
			Place.query.filter_by(user_id = user_id, place_name=place_name).delete()
			print('database entry deleted')

		db.session.commit()

	if request.form.get("event_id"):
		event_id = request.form.get("event_id")
		db_action = request.form.get("database_action")
		event_info = get_event_details(event_id)

		if db_action == 'add':
			new_event = Event(user_id = user_id, eventbrite_id = event_info['event_id'], event_name = event_info['event_name'], event_address = event_info['event_address'],
								event_date = event_info['event_date'], event_imURL = event_info['event_image'])
			db.session.add(new_event)
			print('added to database')
		else:
			Event.query.filter_by(user_id = user_id, event_name=event_info['event_name']).delete()
			print('database entry deleted')

	db.session.commit()

	return 'helllo'

@app.route('/events-search', methods =['GET','POST'])
def showevents_process():

	num_events = 20
	if  request.method == 'GET':
		[events, event_ids] = get_eventbrite_details(city = 'San Francisco', num_events = num_events)
		return render_template("events.html", events_list = events,
											 num_events = num_events,
											 event_ids = event_ids,
											 login_elements = login_elements,
											 login_titles = login_titles, 
											 registration_elements = registration_elements,
											 registration_titles = registration_titles)
	else:
		[events, event_ids] = get_eventbrite_details(city = request.form.get('city'), num_events = num_events)
		return render_template("events.html", events_list = events,
											  num_events = num_events,
											  event_ids = event_ids,
											  login_elements = login_elements,
											  login_titles = login_titles, 
											  registration_elements = registration_elements,
											  registration_titles = registration_titles)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")