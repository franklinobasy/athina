
from .exceptions import StoreNotImplemented
from .chroma import chromadb_store


def get_index(
    data_dir,
    collection_name,
    store_client: str = 'chromadb',
    persist: bool = False
):
    if store_client == 'chromadb':
        return chromadb_store(
            collection_name,
            persist,
            data_dir
        )
    else:
        raise StoreNotImplemented(store_client)
    