import os
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter

from .exceptions import ProviderNotImplemented
from RAG.vector_utils.index import get_index
from .prompting import prompt


def qa(query, retriever):
    model = ChatOpenAI(model='gpt-4')
    chain = (
        {
            "context": itemgetter("question") | retriever,
            "question": itemgetter("question"),
        }
        | prompt
        | model
        | StrOutputParser()
    )
    
    return chain.invoke({
        'question': query
    })
