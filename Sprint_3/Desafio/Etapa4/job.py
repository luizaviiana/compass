import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv_limpo.csv')

aparecimentos = df['Artist'].value_counts()
artista_destaque = aparecimentos.idxmax()
quantidade = aparecimentos.max()
df_artista = df[df['Artist'] == artista_destaque]
media_faturamento = df_artista['Actual gross'].mean()

resposta_q1 = (
    "Q1:\n\n"
    f"A artista que mais aparece na lista é {artista_destaque}, com um total de {quantidade} turnês.\n"
    f"Essas turnês faturaram em média ${media_faturamento:,.2f} cada uma.\n\n"
)

df_turnes_anuais = df[df['Start year'] == df['End year']]
df_maior_media_1ano = df_turnes_anuais.sort_values(by='Average gross', ascending=False)
turne_mais_lucrativa_1ano = df_maior_media_1ano.iloc[0]

resposta_q2 = (
    "Q2:\n\n"
    f"A turnê mais lucrativa, considerando apenas as que começaram e terminaram no mesmo ano, "
    f"foi '{turne_mais_lucrativa_1ano['Tour title']}' da cantora {turne_mais_lucrativa_1ano['Artist']}.\n"
    f"A média de faturamento dessa turnê foi ${turne_mais_lucrativa_1ano['Average gross']:,.2f}.\n\n"
)

df['Lucro por show'] = df['Adjusted gross (in 2022 dollars)'] / df['Shows']
top3 = df.sort_values(by='Lucro por show', ascending=False).head(3)

resposta_q3 = "Q3:\n\n"
resposta_q3 += "Essas são as 3 turnês com maior faturamento por show individual:\n"
for _, row in top3.iterrows():
    resposta_q3 += f"- '{row['Tour title']}', da artista {row['Artist']}, arrecadou em média ${row['Lucro por show']:,.2f} por apresentação.\n"
resposta_q3 += "\n"

with open('/app/volume/respostas.txt', 'w', encoding='utf-8') as f:
    f.write(resposta_q1)
    f.write(resposta_q2)
    f.write(resposta_q3)

artista_destaque = df['Artist'].value_counts().idxmax()
df_artista_destaque = df[df['Artist'] == artista_destaque]
faturamento_anual = df_artista_destaque.groupby('Start year')['Actual gross'].sum().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(faturamento_anual.index, faturamento_anual.values, marker='o', color='hotpink')
plt.title(f'Faturamento por Ano das Turnês de {artista_destaque}', fontsize=14)
plt.xlabel('Ano de Início da Turnê')
plt.ylabel('Faturamento Bruto (USD)')
plt.grid(True)
plt.tight_layout()
plt.savefig('/app/volume/Q4.png')
plt.show()

shows_por_cantora = df.groupby('Artist')['Shows'].sum()
top5_shows = shows_por_cantora.sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6))
top5_shows.plot(kind='bar', color='mediumorchid')
plt.title('Top 5 Cantoras com Mais Shows nas Turnês', fontsize=14)
plt.xlabel('Artista')
plt.ylabel('Número Total de Shows')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('/app/volume/Q5.png')
plt.show()
