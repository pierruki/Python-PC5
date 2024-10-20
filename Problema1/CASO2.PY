import pandas as pd

# Cargar el archivo CSV
df_airbnb = pd.read_csv('data/airbnb.csv')

# IDs de las casas de Roberto y Clara
roberto_id = 97503
clara_id = 90387

# Filtrar las propiedades de Roberto y Clara
roberto_clara_filter = df_airbnb[df_airbnb['room_id'].isin([roberto_id, clara_id])]

# Guardar el DataFrame filtrado como un archivo Excel (ahora con extensión .xlsx)
roberto_clara_filter.to_excel('roberto.xlsx', index=False)

# Mostrar el DataFrame filtrado
print(roberto_clara_filter)

