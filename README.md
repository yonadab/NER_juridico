# NER_juridico
Name Entity Recognition para entidades Jurídicas

**¿Qué es el reconocimiento de entidades jurídicas y cómo funciona?**

La detección de entidades o Named Entity Recognition (NER) es un modelo de aprendizaje de máquina que permite localizar y clasificar automáticamente determinadas palabras dentro de un texto en categorías predefinidas como personas, organizaciones, lugares, marcas, cantidades, entre otras a partir de un entrenamiento con datos.

En este caso, el reconocimiento de entidades jurídicas clasifica, ubica y localiza todas las palabras que tengan que ver con el sistema penal acusatorio y el sistema fiscal en México. Por ejemplo la palabra Víctima será clasificada con la etiqueta Penal debido a que pertenece al sistema penal acusatorio.

**¿Cómo funciona el NER JURÍDICO?**

import utils

texto = 'artículo 102 del Código Fiscal de la Federación establece que comete el delito de contrabando quien introduzca al país o extraiga de él mercancías: I.- Omitiendo el pago total o parcial de las contribuciones o cuotas compensatorias que deban cubrirse. En este artículo, el estado nos advierte que aquél que realice dicha conducta estará realizando un delito'

utils.NER(texto)



**Sobre el modelo:**

En algunas ocasiones, el modelo no es capaz de generalizar palabras compuestas con dos o más entidades como por ejemplo *Servicio de Administración Tributaria*

En un futuro se agregarán más clasificaciones jurídicas y se ampliarán los datos de entrenamiento para su mejora en la predicción

*Notas de autor: El modelo pretende ser de utilidad y apoyo para textos jurídicos y la mejora de su comprensión. En ningún momento sustituye la actividad de un abogado o licenciado en el tema judicial.*
