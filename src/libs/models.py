import email
from flask_sqlalchemy import SQLAlchemy
from configs.flask_config import APP

db = SQLAlchemy(APP)

class User_Model(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    ph_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    passwd = db.Column(db.String(50), nullable=False)
    re_passwd = db.Column(db.String(50), nullable=False)

    def json(self):
        return {'id': self.id, 'fname': self.fname, 'lname': self.lname, 'ph_no': self.ph_no, 'email':self.email, 'passwd':self.passwd, 're_passwd':self.re_passwd}

    def add_usr(_fname, _lname, _ph_no, _email, _passwd, _re_passwd):
        '''method to add User to database using parameters'''
        # creating an instance of our User constructor
        new_user = User_Model(fname= _fname, lname =_lname, ph_no =_ph_no, email=_email, passwd= _passwd, re_passwd=_re_passwd)
        db.session.add(new_user)  # add new emp to database session
        db.session.commit()  # commit changes to session

    def get_all_users():
        '''method to get all users in our database'''
        return [User_Model.json(user) for user in User_Model.query.all()]

    def get_user_by_id(_id):
        '''method to get user info using the id parameter'''
        return [User_Model.json(User_Model.query.filter_by(id=_id).first())]

    def update_user(_id, _fname, _lname, _ph_no, _email, _passwd, _re_passwd):
        '''method to update the details of a user using given parameters'''
        user_to_update = User_Model.query.filter_by(id=_id).first()
        user_to_update.fname = _fname
        user_to_update.lname = _lname
        user_to_update.ph_no = _ph_no
        user_to_update.email = _email
        user_to_update.passwd = _passwd
        user_to_update.re_passwd = _re_passwd
        db.session.commit()  # commiting the new change to our database

    def delete_user(_id):
        '''method to delete a user from our database using
           the id as a parameter'''
        User_Model.query.filter_by(id=_id).delete()
        # filter user by id and delete
        db.session.commit()  # commiting the new change to our database