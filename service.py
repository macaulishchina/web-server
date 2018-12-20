from dao import User,Function,StreamService,db


class Service:
    def register(self, username, password, authority=0, key=""):
        pass

    def login(self, username, password):
        pass

    def deleteAllUsers(self, operator):
        pass

    def deleteUser(self, username, operator):
        pass

    def updateUser(self, username, password, operator):
        pass

    def queryAllUsers(self, operator):
        pass

    def queryUser(self, username,operator):
        pass

    def addFunction(self, name, capacity, operator):
        pass

    def deleteAllFunctions(self, operator):
        pass

    def deleteFunction(self, name, operator):
        pass

    def updateFunction(self, name, capacity, operator):
        pass

    def queryAllFunctions(self,operator):
        pass

    def addStreamService(self, source_url, function_name, ss_name, description, operator):
        pass

    def deleteAllSS(self, operator):
        pass

    def deleteStreamService(self, ss_guid, operator):
        pass

    def updateStreamService(self, ss_guid, source_url, function_guid, operator):
        pass

    def queryAllSS(self,operator):
        pass

    def queryStreamService(self, ss_guid='*',source_url='*',function_guid='*'):
        pass


