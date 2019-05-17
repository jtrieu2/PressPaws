from sqlalchemy import func

from model import User, connect_to_db, db
from server import app

def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()


    # Mimic what we did in the interpreter, and add the Eye and some ratings
    user = User(user_id=1,fname='Jenny',lname='Trieu',email='jennytrieu10@gmail.com', password="evil")
    db.session.add(user)
    db.session.commit()
    set_val_user_id()


  