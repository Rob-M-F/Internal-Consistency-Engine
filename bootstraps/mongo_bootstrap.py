import motor.motor_asyncio
# Connect to Mongo Server, create database, create collections, establish system credentials, save relevant information


class MongoBootstrapper:
    default_data = {
        "PROTOCOL": "mongodb",
        "USERNAME": "DEMO",
        "PASSWORD": "DEMO",
        "HOSTNAME": "127.0.0.1",
        "HOST_PORT": "27017",
        "DATABASE": "COHERENCY",
    }
    uri_template = "{PROTOCOL}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{HOST_PORT}/{DATABASE}"

    @staticmethod
    def test_connection_string(uri=None, data=None, msg=False):
        if uri is None:
            uri = MongoBootstrapper.uri_template
        if data is None:
            data = MongoBootstrapper.default_data
        try:
            _ = motor.motor_asyncio.AsyncIOMotorClient(uri.format(**data))
            result = True
            result_msg = "Success"
        except ConnectionError as e:
            result = False
            result_msg = e.strerror
        if msg:
            return result_msg
        else:
            return result
