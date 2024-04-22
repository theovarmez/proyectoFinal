# Propuesta de Proyecto MLOps

**Autores:**
- Luis Gabriel Corrales Mora
- Manuel Alejandro Espinoza Ramírez
- Cristian Vargas Jiménez

**Programa Académico:** Bachillerato en Ciencias de Datos

**Curso:** BCD4205 Gestión de tecnología digital

**Profesor:** Jorge Zapata

**Fecha:** Abril 2024

---

## Propuesta de Proyecto

### Objetivo del Proyecto:

Desarrollar un algoritmo de predicción de riesgo de ataque cardíaco basado en datos clínicos y biométricos del paciente, con el fin de identificar patrones y factores de riesgo asociados con la probabilidad de sufrir un evento cardíaco.

### Detalles del Objetivo:

El proyecto tiene como objetivo principal utilizar técnicas de aprendizaje automático para crear un modelo predictivo que pueda clasificar a los pacientes en dos categorías:

- Categoría 0: Individuos con menos posibilidades de sufrir un ataque cardíaco.
- Categoría 1: Individuos con más posibilidades de sufrir un ataque cardíaco.

Se utilizarán datos del conjunto de datos proporcionado por Kaggle, que incluyen variables como la edad, sexo, presión arterial en reposo, colesterol, frecuencia cardíaca máxima alcanzada, entre otros.

### Metodología Propuesta:

1. **Preprocesamiento de Datos:** Limpieza y transformación de los datos para garantizar su calidad y coherencia.
2. **Exploración de Datos:** Análisis exploratorio para comprender la distribución de las variables y su relación con el objetivo.
3. **Selección de Características:** Identificación de las variables más relevantes para la predicción del riesgo de ataque cardíaco.
4. **Desarrollo del Modelo:** Entrenamiento de varios modelos de aprendizaje automático utilizando técnicas de validación cruzada.
5. **Ajuste de Parámetros:** Optimización de los hiperparámetros de los modelos seleccionados.
6. **Evaluación del Modelo:** Evaluación del rendimiento del modelo final utilizando métricas de evaluación.
7. **Interpretación de Resultados:** Análisis e interpretación de los resultados para identificar los factores de riesgo más importantes.

### Tecnologías por Utilizar:

- **Lenguaje de Programación:** Python.
- **Herramientas de Contenerización:** Docker.
- **Versionamiento de los Datos:** DVC.
- **Repositorio de Control de Versiones:** GitHub.
- **Servicios en la Nube:** AWS (Amazon Web Services, EC2, S3).

### Entregables Esperados:

- Un informe técnico detallado que documente todo el proceso de desarrollo del modelo.
- El código fuente del algoritmo desarrollado, junto con instrucciones claras para su implementación y uso.
- Conclusiones y recomendaciones basadas en los hallazgos del análisis.
- Objetivo: 0= menos posibilidades de sufrir un ataque cardíaco 1= más posibilidades de sufrir un ataque cardíaco


### Acerca de este conjunto de datos

- Edad: Edad del paciente.
- Sexo: Sexo del paciente.
- exang: angina inducida por el ejercicio (1 = sí; 0 = no)
- ca: número de vasos principales (0-3)
- cp: tipo de dolor en el pecho tipo de dolor en el pecho
        Valor 1: angina típica
        Valor 2: angina atípica
        Valor 3: dolor no anginoso
        Valor 4: asintomático
- trtbps: presión arterial en reposo (en mm Hg)
- chol: colestoral en mg/dl obtenido mediante el sensor de IMC
- fbs: (azúcar en sangre en ayunas > 120 mg/dl) (1 = verdadero; 0 = falso)
- rest_ecg: resultados electrocardiográficos en reposo
- Valor 0: normal
        Valor 1: tener anomalía de la onda ST-T (inversiones de la onda T y/o elevación o depresión del ST > 0,05 mV)
        Valor 2: muestra hipertrofia ventricular izquierda probable o definitiva según los criterios de Estes
- tálaco: frecuencia cardíaca máxima alcanzada
        
### Equipo de Trabajo:

1. **Luis Gabriel Corrales Mora (Desarrollador de Software):** Responsable del montaje del código y la implementación del algoritmo.
2. **Cristian Vargas Jiménez (Infraestructura en la Nube y CI/CD):** Encargado de la configuración y mantenimiento de la infraestructura en la nube y del pipeline de CI/CD.
3. **Manuel Alejandro Espinoza Ramírez (Seguridad e Infraestructura):** Responsable de garantizar la seguridad del sistema y diseñar la infraestructura necesaria.

---

*"Si buscas resultados distintos, no hagas siempre lo mismo."* - Albert Einstein
