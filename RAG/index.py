from langchain_community.document_loaders import DirectoryLoader


def docs_loader(dir: str):
    loader = DirectoryLoader(dir, glob="**/*.pdf")
    docs = loader.load()
    return docs