from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Avatar, Place, Event

from eventbrite import get_eventbrite_details, get_event_details

from sendgrid_helper import send_email, send_batch_shelters_email, send_batch_events_email

import os, json, random, requests

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

    session["login_elements"] = login_elements
    session["login_titles"] = login_titles
    session["registration_elements"] = registration_elements
    session["registration_titles"] = registration_titles
    session["current_page"] = '/'
        # [events, event_ids] = get_eventbrite_details(city = 'San Francisco', num_events = 8)
    events = []
    event_ids = []

    if session.get('user_id',0):
    	print(session['user_id'])


    return render_template("landing.html", events = events, event_ids = event_ids)

@app.route('/landing-login', methods=['GET','POST'])
def landing_login_process():
	"""Login Process"""

	# If a user logs in (not with the demo account)
	if request.method == 'POST' and not request.form.get('clicked'):
		# Get form variables
		email = request.form['email']
		password = request.form['password']

		user = User.query.filter_by(email=email).first()

		# If no user exists or if the password does not
		# match with the registered username, redirect to homepage.
		if not user or user and user.password != password:
			return redirect('/')

		# If user login is successful, update session variables.
		if user and user.password == password:
			session["user_id"] = user.user_id
			session["fname"] = user.fname	

	# If user clicks on demo account button
	elif request.form.get('clicked') == 'yes':
		user = User.query.get(1)
		session['user_id'] = user.user_id
		session['fname'] = user.fname
		session['demo'] = 'active'

	# Grab eventbrite details to display on homepage
	# [events, event_ids] = get_eventbrite_details(city = 'New York', num_events = 8)

	# return render_template("landing.html", events = events)
	return redirect(session['current_page'])

@app.route('/landing-registration', methods=['GET','POST'])
def registration_process():
	"""Registration Process."""

	# Get form variables
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	password = request.form['password']
	zipcode = request.form['zipcode']
	
	# Create new user
	new_user = User(fname = fname, lname = lname, email=email, password=password, zipcode=zipcode)

	# Add new user to the database
	db.session.add(new_user)
	db.session.commit()

	# [events, event_ids] = get_eventbrite_details(city = 'New York', num_events = 8)

	# return render_template("landing.html", events = events, event_ids = event_ids)
	return redirect(session['current_page'])

@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    if session.get('demo',0):
    	del session['demo']

    if session['current_page'] == '/profile':
    	return redirect('/')
    else:
    	return redirect(session['current_page'])

@app.route('/search')
def search():
	"""Dog Adoption Shelters Page."""

	session['current_page'] = '/search'
	return render_template("search.html")

@app.route('/search.json')
def get_favorites():
	"""Search in the database to find bookmarked shelters
	and events in order to indicate these bookmarks on
 	the appropriate pages."""

   	# Get the id of the user currently signed in.
	if session.get('user_id',0) != 0:
		user_id = session['user_id']

		# Get the list of places and events saved by the user
		saved_places_list = User.query.get(user_id).places
		saved_events_list = User.query.get(user_id).events

		# Format the bookmarked data in json format for the frontend to render
		store_names = []
		events = []

		for place in saved_places_list:
			store_names.append(place.place_name)

		for event in saved_events_list:
			events.append(event.eventbrite_id)

		saved_data = {'places': store_names, 'events': events }

		return jsonify(saved_data)
	else:
		return redirect('/events-search')

@app.route('/profile')
def profile():
	"""User Profile Page"""
	session['current_page'] = '/profile'

	if session.get('user_id',0) != 0:
		user_id = session['user_id']

		user = User.query.filter_by(user_id=user_id).first();

		# Get all bookmarked data from database to display on profile page.
		places = user.places
		events = user.events

		# Reformat the stringified array representing the business hours from the database.
		for place in places:
			if place.place_hours:
				place.place_hours = json.loads(place.place_hours)

		return render_template("profile.html", user=user, places = places, events = events)
	else: 
		return redirect('/')

@app.route('/profile-change-avatar')
def change_avatar():
	"""Method allowing the user to change
	the profile picture and to store the
	change to the database"""

	# Randomly select a number from 1-17 that represents that id of the Avatar images
	selected_avatar = Avatar.query.get(random.randint(1,17))
	selected_url = selected_avatar.url

	# Get the current user's profile picture and reassign the value
	user = User.query.get(session["user_id"])
	user.url = selected_url
	db.session.commit()

	return selected_url


