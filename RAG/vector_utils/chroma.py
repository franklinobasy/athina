from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import chromadb


from .utils import docs_loader, splitter

def chromadb_store(
    collection_name,
    persist,
    data_dir,
    db_directory="chroma_persist_directory",
):
    if not persist:
        docs = docs_loader(data_dir)
        texts = splitter(docs)

        db = Chroma.from_documents(
            texts,
            embedding=OpenAIEmbeddings(),
            collection_name=collection_name,
            persist_directory=db_directory,
        )

        return db

    client = chromadb.PersistentClient(path=db_directory)

    db = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=OpenAIEmbeddings(),
    )

    return db