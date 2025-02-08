# import pymongo

# client = pymongo.MongoClient('mongodb+srv://ineuron:Lenovo%40corei5@cluster0.ytxor.mongodb.net/?retryWrites=true&w=majority&appName=cluster0')
# db = client.test
# print(db)


# import pymongo
# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

# d = {
#     'name': 'SHubham',
#     'email' : 'sbarhate88@gmail.com',
#     'surname' : 'Barhate'
# }
#
# db1 = client['mongotest']
# coll = db1['test']
# coll.insert_one(d )



import pymongo

client = pymongo.MongoClient('mongodb+srv://sbarhate88:Lenovo%40corei5@cluster0.ytxor.mongodb.net/?retryWrites=true&w=majority&appName=cluster0')
# client = pymongo.MongoClient("mongodb+srv://ineuron:Lenovo%40corei5@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Shubham",
    "email" : "sbarate88@gmail.com",
    "surname" : "Barhate"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )