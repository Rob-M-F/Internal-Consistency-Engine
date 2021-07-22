import motor.motor_asyncio
import json


class DatabaseHelper:
    config_type: str
    config_type: str
    uri_details: dict
    uri: str

    def __init__(self, config_type="file", config_key="db_config.json"):
        if config_type == "file":
            try:
                with open(config_key) as f:
                    data = json.load(f)
                    self.configure(data)
            except IOError as e:
                print("In Datasource Init, config file fault.")
                print(e)

    def configure(self, protocol="mongodb", user="DEMO", password="DEMO", host="127.0.0.1", port="27017", db="DEMO",
                  extra="?retryWrites=true&w=majority"):
        self.uri_details["PROTOCOL"] = protocol
        self.uri_details["USER"] = user
        self.uri_details["PASSWORD"] = password
        self.uri_details["HOST"] = host
        self.uri_details["PORT"] = port
        self.uri_details["DB"] = db
        self.uri_details["EXTRA"] = extra
        self.uri = "{PROTOCOL}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}{EXTRA}"


DB_INFO = {
    "PROTOCOL": "mongodb",
    "USERNAME": "DEMO",
    "PASSWORD": "DEMO",
    "HOSTNAME": "127.0.0.1",
    "HOSTPORT": "27017",
    "DATABASE": "COHERENCY",
    "ADDENDUM": "?retryWrites=true&w=majority",
    "CONNECT": "{PROTOCOL}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{HOSTPORT}/{DATABASE}{ADDENDUM}"
}

datasource = motor.motor_asyncio.AsyncIOMotorClient(DB_INFO["CONNECT"].format(**DB_INFO))




