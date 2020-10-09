from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

app = create_app()

with app.app_context():
    username = input("Write here username")
    
    if User.query.filter(User.username == username).count():
        print("This user is already exist")
        sys.exit()
    
    password1 = getpass("Write here your password")    
    password2 = getpass("Write here your password again")
    
    if not password1 == password2:
        print("Passwords are not same")
        sys.exit() 
        
    new_user = User(username=username, role='admin')
    new_user.set_password(password1)
    
    
    db.session.add(new_user)
    db.session.commit()
    print("New user is created, id = {}".format(new_user.id))