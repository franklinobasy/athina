
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def docs_loader(dir: str):
    loader = DirectoryLoader(dir, glob="**/*.pdf")
    docs = loader.load()
    return docs


def splitter(docs: list, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    is_separator_regex=False,
)
    texts = text_splitter.split_documents(docs)
    return texts
