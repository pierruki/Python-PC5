import pandas as pd

# Cargar el archivo CSV
df_airbnb = pd.read_csv('data/airbnb.csv')

# Filtrar propiedades que sean "Shared room" y cuyo precio sea menor o igual a 50€
diana_filter = df_airbnb[(df_airbnb['room_type'] == 'Shared room') & (df_airbnb['price'] <= 50)]

# Ordenar las propiedades por mejor puntuación (overall_satisfaction)
diana_sorted = diana_filter.sort_values(by='overall_satisfaction', ascending=False)

# Seleccionar las 10 propiedades más baratas
diana_top10 = diana_sorted.head(10)

# Mostrar las propiedades seleccionadas
print(diana_top10)
