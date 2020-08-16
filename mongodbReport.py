from pymongo import MongoClient

client = MongoClient('mongodb://admin:4linux@192.168.100.10')

print(dir(client))

all_dbs = client.list_database_names()

mongo_dbs = ['admin','local','config']

dbs = list(set(all_dbs) - set(mongo_dbs))

for db in dbs:
  database = client[db]

  dbstats = database.command('dbstats')
  
  print(dbstats['db'])  
 
  for collection in database.list_collection_names():
    coll = database[collection]
    collstats = database.command('collstats',collection)
    print(collstats['totalIndexSize'])
    print(collstats['indexSizes'])
    
    






