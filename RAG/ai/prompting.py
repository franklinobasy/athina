from langchain.prompts import PromptTemplate

template = '''
You are a chat bot that works for Churchill Insurance company.
Your task is to answer the question about car insurance in
churchill using the following context. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
'''

prompt = PromptTemplate.from_template(template)