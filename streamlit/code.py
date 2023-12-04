import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
df = pd.read_csv('../csv/csv_limpios/jugadores_completo.csv')

# Mostrar los datos en Streamlit
#st.write(df)

#Filtro por posición
opciones_posicion = ['Todas'] + list(df['Posicion'].unique())
opcion_posicion = st.sidebar.selectbox('Elige una posición', opciones_posicion)

if opcion_posicion == 'Todas':
    df_filtrado_por_posicion = df
else:
    df_filtrado_por_posicion = df[df['Posicion'] == opcion_posicion]

st.write(df_filtrado_por_posicion)


# Edad
# Agrupar por edad y calcular estadísticas del valor de mercado
df_agrupado = df.groupby('Edad')['Valor de mercado'].mean()

# Calcular la edad promedio
edad_promedio = df['Edad'].mean()

# Crear un gráfico de barras para el valor de mercado promedio
plt.figure(figsize=(10, 6))
plt.bar(df_agrupado.index, df_agrupado.values)
plt.axhline(y=edad_promedio, color='r', linestyle='-', label=f'Edad Promedio: {edad_promedio:.2f}')
plt.title('Distribución del Valor de Mercado Promedio Según la Edad')
plt.xlabel('Edad')
plt.ylabel('Valor de Mercado Promedio')
plt.legend()
plt.grid(True)

# Mostrar el gráfico en Streamlit
st.pyplot(plt)