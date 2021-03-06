#Amanda Zheng, Yevgeniy Gorbachev (downgraded-octo-waffle)
#SoftDev1 pd1
#K09 -- Yummy Mongo Py
#2020-02-26


from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient("localhost",27017)
food = client.restaurants.food
food.drop()

file = open("dataset.json", "r")
doc = file.readlines()
print(doc[0])
for x in doc:
    food.insert_one(loads(x))


def findBorough(bor):
    return food.find( { "borough": bor },{ "name": 1,"_id":0} )

def findzip(zipc):
    return food.find( { "address.zipcode": zipc },{ "name": 1,"_id":0} )

def findzipgrade(zipc,grade):
    return food.find( { "address.zipcode": zipc, "grades.grade": grade },{ "name": 1, "_id":0} )

def findzipthresh(zipc,score):
    return food.find( { "address.zipcode": zipc, "grades.score": {"$lt":score}},{ "name": 1,"_id":0} )

def findsubName(name):
    name=".*"+name+".*"
    return food.find({"name": {"$regex":name,"$options":"i"}},{"name":1,"_id":0})



print("\nPrinting results for Restaurants in Queens\n")

for result in findBorough("Queens"):
    if(result["name"]==""):
       print("No Name Found")
    else:
       print(result["name"])

print("\nprinting results for Restaurants with zipcode 11377\n")
for result in findzip("11377"):
    if (result["name"]==""):
        print("No Name Found")
    else:
       print(result["name"])


print("\nprinting results for Restaurants with zipcode 11377 and grade B\n")

for result in findzipgrade("11377","B"):
    if (result["name"]==""):
        print("No Name Found")
    else:   
      print (result["name"])

print("\nprinting results for Restaurants with zipcode 11377 and score of less than 50")

for result in findzipthresh("11377",50):
    if(result["name"]==""):
        print("No Name Found")
    else:
      print(result["name"])

print("\nprinting results for Restaurants with the word pizza in its name\n")
for result in findsubName("pizza"):
   print(result["name"])
