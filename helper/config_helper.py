from pathlib import Path
import json


class ConfigHelper:
    @staticmethod
    def get_magic_values():
        return {
            "FAST_API_CONFIG": Path("../configs/fast_api_config.json"),   # FastAPI config file name
            "SERVICE_NAME": "COHERENCY_ENGINE",                           # Service Name used by the OS Keyring
            "SECRET_KEY_FORMAT": "HEX",                                   # Format used for the FastAPI Secret Key
            "SECRET_KEY_LENGTH": 32,                                      # Length used for the FastAPI Secret Key
            "ENCRYPTION_ALGORITHM": "HS256",                              # Algorithm JWT Encode will use
            "ACCESS_TOKEN_EXPIRE_MINUTES": 30,                            # Time to Live for Access Tokens in minutes
        }

    @staticmethod
    def get_fast_api_config(path=None):
        magic_values = ConfigHelper.get_magic_values()
        if not Path.is_file(magic_values["FAST_API_CONFIG"] if path is None else path):
            ConfigHelper.create_fast_api_config(path=magic_values["FAST_API_CONFIG"] if path is None else path)
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except IOError as e:
            print(e)

    @staticmethod
    def create_fast_api_config(path=None):
        magic_values = ConfigHelper.get_magic_values()
        data = {
            "service_name": magic_values["SERVICE_NAME"],
            "secret_key_format": magic_values["SECRET_KEY_FORMAT"],
            "secret_key_length": magic_values["SECRET_KEY_LENGTH"],
            "encryption_algorithm": magic_values["ENCRYPTION_ALGORITHM"],
            "access_token_expiration_minutes": magic_values["ACCESS_TOKEN_EXPIRE_MINUTES"]
        }
        try:
            with open(path, 'w') as f:
                json.dump(obj=data, fp=f)
        except IOError as e:
            print(e)