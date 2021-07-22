import secrets
import keyring


class KeyringHelper:
    @staticmethod
    def get_keyring_data(data_field, service_id=__name__):
        """ Retrieve Environment Variable

        :param data_field: Environment Variable to retrieve
        :param service_id: Service Name under which the variable is stored
        :return: The environment variable value or None if not present
        """
        return keyring.get_password(service_name=service_id, username=data_field)

    @staticmethod
    def set_keyring_data(data_field="SECRET", service_id=__name__, password=None):
        """ Set Environment Variable

        :param data_field: Environment Variable to set
        :param service_id: Service Name under which the variable will be stored
        :param password: Value to be stored
        :return: None
        """
        keyring.set_password(service_name=service_id, username=data_field, password=password)

    @staticmethod
    def generate_secret(secret_type="HEX", length=32):
        if secret_type == "HEX":
            return secrets.token_hex(length)
        if secret_type == "BYTES":
            return secrets.token_bytes(length)
        if secret_type == "URL":
            return secrets.token_urlsafe(length)
