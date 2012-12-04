from google.appengine.ext import db

class Person(db.Model):
    Firstname = db.StringProperty()
    Lastname = db.StringProperty()
