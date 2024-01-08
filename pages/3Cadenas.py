import streamlit as st
from langchain.chains import LLMChain,LLMMathChain
from langchain_openai import ChatOpenAI, OpenAI
from langchain.prompts import ChatPromptTemplate

st.set_page_config(page_title="Aprendiendo LangChain | Cadenas",page_icon="🔗")

from st_components.st_init import password

st.header('🔗 Cadenas')

if 'OPENAI_API_KEY' not in st.session_state:
    password()
    
else:
    st.success('Exitosamente colocado tu api key', icon='🎉')

st.write('''
Ahora que tenemos una buena comprensión de los LLMs y las Plantillas de Prompts, estamos listos para presentar las cadenas, el componente central más importante de LangChain. Las cadenas son clases preconstruidas que nos permiten combinar LLMs e Indicaciones juntos, con un enfoque modular diseñado para facilitar la creación de flujos de procesamiento de lenguaje complejas mientras mantenemos nuestra base de código sólida y legible.

LangChain proporciona cadenas para las operaciones más comunes (enrutamiento, ejecución secuencial, análisis de documentos), así como cadenas avanzadas para trabajar con datos personalizados, manejar la memoria y más. También veremos características más avanzadas de LangChain (tokenizadores, transformadores, incrustaciones) que son mucho más fáciles de usar con cadenas.
''')

st.subheader('Our first basic Chain')

st.code('''
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

prompt = ChatPromptTemplate.from_template(\'''
I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
The name should honor the film story as it is. Please limit your answer to the name only.\
If you don't know the movie, answer: "I don't know this movie"
\''')

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run(movie)
''')

with st.form("basic_chain"):

    movie = st.text_input("Movie", placeholder="The Green Mile")

    execute = st.form_submit_button("🚀 Execute")

with st.spinner('Processing your request...'):
	if execute and 'OPENAI_API_KEY' in st.session_state:

		llm = ChatOpenAI(openai_api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.9)

		prompt = ChatPromptTemplate.from_template('''
		I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
		The name should honor the film story as it is. Please limit your answer to the name only.\
		If you don't know the movie, answer: "I don't know this movie"
		''')

		chain = LLMChain(llm=llm, prompt=prompt)

		response = chain.run(movie)

		st.code(response)

	elif execute and 'OPENAI_API_KEY' not in st.session_state:
		st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.write('''
Esta Cadena básica no es muy diferente del enfoque de la Plantilla de Prompts, pero avancemos hacia un ejemplo donde podamos ver las ventajas y la simplicidad que nos brindan las cadenas.
''')

st.subheader('LlmMath tool')

st.write('La herramienta LLMmath es una poderosa herramienta que te permite realizar cálculos matemáticos utilizando la biblioteca numexpr de Python. Puede traducir problemas matemáticos en expresiones que pueden ser ejecutadas y proporcionar la salida de la ejecución del código')

st.code('''
from langchain.chains import LLMMathChain
from langchain_openai import OpenAI

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)
llmmath_tool = LLMMathTool(llm)
		
question = "37593 * 67"
output = llmmath_tool.run(question)
print(output)
''')

st.write('La salida seria:')

st.code('2518731')

with st.form("Math_tool	"):

    question = st.text_input("Ejercicio matematico a calcular", placeholder="Cuanto es 37593 * 67?")

    execute = st.form_submit_button("🚀 Execute")

with st.spinner('Processing your request...'):
	if execute and 'OPENAI_API_KEY' in st.session_state:

		llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.5)

		chain = LLMMathChain(llm=llm)

		response = chain.run(question)

		st.code(response)
	elif execute and 'OPENAI_API_KEY' not in st.session_state:
		st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.subheader('Para mantener en mente:')

st.write('''
LangChain proporciona una impresionante cantidad de cadenas con varios niveles de complejidad y diferentes propósitos. Estudiarlas todas puede resultar abrumador, pero estaremos utilizando varias de ellas en nuestros tutoriales prácticos, lo que hará que sea más divertido aprender en un contexto más práctico.
''')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')
