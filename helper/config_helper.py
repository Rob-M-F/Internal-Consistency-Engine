from pathlib import Path
from keyring_helper import KeyringHelper
import json
from time import sleep


class ConfigHelper:
    ENVIRONMENT_CONFIG_PATH = Path("../configs/environment.json")    # Environment config file name
    DEFAULT_SERVICE_NAME = ""

    @staticmethod
    def configuration_bootstrap(path=None):
        environment_default = ConfigHelper.get_environment_magic_values()
        if path is None:
            path = ConfigHelper.ENVIRONMENT_CONFIG_PATH
        print("Texting path existence: {path} - {existence}".format(path=path, existence=Path(path).exists()))
        if not Path(path).exists():
            ConfigHelper.create_environment_config()
        while (configuration := ConfigHelper.get_environment_config())["SERVICE_NAME"] == "":
            print("Waiting for valid configuration at {path}".format(path=path))
            sleep(3)
        basic_config = {"SERVICE_NAME": configuration.pop("SERVICE_NAME")}
        for config in configuration:
            KeyringHelper.set_keyring_data(
                data_field=config,
                service_id=basic_config["SERVICE_NAME"],
                password=configuration[config])
        ConfigHelper.set_environment_config(path=path, config=basic_config)
        return ConfigHelper.get_environment_values(service_name=basic_config["SERVICE_NAME"])

    @staticmethod
    def get_environment_values(service_name):
        key_list = ConfigHelper.get_environment_magic_values().keys()
        return {key: KeyringHelper.get_keyring_data(data_field=key, service_id=service_name) for key in key_list}

    @staticmethod
    def get_environment_magic_values():
        return {
            "SECRET_KEY_FORMAT": "HEX",                                   # Format used for the FastAPI Secret Key
            "SECRET_KEY_LENGTH": 32,                                      # Length used for the FastAPI Secret Key
            "ENCRYPTION_ALGORITHM": "HS256",                              # Algorithm JWT Encode will use
            "ACCESS_TOKEN_EXPIRE_MINUTES": 30,                            # Time to Live for Access Tokens in minutes
            "DATABASE_PROTOCOL": "mongodb",
            "DATABASE_USER": "DEMO",
            "DATABASE_PASSWORD": "DEMO",
            "DATABASE_HOST": "127.0.0.1",
            "DATABASE_PORT": "27017",
            "DATABASE_NAME": "COHERENCY",
            "CONNECTION_URI": "{DATABASE_PROTOCOL}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:" +
                              "{DATABASE_PORT}/{DATABASE_NAME}?retryWrites=true&w=majority"
        }

    @staticmethod
    def create_environment_config(path=None):
        ConfigHelper.set_environment_config(path=path)

    @staticmethod
    def set_environment_config(path=None, config=None):
        if config is None:
            config = ConfigHelper.get_environment_magic_values()
            config["SERVICE_NAME"] = ""
        if path is None:
            path = ConfigHelper.ENVIRONMENT_CONFIG_PATH
        try:
            with open(path, 'w') as f:
                json.dump(obj=config, fp=f)
        except IOError as e:
            print(e)

    @staticmethod
    def get_environment_config(path=None):
        magic_values = ConfigHelper.get_environment_magic_values()
        if path is None:
            path = ConfigHelper.ENVIRONMENT_CONFIG_PATH
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except IOError as e:
            print(e)


if __name__ == "__main__":
    print(ConfigHelper.configuration_bootstrap())
