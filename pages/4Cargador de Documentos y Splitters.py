import os
import openai
import tempfile
import streamlit as st
from langchain.text_splitter import Language
from langchain.document_loaders import CSVLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="Aprendiendo LangChain | Document Loaders and Text Splitters", page_icon="✂️")

st.header('✂️ Cargadores de documentos y Splitters de Texto')

st.write('''
Uno de los conceptos más revolucionarios en el mundo de la inteligencia artificial es tener LLM interactuando con nuestros datos de propios. LangChain proporciona clases y métodos convenientes para cargar varios tipos de documentos y transformarlos para adaptarse a las necesidades de nuestra aplicación.
''')

st.subheader('Cargadores de Documentos')

st.write('''
Para manejar diferentes tipos de documentos de manera sencilla, LangChain proporciona varias clases de cargadores de documentos. Con los cargadores de documentos, podemos cargar archivos externos en nuestra aplicación y dependeremos en gran medida de esta característica para implementar sistemas de inteligencia artificial que trabajen con nuestros propios datos de propiedad intelectual, que no están presentes en el entrenamiento predeterminado del modelo. Para cargar un documento, por lo general solo necesitamos unas pocas líneas de código, por ejemplo:
''')

st.code('''
from langchain_community.document_loaders import TextLoader

# load the document and split it into chunks
loader = TextLoader("../../modules/state_of_the_union.txt")
documents = loader.load()
''')

st.write('''
Veamos este cargador en acción para realmente entender el propósito y el valor de utilizar cargadores de documentos en comparación con otros métodos incorporados en Python.
''')

st.subheader('Cargador de txt archivos')

sample_txt_file = st.file_uploader("Cargar un TXT file", type=["txt"])

if sample_txt_file:

    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:

        temporary_file.write(sample_txt_file.read())

    loader = TextLoader(temporary_file.name)

    st.write(loader.load())

    # clean-up the temporary file
    os.remove(temporary_file.name)

st.write('''
Si intentaste cargar este tipo de archivo diferente, es posible que hayas notado que el cargador de LangChain básicamente convierte el documento en un objeto con la siguiente estructura:
''')

st.code('''
Document(page_content='the document content', metadata={'key': 'value'})
''')

st.write('''
Y esto es muy importante porque tener un **formato estandarizado** para muchos tipos de documentos nos permite trabajar fácilmente con muchas fuentes de entrada al mismo tiempo, como una capa de normalización incorporada. También podemos hacer notar que diferentes formatos tienen diferentes tipos de metadatos, por lo que el cargador de CSV conserva los números de fila, el PDF tiene números de página, y lo más importante es que podemos ver que los CSV y los PDF ya se dividen en múltiples documentos correspondientes al número de filas/páginas. Y esto nos lleva al siguiente tema: Divisores de texto.
''')

st.info('''
Para ver la lista completa de cargadores de documentos de LangChain, consulta la documentación oficial en:
https://python.langchain.com/docs/integrations/document_loaders/
''')

st.subheader('Splitters de Texto')

st.write('''
Antes de sumergirnos en los Divisores de Texto, es importante entender por qué este paso es crucial para trabajar correctamente con datos personalizados. Especialmente cuando lidiamos con datos no estructurados (archivos de texto, páginas web, transcripciones de audio), tenemos una enorme cantidad de contenido que no puede ser procesado de manera eficiente por un LLM. Por lo tanto, necesitamos dividirlo en fragmentos, y también asegurarnos de que esos fragmentos sean **semánticamente relevantes** para obtener respuestas adecuadas de los sistemas de inteligencia artificial. Cuando estamos utilizando Vectorstores en un gran conjunto de datos, nuestra aplicación necesitará buscar el fragmento más relevante (o fragmentos) para pasar al LLM basándose en la tarea, y cuando utilizamos [cadenas](https://python.langchain.com/docs/use_cases/summarization) específicas de LangChain (por ejemplo, map_reduce, refine, map_rerank), LangChain itera sobre todos los fragmentos, pero necesita que el documento esté dividido correctamente; de lo contrario, esas cadenas no funcionarán.
''')

st.write('''
Por más simple que parezca, dividir claramente es un paso muy importante y necesitamos dominarlo para construir aplicaciones efectivas de LangChain. Ahora veamos en acción algunos Divisores de Texto, comenzando por el más básico:
''')

st.subheader('CharacterTextSplitter')

st.code('''
from langchain.text_splitter import CharacterTextSplitter

# the chunk size/overlap are deliberately low for demo purposes
text_splitter = CharacterTextSplitter(
    separator = ' ',
    chunk_size=50,
    chunk_overlap=5,
    length_function=len,
)

# simply split the text
splits = text_splitter.split_text(text)
''')

with st.form("char_textsplitter"):

    text = st.text_area("Insert some text")

    execute = st.form_submit_button("✂️ Split")

    if execute:

        text_splitter = CharacterTextSplitter(
            separator = ' ',
            chunk_size=50,
            chunk_overlap=5,
            length_function=len,
        )

        splits = text_splitter.split_text(text)

        st.write(splits)

st.subheader('RecursiveCharacterTextSplitter')

st.write('''
RecursiveCharacterTextSplitter es la forma recomendada de dividir texto no estructurado, porque intenta mantener todos los párrafos y oraciones juntos. Por supuesto, podemos ajustar la superposición de fragmentos según el tipo de contenido que nuestra aplicación está procesando.
''')

st.code('''
from langchain.text_splitter import RecursiveCharacterTextSplitter

# the chunk size/overlap are deliberately low for demo purposes
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\\n\\n", "\\n", " ", ""],
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)

# create documents back from text chunks, as LangChain default format
docs = text_splitter.create_documents([text])
''')

with st.form("recursive_textsplitter"):

    text = st.text_area("Insert some text")

    execute = st.form_submit_button("✂️ Split")

    if execute:

        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", " ", ""],
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
        )

        docs = text_splitter.create_documents([text])

        st.write(docs)

st.subheader('Load and Split')

st.write('''
Recuerda que LangChain se trata completamente de simplicidad y abstracción, de hecho, también tenemos un método conveniente **`load_and_split()`** para cargar y dividir genéricamente el contenido al mismo tiempo. No funciona bien todo el tiempo (dependiendo de la fuente), pero es una línea útil para recordar y probar.
''')

st.code('''
from langchain.document_loaders import WebBaseLoader

web_loader = WebBaseLoader(url)

docs = web_loader.load_and_split()
''')

with st.form("load_and_split"):

    url = st.text_input("Insert an URL to load", placeholder="https://francescocarlucci.com/blog/thoughts-on-artificial-intelligence")

    execute = st.form_submit_button("✂️ Load and Split")

    if execute:

        web_loader = WebBaseLoader(url)

        docs = web_loader.load_and_split()

        st.write(docs)

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')
