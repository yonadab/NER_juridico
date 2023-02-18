# -*- coding: utf-8 -*-
"""
@author: Yonadab Jared Guzmán Mendoza

"""

import streamlit as st
import utils
from PIL import Image

# configuraciones iniciales
st.set_page_config(page_title='NER JURIDICO',
                   page_icon=':briefcase:',
                   layout='wide')


# eliminamos las notas de agua de la pagina para que se ve más estética
hide_st_style = """
	<style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	header {visibility: hidden;}
	</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


####### SECCIÓN DE INFORMACIÓN DE LA PAGINA Y CONTENIDO ##############

st.title('RECONOCIMIENTO DE ENTIDADES (:blue[NER]) JURÍDICAS')
st.caption('by Yonadab')

tab_analizar, tab_modelo, tab_train, tab_que_es, tab_funcion = st.tabs(['Analizar texto','Modelo','Entrenamiento','¿Qué es NER Jurídico?', '¿Cómo funciona?'])


with tab_analizar:
    st.write('Ingresa tu texto aquí:')
    text = st.text_area('', height=190)
    
    
    
    butt_analisis = st.button('Analizar texto')
    
    if butt_analisis:
        if text != '':
            st.write('**RESULTADO:**')
            ent_html = utils.NER(text)
            st.markdown(ent_html, unsafe_allow_html=True)
        
        else:
            st.write('**No se ha encontrado ningún texto dentro de la caja**')


with tab_modelo:
    
    st.subheader('Natural Language Processing')
    
    st.write('El modelo está basado en técnicas de procesamiento del lenguaje natural (NLP) \
             supervisado mediante la librería Spacy (3.5.0). Para ello se recopilaron textos \
            de la web (__ver apartado de Entrenamiento__) y posteriormente fueron procesados mediante \
            la vectorización de palabras; esto permite que el modelo sea más flexible y generalizable a la hora de procesar el texto.  ')
    
    image = Image.open('./images/ML_logo.png')
    st.image(image)


with tab_train:
    
    st.subheader('Corpus textual')
    
    st.write('Para extraer y categorizar las etiquetas a partir de cualquier texto,\
             los modelos de aprendizaje necesitan información valiosa para su procesamiento.\
            Para estos fines, es necesario dotar de un _corpus textual_ donde el modelo extraiga \
            y comprenda las palabras presentadas. \n')
    
    st.write('En la primera etapa, se recopilaron las palabras más relevantes dentro del\
             sistema penal judicial y fiscal, tales como:  **Víctima, SAT, Sistema Penal, Juez,\
            Contribuciones, etc.** mismas que fueron puesta sen un archivo de texto.\
            Posteriormente, se recopiló un corpus desde la web en fuentes oficiales como\
            la página de Gobernación y SAT así como fuente no oficiales tales como Wikipedia\
            y terceros. \n')
            
    st.write('Gran parte del corpus para al extracción de entidades penales está entrenado en el Código penal de procedimientos legales.')

    st.caption('Para consultar los datos de entrenamiento, visita mi Github.')



with tab_que_es:


    st.subheader('¿Qué es el reconocimiento de entidades jurídicas y cómo funciona?')
    st.write('La detección de entidades o Named Entity Recognition (NER) es un modelo de\
         aprendizaje de máquina que permite localizar y clasificar automáticamente \
        determinadas palabras dentro de un texto en categorías predefinidas como \
        personas, organizaciones, lugares, marcas, cantidades, entre otras \
        a partir de un entrenamiento con datos.\
        \n')
        
    st.write('En este caso, el reconocimiento de entidades jurídicas clasifica, ubica y localiza todas \
        las palabras que tengan que ver con el sistema penal acusatorio y el sistema fiscal en México.\
        Por ejemplo la palabra :orange[Víctima] será clasificada con la etiqueta **Penal** debido a \
        que pertenece al sistema penal acusatorio.')
        

with tab_funcion:
    
    st.subheader('¿Cómo funciona el NER JURÍDICO?')
    
    st.write('1) Ingresa un texto dentro de la caja en el apartado _analizar texto_ \n')
    st.write('2) Click en el botón _Analizar texto_ \n')
    st.write('3) El modelo automáticamente analizará las palabras que pertenecen al sistema\
             fiscal mediante la palabra **Fiscal** y la palabra **Penal** según sea el caso.\
            Para cada etiqueta existe un color _(verde para Fiscal y morado para Penal)_ tal\
            como se observa en la siguiente imagen:')
    
    ejemplo = Image.open('./images/ejemplo.png')
    st.image(ejemplo, width=512)
    
    st.write('**:blue[Nota:]** **Para obtener mejores resultados, evita poner cadenas de caracteres especiales largos dentro del texto\
             ya que el modelo mal clasificará los resultados.**')
 
    error = Image.open('./images/error.png')
    st.image(error, caption='Ejemplo de mal clasificación del modelo')


st.sidebar.subheader('Sobre el modelo')
st.sidebar.caption('En algunas ocasiones, el modelo no es capaz de generalizar palabras compuestas con dos o más entidades\
                como por ejemplo _Servicio de Administración Tributaria_ \n')
st.sidebar.caption('En un futuro se agregarán más clasificaciones jurídicas y se ampliarán los datos de\
                 entrenamiento para su mejora en la predicción')
    
st.sidebar.write('**Notas de autor**')
st.sidebar.caption('_El modelo pretende ser de utilidad y apoyo para textos jurídicos y la mejora de su comprensión.\
                 En ningún momento sustituye la actividad de un abogado o licenciado en el tema judicial._')       

st.sidebar.write('**__________________________________**')
st.sidebar.caption('Visita mi Github')

github = st.sidebar.button('Ir a Github')

if github:
    import webbrowser
    webbrowser.open_new('https://github.com/yonadab')
        
        
