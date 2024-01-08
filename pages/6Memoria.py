import streamlit as st

st.set_page_config(
    page_title="Aprendiendo LangChain | Memory",
    page_icon="💡"
)

st.header('💡 Memory')

st.write('''
LLMs are stateless by default, meaning that they have no built-in memory. But sometimes
we need memory to implement applications such like conversational systems, which may have
to remember previous information provided by the user. Fortunately, LangChain provides
several memory management solutions, suitable for different use cases.

We have seen beofre as vector stores are referred as long-term memory, instead, the methods
we will see in this secion are considered short-term memory, as they do not persist after
the interactions are complete.
''')

st.subheader('ConversationBufferMemory')

st.write('''
This is the simplest memory class and basically what it does, is to include previous messages
in the new LLM prompt. You can try to have a conversation with the chatbot, then ask questions
about the previous message and the LLM will be able to answer them.
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.0)

memory = ConversationBufferMemory()
        
chain = ConversationChain(llm=llm, memory=memory)

chain.predict(input=prompt)
''')

st.subheader('ConversationBufferWindowMemory')

st.write('''
Of course, the conversation can get long and including all the chat instory in the prompt can
become inefficient and expensive, because longest prompts result in a highest LLM token usage.
To optimize this behavior, LangChain provides three other types of memory. The
ConversationBufferWindowMemory let up decide how many messages in the chat history the system
has to remember, using a simple parameter:
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.0)

# 2 is the number of messages stored in the memory
memory = ConversationBufferWindowMemory(k=2)
        
chain = ConversationChain(llm=llm, memory=memory)

chain.predict(input=prompt)
''')

st.subheader('ConversationTokenBufferMemory')

st.write('''
Very similar to the previous memory, the ConversationTokenBufferMemory type that let us be
more specific about the number of token we want to use in our prompts, and contains the content
stored to meet that limit. We have to pass the LLM as parameter, in order to calculate the 
number of tokens:
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationTokenBufferMemory

llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.0)

# limit to 50 tokens
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)
''')

st.subheader('ConversationSummaryMemory')

st.write('''
Finally, if we don't want just arbitrarily cut the memory based on a fixed lenght, we can
use the ConversationSummaryMemory, which still let us define a token limit, but passes as
memory a summary of the previous interactions. Thsi way we can still keep the short-term
memory under control while retaining the most importan information.
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.0)

# limit to 100 tokens and store a summary
memory = ConversationSummaryMemory(llm=llm, max_token_limit=100)
''')

st.info("In the following example, we will use the ConversationChain, another LangChain built-in chain.\
 You can choose the memory type and understand the memory usage by inspecting the memory dump.", icon="ℹ️")

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')
