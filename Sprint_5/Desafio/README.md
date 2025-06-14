# 🚀 Desafio 

## 📌 Resumo

Neste desafio da Sprint 5, o objetivo foi construir um Data Lake na AWS, aplicando na prática os conceitos de ingestão, armazenamento e organização de dados em nuvem. O tema escolhido para a análise foi a evolução da representação feminina em filmes de guerra ao longo das décadas, buscando entender tanto a participação de mulheres nos elencos, quanto a presença de diretoras e possíveis variações por região geográfica.

A primeira etapa do desafio foi a definição dos questionamentos, baseados em uma análise exploratória inicial do arquivo movies.csv e nas possibilidades de enriquecimento dos dados via API do TMDB. Essa definição foi fundamental para direcionar todas as demais etapas de ingestão e processamento de dados. Na sequência, realizei a ingestão batch dos dados locais, utilizando Python e a biblioteca boto3 para o envio dos arquivos CSV ao Amazon S3, organizando-os na camada RAW do Data Lake, seguindo o padrão de particionamento por tipo de dado e data de processamento.

Na segunda etapa, desenvolvi um processo de ingestão via API, com foco na coleta de informações complementares dos filmes selecionados, utilizando uma função AWS Lambda. O desenvolvimento foi organizado em etapas, desde a prototipação inicial até a execução final, detalhadas nas seções a seguir, contendo os arquivos e as evidências de cada etapa:



## 🗂️ Sumário 

1. [Etapa 1](#etapa-1)



<br>

---

# Etapa 1

Nessa etapa do desafio, realizei a leitura e análise de dois arquivos: o movies.csv e o CSV gerado a partir da extração de dados da API do TMDB, ambos contendo informações detalhadas sobre filmes lançados. Assim, criei dois notebooks separados para realizar a análise exploratória de cada conjunto de dados, entendendo a estrutura e a qualidade das informações disponíveis. A partir dessa análise inicial, defini a linha de investigação que seguirei nas próximas etapas, focando na evolução da representação feminina em filmes de guerra ao longo das décadas. Nas seções seguintes, detalharei os códigos utilizados e os questionamentos estratégicos definidos.

| Arquivo | Link |
|--------|------|
|  | [🔗 ]() |
| | [🔗 ]() |

<br>

> Explicação 


**Análise inicial**

Como mencionado anteriormente, iniciei essa parte realizando a leitura e análise dos conjuntos de dados: o arquivo movies.csv e o CSV gerado a partir da extração de dados da API do TMDB. Para organizar melhor o processo, optei por criar dois notebooks separados no Jupyter, essa separação me permitiu comparar as duas bases e entender de forma mais clara como elas poderiam se complementar nas próximas etapas. Durante essa análise exploratória, fui também avaliando se os dados disponíveis seriam suficientes para responder aos questionamentos que eu tinha interesse em investigar.

A partir dessas análises iniciais, optei por seguir uma linha de investigação voltada para a evolução da representação feminina em filmes de guerra ao longo das décadas. A escolha desse tema foi motivada pelo interesse em explorar como a participação das mulheres tem evoluído nesse contexto, considerando tanto aspectos quantitativos (como a proporção de mulheres nos elencos e a presença de diretoras) quanto qualitativos (como o perfil dos papéis desempenhados pelas personagens femininas e possíveis variações regionais na produção desses filmes).

Além disso, busquei também comparar a representatividade feminina em relação à masculina ao longo das décadas, entendendo como esse cenário tem se transformado com o tempo. Para garantir uma base de análise mais consistente e focada em filmes com maior relevância dentro do gênero, apliquei alguns filtros iniciais, considerando apenas filmes de guerra lançados a partir de 1950, com nota média maior ou igual a 6 e com pelo menos 100 votos registrados no TMDB, o que ajudou a garantir uma amostra com dados mais representativos e de melhor qualidade para análise.


![Evidência 1](../Evidências/Evidencia1.png)

<br>

**Questionamentos**

Por meio da análise inicial, foi possível identificar as principais informações e dados presentes no arquivo CSV e da API. Com base nisso, selecionei oito questionamentos principais:


- Qual a média da proporção de mulheres nos elencos de filmes de guerra em cada década?

Objetivo: analisar a evolução histórica da participação feminina nos elencos ao longo do tempo.

- Como evoluiu a proporção entre homens e mulheres nos elencos principais desses filmes?

Objetivo: investigar se houve mudanças no equilíbrio de gênero entre os papéis principais.

- Quais filmes de guerra tiveram o maior e o menor percentual de mulheres no elenco?

Objetivo: destacar os filmes de guerra que apresentaram os maiores e menores percentuais de mulheres no elenco, evidenciando casos de maior inclusão ou de baixa representatividade feminina.

- Há diferença na recepção crítica (nota média e número de votos) entre filmes com maior presença feminina e os com menor presença feminina?

Objetivo: avaliar se existe alguma correlação entre a representatividade feminina e a avaliação do público.

- Qual o perfil das personagens femininas nesses filmes?

Objetivo: investigar se as mulheres ocupam papéis de destaque (protagonistas, oficiais, guerreiras) ou se predominam em papéis secundários.

- Como a participação feminina varia entre as diferentes décadas e qual a relação com a presença de diretoras ou cineastas mulheres?

objetivo: relacionar a evolução da representatividade feminina no elenco com a atuação de diretoras.

- Quais diretoras estão associadas a uma maior representatividade feminina nos filmes de guerra?

Objetivo: mapear quais cineastas contribuíram para ampliar a diversidade de gênero nesse gênero cinematográfico.

- Existe alguma tendência regional ou país onde a presença feminina nos filmes de guerra é maior?

Objetivo: analisar se determinadas regiões ou países apresentam maior inclusão de mulheres em seus elencos de filmes de guerra.


<br>

