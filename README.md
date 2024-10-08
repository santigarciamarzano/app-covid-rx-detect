# RX-COVID Detect App

## Introducción

Esta aplicación utiliza Streamlit para detectar si una imagen de rayos X corresponde a un caso de COVID-19 o es una imagen normal. La detección se basa en un modelo previamente entrenado, cuyos pesos están almacenados en el archivo best_model.h5.

El modelo fue entrenado en un proyecto diferente, cuyo repositorio puedes encontrar en https://github.com/santigarciamarzano/COVID-RX-DenseNet121-train-detect.git

---

## Requisitos e Instalación

Clona este repositorio:

```bash

git clone https://github.com/tu-usuario/rx-covid-detect-app.git
cd rx-covid-detect-app
```

Instala las dependencias desde el archivo requirements.txt:

```bash

pip install -r requirements.txt
```

Ejecuta la aplicación:

Para iniciar la app en local, simplemente ejecuta el siguiente comando:

```bash

streamlit run app.py
```

Puedes instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```
---

Es importante crear una carpeta "uploads" en el directorio raíz dónde se alojará la imagen a analizar.

## Uso

Sube una imagen de rayos X.
La aplicación clasificará la imagen como COVID-19 o Normal utilizando el modelo entrenado.


## Docker

La aplicación también está dockerizada, lo que significa que puedes correrla dentro de un contenedor Docker para mayor portabilidad.

