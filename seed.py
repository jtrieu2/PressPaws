from sqlalchemy import func

from model import User, Avatar, connect_to_db, db
from server import app

import pandas as pd 

default_url = 'https://images.unsplash.com/photo-1537151672256-6caf2e9f8c95?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=ipet-photo-1061142-unsplash.jpg'

def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()

def load_avatars(filename):

    df = pd.read_excel(filename)
    avatar_list = list(df['Name'])

    for url in avatar_list:
        avatar = Avatar(url=url)

        db.session.add(avatar)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    excel_file = 'avatars.xlsx'
    load_avatars(excel_file)

    user = User(user_id=1,fname='Jenny',lname='Trieu',email='jennytrieu10@gmail.com', password="evil", url = default_url)
    db.session.add(user)
    db.session.commit()
    set_val_user_id()


  