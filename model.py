"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String(64), nullable=True)
    lname = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)
    url = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} email={self.email}>"

class Avatar(db.Model):

    __tablename__ = "avatars"

    avatar_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    url = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Avatar avatar_id={self.avatar_id} url={self.url}>"

class Place(db.Model):

    __tablename__ = "places"

    place_id = db.Column(db.Integer, 
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    place_name = db.Column(db.String(300))
    place_address = db.Column(db.String(500))
    place_imURL = db.Column(db.String(1000))

    user = db.relationship("User", 
                            backref=db.backref("places", 
                                               order_by=place_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Place place_id={self.place_id} place_name={self.place_name}>"

class Event(db.Model):

    __tablename__ = "events"

    event_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    eventbrite_id = db.Column(db.String(500))
    event_name = db.Column(db.String(300))
    event_address = db.Column(db.String(500))
    event_date = db.Column(db.String(100))
    event_imURL = db.Column(db.String(1000))

    user = db.relationship("User", 
                        backref=db.backref("events", 
                                           order_by=event_id))



#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///projectpaws'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
