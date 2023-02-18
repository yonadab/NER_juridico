# -*- coding: utf-8 -*-
"""

#################################################################
##                                                             ##
##               NAME ENTITY RECOGNITION (NER)                 ##
##        PARA ENTIDADES JURÍDICAS: FISCALES Y PENALES         ##
##                                                             ##
#################################################################


@author: YONADAB JARED GUZMAN MENDOZA

"""

import spacy
from spacy import displacy

def load_model(text):
    # Leemos el modelo pre-entrenado
    nlp = spacy.load('./modelo/MODELO_PENAL_FISCAL')
    doc = nlp(text)

    return doc


def NER(text):
    # Graficamos
    colors = {"Penal": "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
             'Fiscal': 'linear-gradient(90deg, #00FBC1, #01DFC2)'}
    
    options = {"ents": ["Penal",'Fiscal'], "colors": colors}
    
    doc = load_model(text)
    
    disp_obj = displacy.render(doc, style="ent", options=options, jupyter=False)

    return disp_obj