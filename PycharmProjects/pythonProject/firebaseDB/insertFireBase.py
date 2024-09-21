from  firebase import firebase
firebase = firebase.FirebaseApplication('https://aaaa-ce739-default-rtdb.firebaseio.com', None)
data =  { 'Name': 'blsn',
          'RollNo': 7,
          'Percentage': 89.02
          }
result = firebase.post('student',data) # post() to insert into  db under student
print(result)


