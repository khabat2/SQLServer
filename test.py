
import pymongo

connection = pymongo.MongoClient('mongodb://localhost:27017/?directConnection=true')

DataBase = connection["PythonTosegar"]
collection = DataBase['Users']


def Create(dic):
    collection.insert_one(dic)
    return True

def Read(item):
    result = collection.find_one(item)
    if result:
        print(result)
        return result
    else:
        print("result not found")

def Update(oldDic, newDic):
    collection.update_one(oldDic, {"$set": newDic})

def Delete(item):
    result = collection.delete_one(item)
    return True

dic = {"Name": "Rasul", "Family": "Noorani"}
newDic = {"Name": "Ahmad", "Family": "Sohrabi"}

Create(dic)
Delete(dic)
Read(dic)
Update(dic, newDic)

Update({"user.Info1.Name": "Milad"}, {"user.Info1.Name": "میلاد"})