@app.route('/grab-data-from-frontend', methods=['POST'])
def showdata():
	"""Method that takes into account user activity
	of bookmarks of events and shelters on the frontend
	and adjusts database accordingly."""

	# Get the currently logged in user id
	if session.get('user_id',0) != 0:
		user_id = session['user_id']

	# If the user has clicked on a shelter, get the general business 
	# information of the shelter and add or delete the entry from the db 
	# depending on the check_status flag variable
	if request.form.get("store_name"):
		place_name = request.form.get("store_name")
		place_address = request.form.get("store_address")
		place_photo = request.form.get("store_photo")
		place_website = request.form.get("business_website")
		place_hours = request.form.get("business_hours")
		check_status = request.form.get("check_status")

		place = Place.query.filter_by(user_id=user_id, place_name=place_name).first()
		
		if check_status:
			if not place:
				new_place = Place(user_id = user_id, place_name=place_name, place_address=place_address,
									 place_imURL = place_photo, place_website = place_website, place_hours = place_hours)
				db.session.add(new_place)

		if check_status=='false':
			Place.query.filter_by(user_id = user_id, place_name=place_name).delete()

		db.session.commit()

	# If the user has clicked on an event, get the event id and then add
	# or delete from the database depending on the db_action flag variable
	if request.form.get("event_id"):
		event_id = request.form.get("event_id")
		db_action = request.form.get("database_action")
		event_info = get_event_details(event_id)

		if db_action == 'add':
			new_event = Event(user_id = user_id, eventbrite_id = event_info['event_id'], event_name = event_info['event_name'], event_address = event_info['event_address'],
								event_date = event_info['event_date'], event_imURL = event_info['event_image'], event_website = event_info['eventbrite_url'])
			db.session.add(new_event)
		else:
			Event.query.filter_by(user_id = user_id, event_name=event_info['event_name']).delete()

	db.session.commit()

	return 'None'

@app.route('/events-search', methods =['GET','POST'])
def showevents_process():
	"""Events Listing Page. Page defaults to events listed in SF but also
	allows user to search for events in other cities too."""

	# Default events page
	if  request.method == 'GET':
		session['city'] = 'San Francisco'
		[events, event_ids] = get_eventbrite_details(city = 'San Francisco', num_events = 20)
		return render_template("events.html", events_list = events, num_events = 20, event_ids = event_ids)
	else:
	# Render new events page depending on user input
		session['city'] = request.form.get('city')
		[events, event_ids] = get_eventbrite_details(city = request.form.get('city'), num_events = 20)
		return render_template("events.html", events_list = events, num_events = 20, event_ids = event_ids)

@app.route('/share-event', methods = ['POST'])
def share_events():
	"""Send email method on events listing page.
	Allows users to share event details of a particular 
	event to another user via email."""

	# Get form variables: from and to email addresses and event information
	user_email = request.form['user_email']
	recipient_email = request.form['recipient_email']
	event_id = request.form['event_id']
	event_info = get_event_details(event_id)

	# Send email function imported from sendgrid_helper.py
	send_email(user_email, recipient_email, event_info)

	return redirect('/events-search')

@app.route('/share-favorite-shelters', methods = ['POST'])
def share_batch_shelters():
	"""Send email method from profile.
	Allows users to share all bookmarked places in one email."""

	# Get form variables: from and to email addresses and event information.
	user_email = request.form['user_email']
	recipient_email = request.form['recipient_email']

	# Query data base for currently logged in user and obtain user's saved shelters list
	user = User.query.get(session['user_id'])
	places = user.places

	for place in places:
		if place.place_hours:
			place.place_hours = json.loads(place.place_hours)

	# Send email function imported from sendgrid_helper.py
	send_batch_shelters_email(user_email, recipient_email, places)

	return redirect('/profile')

@app.route('/share-favorite-events', methods = ['GET','POST'])
def share_batch_events():
	"""Send email method from profile.
	Allows users to share all bookmarked events in one email."""

	# Get form variables: from and to email addresses and event information.
	user_email = request.form['user_email']
	recipient_email = request.form['recipient_email']

	# Query data base for currently logged in user and obtain user's saved shelters list
	user = User.query.get(session['user_id'])
	events = user.events

	send_batch_events_email(user_email, recipient_email, events)

	return redirect('/profile')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")