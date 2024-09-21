from  firebase import  firebase

firebase=firebase.FirebaseApplication('https://aaaa-ce739-default-rtdb.firebaseio.com',None)
result=firebase.get('student','')
print(result)