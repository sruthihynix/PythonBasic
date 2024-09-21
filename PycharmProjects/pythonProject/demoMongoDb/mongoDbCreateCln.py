from pymongo import MongoClient

# cars = [{'name': 'Audi', 'price': 52642},
#         {'name': 'Mercedes', 'price': 57127},
#         {'name': 'Skoda', 'price': 9000},
#         {'name': 'Volvo', 'price': 29000},
#         {'name': 'Bentley', 'price': 350000},
#         {'name': 'Citroen', 'price': 21000},
#         {'name': 'Hummer', 'price': 41400},
#         {'name': 'Volkswagen', 'price': 21600}]
#
client = MongoClient('mongodb://localhost:27017/')
# with client:
# db = client.testdb1
db = client.testdb1
# db-- reference to the testdb database.
# db.cars.drop()
# db.cars.insert_many(cars)
print("success")
# ---------------------------------find()-----------------------------------------
# cars=db.cars.find()
# for car in cars:
#     print('{0} {1}'.format(car['name'],
#         car['price']))
# ---------------------------------------------------------------
from pprint import pprint
status = db.command("serverStatus")
pprint(status)
