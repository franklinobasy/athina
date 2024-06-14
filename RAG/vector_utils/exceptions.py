
class StoreNotImplemented(Exception):
    def __init__(self, store_name):
        message = f'There is currently not support for {store_name}'
        super().__init__(message)
