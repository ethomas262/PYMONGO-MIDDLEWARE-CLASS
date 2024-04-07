from pymongo import MongoClient

class mongoDriver:
    def __init__(self): #Constructor with static values to spin up new db client
        
        #declare variables and credentials for connecting to database
        user = "sampleUsername"
        password = 'samplePassword'
        host = 'address.domain.com'
        db = 'DATABASE'
        collection = 'testCollection'
        port = 32410

        #create client for CRUD functionality
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,password,host,port))

        #assign db collection to use
        self.db = self.client[db]
        self.collection = self.db[collection]

    def createDocument(self, inputData): #Method for creating a new document in database

        #If data is valid
        if inputData:

            #Try creating Document returning true if document is created and false if it failes
            try:
                self.collection.insert_one(inputData)
                return True
            except Exception as e:
                return False
        else:
            raise Exception("Nothing to save, invalid input")
            
    def readDocument(self, query):
        #if query is valid
        if query:

            #query database and return a list of all matching documents
            try:
                result = list(self.collection.find(query))
                return result
            
            #return an empty list if anything goes wrong
            except Exception as e:
                return []
            
        else:
            raise Exception("No data input")
        

    def updateDocument(self, query, newData):
        #if query and newData are valid
        if query and newData:
            
            #update database documents that match the query
            try:
                result = self.collection.update_many(query, {'$set': newData})
                
                return result.modified_count #return number of edited documents
            
            #return -1 if anything goes wrong
            except Exception as e:
                print(e)
                return -1
        else:
            raise Exception("INVALID INPUT")

    def deleteDocument(self, query):
        #if query is valid
        if query:
            #delete all documents that match query
            try:
                result = self.collection.delete_many(query)
                
                return result.deleted_count #return number of deleted documents
            
            #return -1 if anything goes wrong
            except Exception as e:
                print(e)
                return -1 
        else:
            raise Exception("ERROR: INVALID INPUT")
        
        
            
