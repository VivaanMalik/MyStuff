from firebase_admin import credentials
import pyrebase
import re
import firebase_admin 
from firebase_admin import auth as au
import requests

class auth:
    def __init__(self):
        self.config = {"apiKey": "AIzaSyBYLeFyqf9YBC4RWcuqKkfCnVMuE6h6Sno","authDomain": "tower-game-ss.firebaseapp.com","databaseURL": "https://tower-game-ss-default-rtdb.firebaseio.com/","storageBucket": "tower-game-ss.appspot.com","serviceAccount": "cred.json"}
        self.firebase = pyrebase.initialize_app(self.config)
        cred = credentials.Certificate('cred.json')
        self.adminsdk = firebase_admin.initialize_app(cred)
        self.db=self.firebase.database()
        self.auth=self.firebase.auth()
        self.user=None

    def create_account(self, username, email, password, passwordverify):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # regex for if email starts with [letter/num] + 0-1 dots + [letter/num] + @ + [word] + . + 2-3 char thing (in, com)
        if(re.search(regex,email)):   
            status='OK'
        else:   
            status = 'INVALID_EMAIL'
            return status

        if password==passwordverify and len(password)>=8 and len(password)<=64:
            status='OK'
        elif password!=passwordverify:
            status='PASSWORD_NO_MATCH'
            return status
        elif len(password)<8:
            status='PASSWORD_TOO_SHORT'
            return status
        elif len(password)>64:
            status='PASSWORD_TOO_LONG'
            return status
        else:
            status='UNKNOWN_ERROR'
            return status

        tmp_data={'name':username, 'coins':0, 'gems':0}
        self.user= au.create_user(email=email, email_verified=True, password=password, display_name=username, photo_url='http://www.example.com/12345678/photo.png')
        self.user = self.auth.sign_in_with_email_and_password(email, password)
        self.email=email
        self.db.child('user_data').child(self.user['localId']).set(tmp_data)
        return 'OK'

    def sign_in(self, email, password):
        try:
            self.user = self.auth.sign_in_with_email_and_password(email, password)
            self.email=email
            return 'OK', self.user
        except:
            return 'PASS/EMAIL_INCORRECT', None

    def reset_pass(self, password, passwordverify):
        if self.user==None:
            return 'ANONYMOUS_USER'
        elif self.email==None:
            return 'NO_EMAIL'

        if password==passwordverify and len(password)>=8 and len(password)<=64:
            status='OK'
        elif password!=passwordverify:
            status='PASSWORD_NO_MATCH'
            return status
        elif len(password)<8:
            status='PASSWORD_TOO_SHORT'
            return status
        elif len(password)>64:
            status='PASSWORD_TOO_LONG'
            return status
        else:
            status='UNKNOWN_ERROR'
            return status

        self.user= au.update_user(self.user['localId'], email=self.email, email_verified=True, password=password, display_name=self.db.child('user_data').child(self.user['localId']).get().val()['name'], photo_url='http://www.example.com/12345678/photo.png')
        return 'OK'

class data:
    def __init__(self):
        self.config = {"apiKey": "AIzaSyBYLeFyqf9YBC4RWcuqKkfCnVMuE6h6Sno","authDomain": "tower-game-ss.firebaseapp.com","databaseURL": "https://tower-game-ss-default-rtdb.firebaseio.com/","storageBucket": "tower-game-ss.appspot.com","serviceAccount": "cred.json"}
        self.firebase = pyrebase.initialize_app(self.config)
        self.db=self.firebase.database()