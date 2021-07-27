from pathlib import Path
import json


class ConfigHelper:
    @staticmethod
    def configuration_bootstrap(path=None):
        environment_default = ConfigHelper.get_environment_magic_values()
        # Test whether the configuration files retain their default values
        # If so, log the error to the system log then wait for 1 minute before checking again
        # After 4 hours of failures to update the configs, return no configurations and stop
        # Once a valid configuration is available, check whether it represents a change from existing
        # If configurations are valid and changed, update the stored configuration, then recheck.
        # If configurations are valid and unchanged, load the configurations and return.

    @staticmethod
    def get_environment_magic_values():
        return {
            "ENVIRONMENT_CONFIG": Path("../configs/environment.json"),   # Environment config file name
            "CONFIGURED": False
        }

    @staticmethod
    def create_environment_config(path=None):
        magic_values = ConfigHelper.get_environment_magic_values()
        path = magic_values["FAST_API_CONFIG"] if path is None else path
        del magic_values["FAST_API_CONFIG"]
        try:
            with open(path, 'w') as f:
                json.dump(obj=magic_values, fp=f)
        except IOError as e:
            print(e)

    @staticmethod
    def get_environment_config(path=None):
        magic_values = ConfigHelper.get_environment_magic_values()
        if path is None:
            path = magic_values["ENVIRONMENT_CONFIG"]
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except IOError as e:
            print(e)

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
        path = magic_values["FAST_API_CONFIG"] if path is None else path
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
        path = magic_values["DATABASE_CONFIG"] if path is None else path
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


if __name__ == "__main__":
    ConfigHelper.create_fast_api_config()
    ConfigHelper.create_database_config()
