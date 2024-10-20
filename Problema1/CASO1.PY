import pandas as pd

# Cargar el archivo CSV
df_airbnb = pd.read_csv('data/airbnb.csv')

# Filtrar apartamentos con más de 10 críticas y una puntuación mayor a 4
alicia_filter = df_airbnb[(df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4)]

# Ordenar por 'overall_satisfaction' y luego por 'reviews' de forma descendente
alicia_filtered_sorted = alicia_filter.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

# Seleccionar las 3 mejores alternativas para Alicia
alicia_top3 = alicia_filtered_sorted.head(3)

# Mostrar las 3 mejores alternativas
print(alicia_top3)
