import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Podemos realizar comentarios donde no serán mostrados al usuario
# Podemos hacer uso de Markdown
st.markdown('''
#### Nombre: Miguel Eugenio Jurado García
#### Github Repo: [Haz Click Aqui](https://github.com/migeruj/streamlit-co2)
#### Github Profile: [Haz Click Aqui](https://github.com/migeruj)
'''
)

# Cargamos el CSV que se hace publico durante la actividad AG1
data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSUxc2WwWmZAC5oLb9qdcmMbaWG5Y5VL8Gu2w596ASMJJ40kVZYMjN5sV_RoejjcO8D4cyjt-O0qZz5/pub?gid=0&single=true&output=csv')

st.markdown('''# Muestra de los datos''')
st.write(data.head(5))

st.markdown('''# Limpieza''')
data.drop(['https://datosmacro.expansion.com/energia-y-medio-ambiente/emisiones-co2', 'Países', 'Var.'], axis=1, inplace=True)
data['CO2 Totales Mt'] = data['CO2 Totales Mt'].apply(lambda x: x.replace('.', ''))
data['CO2 Totales Mt'] = data['CO2 Totales Mt'].apply(lambda x: x.replace(',', '.'))
data['CO2 Totales Mt'] = pd.to_numeric(data['CO2 Totales Mt'])
data['CO2 Kg/1000$'] = data['CO2 Kg/1000$'].apply(lambda x: x.replace(',', '.'))
data['CO2 Kg/1000$'] = pd.to_numeric(data['CO2 Kg/1000$'])
data['CO2 t per capita'] = data['CO2 t per capita'].apply(lambda x: x.replace(',', '.'))
data['CO2 t per capita'] = pd.to_numeric(data['CO2 t per capita'])
data['Variación'] = data['Variación'].apply(lambda x: x.replace(',', '.'))
data['Variación'] = data['Variación'].apply(lambda x: x.replace('%', ''))
data['Variación'] = pd.to_numeric(data['Variación'])

st.write(data.head(5))

st.title('Visualization AG1')
st.markdown('G1: Top 10 Países en Emisiones totales de CO2 en Mt')
### Se puede usar pyplot directamente
ag1 = data.sort_values("CO2 Totales Mt", ascending=False)[0:10]
fig1 = plt.figure(figsize=(10, 4))
plt.pie(ag1['CO2 Totales Mt'],labels = ag1['País'])
st.pyplot(fig1)

### O seaborn si te gustan mas sus graficos
st.markdown('G2: Top 10 Países en Emisiones totales de CO2 en Mt')
fig2 = plt.figure(figsize=(12, 4))
sns.barplot(x='País', y='CO2 Totales Mt', data=ag1)
st.pyplot(fig2)