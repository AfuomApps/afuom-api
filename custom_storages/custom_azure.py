from storages.backends.azure_storage import AzureStorage
from credentials import passport


class PublicAzureStorage(AzureStorage):
    account_name = passport.AZURE_ACCOUNT_NAME
    account_key = passport.AZURE_ACCOUNT_KEY
    azure_container = passport.AZURE_ACCOUNT_CONTAINER
    expiration_secs = None
