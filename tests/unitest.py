import unittest 

def add (a,b) : 
    return a+b 

class TestAPI(unitest.TestCase) : 
    def test_add(self) : 
        result = add(3, 2)
        self.assertEqual(result, 5)


