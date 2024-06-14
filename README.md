# Athina Internship Task

Task: Create a RAG-powered chatbot that can answer questions based on a PDF document.

The repository contains the source code for the RAG app.

To start the application:
1.Install requirements

```bash
python -m pip install -r requirements.txt
```

2. Launch app:

```bash
streamlit run app.py
```

## How the Bot was Evaluated

The bot was Evaluated using a custom dataset.

The [`dataset`](dataset/test-set.jsonl) was prepared using the python giskard library.

The giskard library uses an agent to generate the test set. In order to do this, the library requires:
1. A knowledge base. The knowledge base is simply the data source, where all the text is stored.
```python
import pandas as pd
from giskard.rag import KnowledgeBase

df = pd.DataFrame([d.page_content for d in texts], columns=["text"])

knowledge_base = KnowledgeBase(df)
```

2. Agent description. The agent description is basically the prompt that informs the agent on how to generate the questions.

The goal is to make the questions diverse, that is, the questions generated should encompass several topics that relates to the pdf. To achieve this, I manually extracted different topics from the pdf:

```python
topics = [
    'Making a claim', 'What your cover includes', 'Liability',
    'Fire and theft', 'Courtesy car', 'Accidental damage',
    'Windscreen damage', 'Personal benefits', 'Motor Legal Cover',
    'Guaranteed Hire Car Plus', 'Protected No Claim Discount',
    'Where you can drive', 'Losses we don’t cover', 'Other conditions you need to know about',
    'How the policy works', 'If you have a complaint', 'If you’re in an accident',
    'How to get in touch'
]
    
```

Then I proceeded to generating the test dataset:

```python

from giskard.rag import generate_testset

testset = generate_testset(
    knowledge_base,
    num_questions=30,
    agent_description=f"A chatbot answering questions about car insurance in churchill. Churchill is a car insurance company. Use the following topics: {','.join(topics)}",
)
```

### Why I feel this is a comprehensive dataset.

After critically going through the generated dataset, I am confident that it is comprehensive because of the fact that each question addresses different possible topics or sections in the pdfs. 

As I mentioned earlier, I extracted different sections/topic to inform the giskard agent properly.

Here's my jupyter [`notebook`](notebooks/test_rag.ipynb)
 


### RAG Evaluation

The RAG was Evaluated evaluated using the test dataset.

```
from RAG.ai.chat import qa
from RAG.vector_utils.index import get_index
     

retriever = get_index('../data', 'churchill').as_retriever()
     

def answer_fn(question, history=None):
    return qa(query=question, retriever=retriever)
     

from giskard.rag import evaluate
# from giskard.rag.metrics.ragas_metrics import ragas_context_recall, ragas_context_precision

report = evaluate(
    answer_fn,
    testset=testset,
    knowledge_base=knowledge_base,
)

display(report)
```

Evaluation Report:

1. GENERATOR
Score: 84.0% The Generator is the LLM inside the RAG to generate the answers.

2.RETRIEVER
Score: 70.0% The Retriever fetches relevant documents from the knowledge base according to a user query.

3.REWRITER
Score:60.0% The Rewriter modifies the user query to match a predefined format or to include the context from the chat history.

4. ROUTING
Score: 100.0% The Router filters the query of the user based on his intentions (intentions detection).

5. KNOWLEDGE_BASE
Score: 61.54% The knowledge base is the set of documents given to the RAG to generate the answers. Its scores is computed differently from the other components: it is the difference between the maximum and minimum correctness score across all the topics of the knowledge base.


Overall Correctness Score: 73%