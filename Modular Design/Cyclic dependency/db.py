from init import Initialization


class DB:
    def __init__(self):
        self.DB = None

    def setupDB(self):
        print('Creating database...')
        self.DB = {}
        init = Initialization()
        self.DB = init.loadData(DB)

"""
in a simple way, we can break the cyclic dependency between these three modules by extracting another module, appropriately named validator.

class Validator: 
    def runTest(self, DB): 
        print('Checking if app is ready...') 
        if 'Users' in DB.keys(): 
            return True 
        else: 
            return False
"""