import pandas as pd
import os
from pymongo import MongoClient

# Ruta de la carpeta donde están los archivos
folder_path = './data/0303'

# Obtener la lista de archivos de texto relevantes (excluir log.txt)
files = [f for f in os.listdir(folder_path) if f.endswith('.txt') and f != 'log.txt']

# Lista para almacenar cada DataFrame
df_list = []

# Leer y combinar los archivos de texto
for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, sep='\t', header=None)  # Lee el archivo sin encabezados
    df_list.append(df)

# Concatenar todos los DataFrames en uno solo
df_youtube = pd.concat(df_list, ignore_index=True)

# Verificar el número de columnas en los datos
print(f"Número de columnas en el archivo: {df_youtube.shape[1]}")

# Mostrar las primeras filas para ver todas las columnas
print(df_youtube.head())

# Quedarse solo con las columnas que necesitamos
df_relevant = df_youtube[[0, 2, 3, 6, 7]]  # Ajustar si es necesario a la estructura de tu archivo
df_relevant.columns = ['VideoID', 'age', 'category', 'views', 'rate']

# Mostrar las primeras filas con las columnas seleccionadas
print(df_relevant.head())

# Conectar a MongoDB
client = MongoClient("mongodb+srv://Pieronanezdiaz:QXb-S%40L*-7Si46*@cluster0.fsp84.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['PythonPC5']
collection = db['Grafica_3']

# Insertar los datos filtrados en MongoDB
data_to_insert = df_relevant.to_dict(orient='records')
result = collection.insert_many(data_to_insert)

# Mostrar mensaje de éxito
print("Impresión exitosa")
