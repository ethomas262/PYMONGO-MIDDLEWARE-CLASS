#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:15:34 2024

@author: elijahthomas1_snhu
"""
import unittest
from MongoMiddle import mongoDriver

class TestMongoDriver(unittest.TestCase):
    def setUp(self):
        # Mock MongoClient, database, and collection
        self.testClient = mongoDriver()
        dfresult = self.testClient.createDocument({'_id': '123','name': 'Test Animal', 'type': 'Test Type'})

    def test_createDocument(self):
        # Test createDocument method
        result = self.testClient.createDocument({'_id': '124','name': 'Test Animal', 'type': 'Test Type'})
        self.assertTrue(result)

    def test_readDocument(self):
        # Test getDocument method
        result = self.testClient.getDocument({'_id': 'A716330'})

        #assert that method returns a list
        self.assertIsInstance(result, list)

        #assert that method finds the document
        self.assertTrue( len(result) > 0)

    def test_updateDocument(self):
        # Test updateDocument method
        result = self.testClient.updDateDocument({'_id': '123'}, {'name': 'Updated Animal'})

        #assert that method returns and integer
        self.assertIsInstance(result, int)

        #assert that method has updated a document
        self.assertTrue(result > 0 and result != -1)

    def test_deleteDocument(self):
        # Test deleteDocument method
        result = self.testClient .deleteDocument({'_id': '123'})
        self.assertTrue(result)

    #method deletes created documents that were used in testing
    def tearDown(self):
        self.testClient.deleteDocument({'id': '123'})
        self.testClient.deleteDocument({'id': '124'})

if __name__ == '__main__':
    unittest.main()
