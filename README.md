
# MongoDB CRUD Python Module

## Overview
The MongoDB CRUD Python module provides a convenient interface for performing basic CRUD (Create, Read, Update, Delete) operations on a MongoDB database using Python. It leverages the PyMongo library to interact with MongoDB, offering a simple yet powerful solution for managing data.

## Features
- **Create Document**: Add new documents to the MongoDB collection.
- **Read Document**: Retrieve documents from the collection based on specified criteria.
- **Update Document**: Modify existing documents in the collection.
- **Delete Document**: Remove documents from the collection.

## Usage
### Installation
Ensure that you have Python installed on your system. You can install the required dependencies using pip:
pip install pymongo


### Example Usage
```python
from MongoMiddle import mongoDriver

# Instantiate the mongoDriver class
driver = mongoDriver()

# Create a new document
data = {'_id': '123', 'name': 'Test Animal', 'type': 'Test Type'}
driver.createDocument(data)

# Read documents
result = driver.readDocument({'_id': '123'})

# Update documents
update_query = {'_id': '123'}
new_data = {'name': 'Updated Animal'}
driver.updateDocument(update_query, new_data)

# Delete documents
delete_query = {'_id': '123'}
driver.deleteDocument(delete_query)






