import pandas as pd

# Ruta del archivo descomprimido
file_path = 'ruta_a_los_datos.txt'

# Leer los datos, el separador es '\t' (tabulador), y no hay encabezados
df_youtube = pd.read_csv(file_path, sep='\t', header=None)

# Asignar nombres a las columnas (basado en la descripción proporcionada)
df_youtube.columns = ['VideoID', 'uploader', 'age', 'category', 'length', 'views', 'rate', 'ratings', 'comments', 'relatedIDs']

# Mostrar las primeras 5 filas para verificar los datos
print(df_youtube.head())

# Seleccionar las columnas que vamos a usar: VideoID, edad, categoria, views, rate
df_filtered = df_youtube[['VideoID', 'age', 'category', 'views', 'rate']]

# Mostrar las primeras 5 filas del DataFrame filtrado
print(df_filtered.head())

# Filtrar el DataFrame para seleccionar solo las filas con una categoría específica (ejemplo: 'Music')
df_music = df_filtered[df_filtered['category'] == 'Music']

# Mostrar las primeras 5 filas del DataFrame filtrado
print(df_music.head())

from pymongo import MongoClient

# Conectarse a MongoDB
client = MongoClient('localhost', 27017)

# Crear una base de datos y una colección
db = client['youtube_data']
collection = db['videos']

# Convertir el DataFrame filtrado a un diccionario para poder insertarlo en MongoDB
data_dict = df_filtered.to_dict('records')

# Insertar los datos en la colección
collection.insert_many(data_dict)

print("Datos exportados a MongoDB.")

import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico 1: Distribución de visualizaciones (views) por categoría
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='views', data=df_filtered)
plt.title('Distribución de visualizaciones por categoría')
plt.xticks(rotation=90)
plt.show()

# Gráfico 2: Relación entre la edad del video y la tasa de calificación (rate)
plt.figure(figsize=(10, 6))
plt.scatter(df_filtered['age'], df_filtered['rate'])
plt.title('Relación entre la edad del video y la tasa de calificación')
plt.xlabel('Edad del video (días)')
plt.ylabel('Tasa de calificación')
plt.show()
