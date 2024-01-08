import streamlit as st

st.set_page_config(page_title="LangChain Curso de iniciantes", page_icon="📚")

st.header('📚 LangChain Curso Rapido')

st.subheader('Construye apps con IA y aprende haciendo!')

st.write('''
LangChain es un marco para desarrollar aplicaciones de inteligencia artificial (IA) de una manera mejor y más rápida. Puedes pensar en él como una capa de abstracción diseñada para interactuar con varios modelos de lenguaje grandes (LLM), procesar y persistir datos, realizar tareas complejas y tomar acciones utilizando diferentes APIs.
''')

st.subheader('Principales Componentes')

st.write('''
Los principales componentes/herramientas que LangChain ofrece para desarrollar aplicaciones de IA utilizando LangChain son:

- LLMs (Modelos de Lenguaje Grandes)
- Prompts
- Cadenas
- Splitters
- Embeddings / Almacenes de vectores
- Memoria
- Agentes

LangChain está disponible para Python y JavaScript, pero en esta guía nos enfocaremos en la versión de Python.
''')

st.subheader('Porque LangChain')

st.write('''
En mi opinión, cualquier tecnología que se haya adoptado a gran escala ha sido simplificada de alguna manera. Todos usamos tarjetas de crédito en línea, pero nadie implementa el procesamiento de tarjetas de crédito desde cero; la mayoría de las empresas utilizan Stripe/PayPal/3rd party gateways. El 90% de los sitios web se basan en frameworks y no en PHP, Python, Ruby, o lo que sea. La mayoría de la tecnología que usamos hoy en día es una capa de encapsulación de alguna otra tecnología de nivel inferior, y lo mismo sucede con la IA, estamos construyendo herramientas para reducir la curva de aprendizaje y permitir una adopción más rápida y fluida. ¡LangChain es una de esas herramientas!
''')

st.subheader('Para aprender mejor')

st.write('''
Para disfrutar mejor de este curso de LangChain, deberías tener un conocimiento básico de los fundamentos del desarrollo de software, y idealmente algo de experiencia con Python. Si no es así, puedes consultar estos recursos de FreeCodeCamp para mejorar tus habilidades y luego regresar.

- [Learn Python](https://www.youtube.com/watch?v=nKPbfIU442g)
- [Intro to Programming](https://www.youtube.com/watch?v=oHHsLTV7l3E)
''')

st.subheader('Creditos')

st.write('''
Todos los frameworks usado en este mini-curso pertenece a su propietarios:

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
''')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')
