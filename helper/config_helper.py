from pathlib import Path
import json


class ConfigHelper:
    @staticmethod
    def get_fast_api_magic_values():
        return {
            "FAST_API_CONFIG": Path("../configs/fast_api_config.json"),   # FastAPI config file name
            "SERVICE_NAME": "COHERENCY_ENGINE",                           # Service Name used by the OS Keyring
            "SECRET_KEY_FORMAT": "HEX",                                   # Format used for the FastAPI Secret Key
            "SECRET_KEY_LENGTH": 32,                                      # Length used for the FastAPI Secret Key
            "ENCRYPTION_ALGORITHM": "HS256",                              # Algorithm JWT Encode will use
            "ACCESS_TOKEN_EXPIRE_MINUTES": 30,                            # Time to Live for Access Tokens in minutes
        }

    @staticmethod
    def set_fast_api_config(path=None):
        magic_values = ConfigHelper.get_fast_api_magic_values()
        if not Path.is_file(path := (magic_values["FAST_API_CONFIG"] if path is None else path)):
            ConfigHelper.create_fast_api_config(path=path)

    @staticmethod
    def get_fast_api_config(path=None):
        magic_values = ConfigHelper.get_fast_api_magic_values()
        if path is None:
            path = magic_values["FAST_API_CONFIG"]
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except IOError as e:
            print(e)

    @staticmethod
    def create_fast_api_config(path=None):
        magic_values = ConfigHelper.get_fast_api_magic_values()
        if path is None:
            path = magic_values["FAST_API_CONFIG"]
        del magic_values["FAST_API_CONFIG"]
        try:
            with open(path, 'w') as f:
                json.dump(obj=magic_values, fp=f)
        except IOError as e:
            print(e)

    @staticmethod
    def get_database_magic_values():
        return {
            "DATABASE_CONFIG": Path("../configs/database_config.json"),   # Database config file name
            "PROTOCOL": "mongodb",
            "USER": "DEMO",
            "PASSWORD": "DEMO",
            "HOST": "127.0.0.1",
            "PORT": "27017",
            "DATABASE": "COHERENCY",
            "ADDENDUM": "?retryWrites=true&w=majority",
            "CONNECT": "{PROTOCOL}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}{ADDENDUM}"
        }

    @staticmethod
    def set_database_config(path=None):
        magic_values = ConfigHelper.get_database_magic_values()
        if not Path.is_file(path := (magic_values["DATABASE_CONFIG"] if path is None else path)):
            ConfigHelper.create_database_config(path=path)

    @staticmethod
    def create_database_config(path=None):
        magic_values = ConfigHelper.get_database_magic_values()
        if path is None:
            path = magic_values["DATABASE_CONFIG"]
        del magic_values["DATABASE_CONFIG"]
        try:
            with open(path, 'w') as f:
                json.dump(obj=magic_values, fp=f)
        except IOError as e:
            print(e)

    @staticmethod
    def get_database_config(path=None):
        magic_values = ConfigHelper.get_database_magic_values()
        if path is None:
            path = magic_values["DATABASE_CONFIG"]
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except IOError as e:
            print(e)
