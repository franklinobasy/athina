
class ProviderNotImplemented(Exception):
    def __init__(self, provider):
        message = f'There is currently not support for {provider}'
        super().__init__(message)
