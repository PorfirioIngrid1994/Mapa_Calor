import pandas as pd
import plotly.express as px

# Dados:

# Cidades:
Cidades = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Brasília', 'Manaus', 'Porto Alegre', 'Recife', 'Belo Horizonte']
Estados = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Distrito Federal', 'Amazonas', 'Rio Grande do Sul', 'Pernambuco', 'Minas Gerais']

# Latitudes
Latitudes = [-23.5505, -22.9068, -12.9711, -15.8267, -3.4653, -30.0346, -8.0472, -19.9227]

# Longitudes
Longitudes = [-46.6333, -43.1729, -38.5108, -47.9218, -62.2159, -51.2177, -34.8777, -43.9451]

# Valor hipotético de vendas
Vendas = [500, 400, 100, 300, 150, 200, 270, 340]

# Criação de um dicionário para organizar os dados
Dicionario = {
    'Cidades': Cidades,
    'UF': Estados,
    'Lat': Latitudes,
    'Lon': Longitudes,
    'Vendas': Vendas
}

# Usar o pandas para organizar em um data frame:
Base_Dados = pd.DataFrame(Dicionario)
Base_Dados

# Criação do mapa de calor:
fig = px.density_mapbox(
    Base_Dados,
    lat='Lat',
    lon='Lon',
    z='Vendas',
    radius=30,
    center=dict(lat=-3.4653, lon=-62.2159),
    zoom=7,
    mapbox_style='stamen-terrain'
)

fig.show()
