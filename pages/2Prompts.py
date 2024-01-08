import streamlit as st
from langchain_openai import ChatOpenAI, OpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate

st.set_page_config(page_title="Aprendiendo LangChain | Prompts", page_icon="📝")

from st_components.st_init import password

st.header('📝  Prompts')

if 'OPENAI_API_KEY' not in st.session_state:
    password()
    
else:
    st.success('Exitosamente colocado tu api key', icon='🎉')

st.write('''
Los Prompts son otro componente clave en LangChain y en general en los Modelos de Lenguaje Grandes. Una indicación bien estructurada puede marcar la diferencia para obtener un resultado de calidad de nuestro modelo de IA. LangChain proporciona un componente de Plantilla de Indicaciones que facilita la redacción de buenas indicaciones y las hace reutilizables utilizando variables.
''')

st.info('La ingeniería de Prompts es una de las principales razones por las que la inteligencia artificial está ganando popularidad. Ahora podemos usar modelos pre-entrenados y aprovechar indicaciones específicas y concisas.', icon="ℹ️")

st.subheader('Prompts para modelos generadores de texto')

st.code('''
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt_template = PromptTemplate.from_template(
    "Dime un {adjective} chiste acerca {content}."
)
prompt_template.format(adjective="gracioso", content="pollos")
''')

st.code('''Dime un gracioso chiste acerca pollos.''')

st.code('''
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)

response = llm(prompt_template)

print(response)
''')

with st.form("prompt_template_text_generator"):

    prompt_template = PromptTemplate.from_template(
                "Dime un {adjective} chiste acerca {content}."
            )

    adjective = st.selectbox(
    	'Adjetivo',
    	("divertido", "gracioso", "alegre", "entretenido", "ingenioso", "cómico", "humorístico", "jovial", "juguetón")
    )

    about = st.text_input("Chiste acerca: ", placeholder="pollos, fashion, ...")

    execute = st.form_submit_button("🚀 Execute")

    if execute and 'OPENAI_API_KEY' in st.session_state:
        
        prompt_template.format(adjective=adjective, content=about)
        
        llm = OpenAI(model_name="gpt-3.5-turbo-instruct", api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.5)

        response = llm(prompt_template)

        print(response)

        st.code(response.content)
    elif execute and 'OPENAI_API_KEY' not in st.session_state:
        st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.subheader('Prompts para modelos de chat')

st.write('''
Como es habitual, hagamos todo más claro con un ejemplo de código y una demostración funcional. En este caso, configuraremos una plantilla de indicaciones que hará que nuestra IA actúe como consultora de nombres comerciales y genere ideas de nombres para cualquier negocio que deseemos y en diferentes estilos.
''')

st.code('''
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

template = """\
Eres un consultor de nombres para nuevas empresas.
¿Cuál es un buen nombre {adjective} para una empresa que fabrica {product} ?
"""

prompt_template = ChatPromptTemplate.from_template(template)

chat = ChatOpenAI(model_name="gpt-3.5-turbo-1106", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)

format_template = prompt_template.format_messages(adjective=name_type, product=business_type)

response = chat(format_template)
''')

with st.form("prompt_template"):

    template = """\
    Eres un consultor de nombres para nuevas empresas.
    ¿Cuál es un buen nombre {adjective} para una empresa que fabrica {product} ?
	Please reply only with the name, no comments attached.
	"""

    prompt_template = ChatPromptTemplate.from_template(template)

    name_type = st.selectbox(
    	'Tipo de nombre',
    	('divertido', 'serio', 'irriverente')
    )

    business_type = st.text_input("Tipo de negocio", placeholder="fruit shop, fashion atelier, ...")

    execute = st.form_submit_button("🚀 Execute")

    if execute  and 'OPENAI_API_KEY' in st.session_state:

        chat = ChatOpenAI(model_name="gpt-3.5-turbo-1106", api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.5)

        format_template = prompt_template.format_messages(adjective=name_type, product=business_type)

        response = chat(format_template)

        st.code(response.content)
    elif execute and 'OPENAI_API_KEY' not in st.session_state:
        st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.subheader('Ventajas de Prompt Plantillas')

st.write('''
- Claridad: algunas indicaciones pueden ser largas y detalladas, configurarlas como plantillas mejorará tu código.
- Reusabilidad: muchas veces podrás reutilizar plantillas existentes con algunos cambios en el código.
- Sencillez: LangChain tiene algunas plantillas predefinidas para operaciones comunes (las veremos más adelante).
- Seguridad: al limitar el control del usuario a las entradas necesarias, minimizamos el riesgo de mal uso de nuestro LLM.
- Salida: puedes instruir al LLM para que devuelva datos con palabras clave específicas y analizar la salida como datos estructurados en lugar de simplemente texto plano que se ajuste a las necesidades de tu aplicación.
Este último punto nos lleva al próximo componente de LangChain: los analizadores de salida.
''')

st.subheader('Referencias: ')

st.write('https://python.langchain.com/docs/modules/model_io/prompts/quick_start')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')