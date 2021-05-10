import pymongo

def connectDB():
  try:
    #Connect to the database
    dbclient = pymongo.MongoClient("mongodb+srv://loc:123457@locdbv1.lpjrx.mongodb.net/LOCDBV1?retryWrites=true&w=majority")

    database = dbclient.LOC_V1_DS

    if(len(database.list_collection_names()) > 0) :
      pass
    else:
      database.create_collection("Users")
  except:
    raise Exception("error connecting to the database")
  
  return database.Users


  