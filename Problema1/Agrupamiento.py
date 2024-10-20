import pandas as pd

# Cargar el archivo CSV
df_airbnb = pd.read_csv('data/airbnb.csv')

# 1. Agrupamiento por tipo de habitación para obtener el precio medio y la satisfacción promedio
grouped_room_type = df_airbnb.groupby('room_type').agg({
    'price': 'mean',
    'overall_satisfaction': 'mean'
})

print("Agrupamiento por tipo de habitación:")
print(grouped_room_type)

# 2. Agrupamiento por vecindario para ver cuántas propiedades hay por vecindario
grouped_neighborhood = df_airbnb.groupby('neighborhood').size().reset_index(name='property_count')

print("\nAgrupamiento por vecindario:")
print(grouped_neighborhood)
