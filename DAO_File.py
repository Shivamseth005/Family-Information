import json
# import jsonschema

class FileDaoClass(object):
    _instance = None
    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = super(FileDaoClass, cls).__new__(cls)
        return cls._instance

    def setFilePath(self, filePath):
        self.filePath = filePath
        self.dataSource = {}

    def loadDataSource(self):
        self.dataSource = json.load(open(self.filePath))

    def printDataSource(self):
        print(json.dumps(self.dataSource, indent=4))

    def getDataSourceDump(self):
        return self.dataSource

    def validateJson(self):
        pass
