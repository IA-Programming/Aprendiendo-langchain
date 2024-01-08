import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI

st.set_page_config(
    page_title="Aprendiendo LangChain ! Grandes Modelos de Languaje",
    page_icon="🤖"
)

from st_components.st_init import password

st.header('🤖 Grandes Modelos de Languaje (LLMs)')

if 'OPENAI_API_KEY' not in st.session_state:
    password()
    
else:
    st.success('Exitosamente colocado tu api key', icon='🎉')

st.write('''
Los Modelos de Lenguaje Grandes (LLMs, por sus siglas en inglés) son un tipo de red neuronal entrenada con una gran cantidad de datos de texto, diseñada para entender y generar texto similar al humano basado en las entradas recibidas, y son el núcleo de LangChain. El framework nos permite conectar e interactuar con todos los LLMs más populares, como OpenAI, Cohere, Hugging Face, cualquier modelo alojado en Replicate, y muchos más.
''')

st.subheader('OpenAI LLM')

st.write('''
En este primer tutorial veremos un ejemplo básico conectando con el modelo de OpenAI (también conocido como ChatGPT), probablemente el modelo más popular en el momento de la escritura. Lo instanciaremos y realizaremos una interacción básica.
''')

st.code('''
from langchain_openai import OpenAI

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)

response = llm(your_prompt)

print(response)
''')

with st.form("openai_llm"):

    prompt = st.text_input("Prompt", placeholder="What is 2+2?")

    execute = st.form_submit_button("🚀 Execute")

    if execute and 'OPENAI_API_KEY' in st.session_state:

        llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.5)

        response = llm(prompt)

        st.code(response)
    elif execute and 'OPENAI_API_KEY' not in st.session_state:
        st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.write('''
Aunque pueda parecer trivial abstraer una simple llamada a la API del modelo GPT de OpenAI, este es solo un ejemplo básico que sirve como base para las herramientas más valiosas de LangChain que permitirán construir flujos de trabajo mucho más complejos. Por ahora, apreciemos cómo lo configuramos usando solo 5 líneas de código y lo fácil que es conectar otro modelo.
''')

st.subheader('ChatOpenAI LLM')

st.code('''
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-3.5-turbo-1106", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)

response = chat(your_prompt)

print(response)
''')

with st.form("ChatOpenai_llm"):

    prompt = st.text_input("Prompt", placeholder="What is 2+2?")

    execute = st.form_submit_button("🚀 Execute")

    if execute and 'OPENAI_API_KEY' in st.session_state:

        chat = ChatOpenAI(model_name="gpt-3.5-turbo-1106", api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.5)

        response = chat(prompt)

        st.code(response)
    elif execute and 'OPENAI_API_KEY' not in st.session_state:
        st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.write('''
Take some time to play with prompts and observe how different LLMs provide us so
different responses. This is why is very important to choose the right model based
on our specific needs.
''')

st.subheader('LLMs vs ChatModels')

st.write('''
Los LLMs en LangChain se refieren a modelos de completado de texto (entrada de texto/salida de texto). Sin embargo, algunos modelos requieren una interfaz más compleja, están entrenados específicamente para tener conversaciones y toman una lista de mensajes de chat como entrada. Estos mensajes suelen estar etiquetados con el interlocutor (uno de "System", "AI" y "Human"). Por ejemplo, GPT-4 está entrenado como modelo de chat, mientras que GPT-3 como un LLM. Los modelos de chat funcionan muy bien con las plantillas de comandos de LangChain, que veremos en la próxima sección.
''')

st.subheader('Referencias')

st.markdown('''
            - [OpenAI](https://python.langchain.com/docs/integrations/llms/openai)
            - [ChatOpenAI](https://python.langchain.com/docs/integrations/chat/openai)
            - [OpenAI Plattform Models](https://platform.openai.com/docs/models/models)
            ''')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')
