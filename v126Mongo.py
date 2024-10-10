import pymongo



# client = MongoClient('mongodb://localhost:27017/?directConnection=true')
connection = pymongo.MongoClient('mongodb://localhost:27017/?directConnection=true')

# result = client['PythonTosegar']['Users 👥'].aggregate([])
db = connection["PythonTosegar"]

collection = db['Users 👥']
dic = {"Name":"Khabat","Family":"Bardanoos"}
x = collection.insert_one(dic)


print(x)
