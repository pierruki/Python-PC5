import pandas as pd

# Cargar el archivo CSV
df_wine = pd.read_csv('data/winemag-data-130k-v2.csv')

# Mostrar las primeras 5 filas
print(df_wine.head())

# Revisar las columnas del dataset
print(df_wine.columns)

# Resumen estadístico
print(df_wine.describe())

# Renombrar columnas
df_wine.rename(columns={
    'country': 'pais',
    'points': 'puntuacion',
    'price': 'precio',
    'winery': 'bodega'
}, inplace=True)

# Crear nuevas columnas
# Crear columna para el continente basado en un mapeo de países
# Aquí puedes usar el archivo de países para mapear el continente
continente_mapping = {
    'US': 'América', 'France': 'Europa', 'Italy': 'Europa', 'Chile': 'América', 'Argentina': 'América', 
    'Spain': 'Europa', 'Australia': 'Oceanía', 'South Africa': 'África', 'Portugal': 'Europa'
}
df_wine['continente'] = df_wine['pais'].map(continente_mapping)

# Crear columna que clasifique los vinos por rango de precios
df_wine['rango_precio'] = pd.cut(df_wine['precio'], bins=[0, 20, 50, 100, 500], labels=['Bajo', 'Medio', 'Alto', 'Muy Alto'])

# Crear columna que muestre la relación precio/calidad (puntuación/precio)
df_wine['calidad_precio'] = df_wine['puntuacion'] / df_wine['precio']

# Mostrar las primeras 5 filas para revisar los cambios
print(df_wine.head())

# Reporte 1: Por continente, mostrar los vinos mejor puntuados
reporte_1 = df_wine.groupby('continente').apply(lambda x: x.nlargest(1, 'puntuacion'))
print("Reporte 1 - Mejor puntuado por continente")
print(reporte_1)

# Reporte 2: Promedio de precio de vino y cantidad de reviews obtenidos según país, ordenado de mejor a peor
reporte_2 = df_wine.groupby('pais').agg({
    'precio': 'mean',
    'puntuacion': 'mean',
    'description': 'count'
}).sort_values(by='puntuacion', ascending=False)
print("\nReporte 2 - Promedio de precio, puntuación y cantidad de reviews por país")
print(reporte_2)

# Reporte 3: Vinos más baratos por país
reporte_3 = df_wine.groupby('pais').apply(lambda x: x.nsmallest(1, 'precio'))
print("\nReporte 3 - Vinos más baratos por país")
print(reporte_3)

# Reporte 4: Promedio de calidad/precio por continente
reporte_4 = df_wine.groupby('continente').agg({
    'calidad_precio': 'mean'
}).sort_values(by='calidad_precio', ascending=False)
print("\nReporte 4 - Promedio de calidad/precio por continente")
print(reporte_4)

# Exportar reporte 1 a CSV
reporte_1.to_csv('reporte_mejor_puntuado.csv', index=False)

# Exportar reporte 2 a Excel
reporte_2.to_excel('reporte_promedio_precios.xlsx')

# Exportar reporte 3 a SQL (se necesita sqlite3 o SQLAlchemy)
import sqlite3
conn = sqlite3.connect('reporte_vinos.db')
reporte_3.to_sql('reporte_vinos_baratos', conn, if_exists='replace', index=False)

# Exportar reporte 4 a JSON
reporte_4.to_json('reporte_calidad_precio.json')
