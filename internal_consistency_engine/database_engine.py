import motor.motor_asyncio
# Connect to Mongo Server, create database, create collections, establish system credentials, save relevant information


class DatabaseEngine:
    def __init__(self, uri=None, values=None):

        if uri is None:
            self.__uri = "{PROTOCOL}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{HOST_PORT}/{DATABASE}"
        else:
            self.__uri = uri

        if values is None:
            self.__values = {
                "PROTOCOL": "mongodb",
                "USERNAME": "DEMO",
                "PASSWORD": "DEMO",
                "HOSTNAME": "127.0.0.1",
                "HOST_PORT": "27017",
                "DATABASE": "COHERENCY"
            }
        else:
            self.__values = values

        self.__engine = motor.motor_asyncio.AsyncIOMotorClient(self.__uri.format(**self.__values))

    def validate(self, msg=False):
        return self.__test_connection(uri=self.__uri, values=self.__values, msg=msg)

    def __test_connection(self, uri=None, values=None, msg=None):
        if uri is None:
            uri = self.__uri

        if values is None:
            values = self.__values

        return False

    def update_values(self, uri=None, values=None):
        if self.__test_connection(uri=uri, values=values):
            self.__uri = self.__uri if uri is None else uri
            self.__values = self.__values if values is None else values
            return True
        else:
            return False


class MongoEngine(DatabaseEngine):
    def __test_connection(self, uri=None, values=None, msg=False):
        uri = self.__uri if uri is None else uri
        values = self.__values if values is None else values

        try:
            _ = motor.motor_asyncio.AsyncIOMotorClient(uri.format(**values))
            result = True
            result_msg = "Success"
        except ConnectionError as e:
            result = False
            result_msg = e.strerror

        return result_msg if msg else result
