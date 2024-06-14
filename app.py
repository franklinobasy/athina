import streamlit as st
from RAG.vector_utils.index import get_index
from RAG.ai.chat import qa 

# Initialize the retriever
retriever = get_index(data_dir='data', collection_name='churchil').as_retriever()

# Streamlit app
st.title('Churchill Chatbot')

# Create a form for user input
with st.form(key='chat_form'):
    user_input = st.text_input('You:', '')
    submit_button = st.form_submit_button(label='Send')

    # Process user input and display the response
    if submit_button and user_input:
        # Call the qa function with user input and retriever
            response = qa(user_input, retriever)
            st.write(f'Assistant: {response}')