from pathlib import Path
import json

# Magic Values
FAST_API_CONFIG_PATH = "..\configs\fast_api_config.json"
SERVICE_NAME = "COHERENCY_ENGINE"   # Service Name used by the OS Keyring
SECRET_KEY_FORMAT = "HEX"           # Format used for the FastAPI Secret Key
SECRET_KEY_LENGTH = 32              # Length used for the FastAPI Secret Key
ENCRYPTION_ALGORITHM = "HS256"      # Algorithm CryptContext will use
ACCESS_TOKEN_EXPIRE_MINUTES = 30    # Time to Live for Access Tokens

class ConfigHelper:
    @staticmethod
    def get_fast_api_config(path=FAST_API_CONFIG_PATH):
        if not Path.is_file(path):
            ConfigHelper.create_fast_api_config(path=path)
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except IOError as e:
            print(e)

    @staticmethod
    def create_fast_api_config(path=FAST_API_CONFIG_PATH):
        data = {
            "service_name": SERVICE_NAME,
            "secret_key_format": SECRET_KEY_FORMAT,
            "secret_key_length": SECRET_KEY_LENGTH,
            "encryption_algorithm": ENCRYPTION_ALGORITHM,
            "access_token_expiration_minutes": ACCESS_TOKEN_EXPIRE_MINUTES
        }