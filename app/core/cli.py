from hashlib import new
from flask import current_app
from app.auth.models import User



@current_app.cli.command('create_superuser')
def create_superuser():
    new_user = User()
    new_user.fname = 'Superuser'
    new_user.lname = 'Administrator'
    new_user.username = input("Enter username: ")
    new_user.set_password(input("Enter password: "))
    new_user.save()
    print("Superuser Created!")