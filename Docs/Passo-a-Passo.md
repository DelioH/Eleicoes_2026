👣 Passo a Passo: Construção do Projeto de BI (Eleições)

Este documento descreve a jornada metodológica e técnica percorrida desde a definição da ideia até o deploy da aplicação em Streamlit, evidenciando as decisões de negócio, a exploração matemática e os desafios de Engenharia de Dados.

Passo 1: Ideação e Definição do Escopo

O projeto começou com a exploração de diversos temas que utilizassem dados públicos. Optou-se pela Análise das Eleições, especificamente a dinâmica de virada entre o 1º e o 2º turno, por oferecer um volume massivo de dados e a oportunidade de responder a uma pergunta analítica clara: Como se deu a virada de votos? Foi pela redução de abstenção, redução de Brancos/Nulos, ou pela conversão de votos de outros candidatos?

Decisão chave: Limitar o escopo inicial aos dados agregados para entender a matemática da virada, deixando a análise complexa de horários de urnas (após 17h) e cruzamentos socioeconômicos (IDH) para uma "Fase 2".

Passo 2: Coleta de Dados (extracao)

Fonte: Portal de Dados Abertos do TSE.

Arquivo: detalhe_votacao_secao_2026.zip.

Desafio Técnico: O arquivo bruto continha 5.731.614 linhas e 26 colunas.

Solução: Criado um script de extração utilizando pandas para ler o arquivo localmente, garantindo que o ambiente suportasse o volume de dados na memória.

Passo 3: Limpeza e Transformação (transformacao)

Não era viável carregar 5.7 milhões de linhas em uma aplicação web (Streamlit). O processo de transformação precisou otimizar isso, agrupando os dados de seções para municípios.

Agrupamento: Utilizamos a função groupby do Pandas para somar os votos das seções por município, turno e candidato, focando apenas em 6 colunas essenciais (NR_TURNO, SG_UF, CD_MUNICIPIO, NM_MUNICIPIO, NM_VOTAVEL, QT_VOTOS).

Resultado: A base foi comprimida de 5.7M para 89.669 linhas, gerando o arquivo votacao_agrupada_2026.csv, altamente otimizado para análises e o BI.

Passo 4: Análise Exploratória (EDA) e a Matemática da Virada

Esta foi a etapa mais densa do projeto. Para evitar suposições rasas, a análise foi dividida em duas fases: a descoberta matemática no cenário Macro (Nacional) e a validação estatística no cenário Micro (Municipal).

Fase 1: Análise Macro (O Todo)

Primeiro, foi calculado os totais nacionais para entender o tamanho do "buraco" que o candidato vencedor precisou preencher.

A Diferença: O candidato vencedor teve um salto de +10.376.694 votos no 2º turno. De onde vieram?

Mapeamento das Fontes de Voto:

Redução de Abstenção gerou +2.960.239 votos (representa no máximo 28,5% da diferença).

Redução de Brancos/Nulos gerou +1.816.000 votos (representa no máximo 17% da diferença).

Eleitores de outros candidatos do 1º turno formavam um 'estoque' de 9.321.993 votos (potencial de 89,8% da diferença).

A Dedução dos 54,5%: Somando o impacto da abstenção (28,5%) com os brancos/nulos (17%), temos 45,5%. Em um cenário extremo, mesmo que absolutamente todas essas novas pessoas tivessem votado no candidato vencedor, a conta não fecharia. Restariam 54,5% da diferença (cerca de 5,6 milhões de votos). Portanto, a matemática macro comprova que a virada foi decidida primariamente pela conversão de votos de terceiros. Aqui trata-se de uma conta matemática e uma suposição, pois não conseguimos comprovar que todos que votaram no primeiro turno votaram no segundo e e ainda assim que eles votaram nos mesmos candidatos (considerando candidato 1 e candidato 2).
Importante: Opto aqui por não exibir os nomes dos candidatos ou partidos políticos ao longo da análise. O objetivo é preservar a neutralidade do estudo e direcionar o foco exclusivamente para os aspectos estatísticos e metodológicos dos dados, promovendo uma discussão estritamente acadêmica e imparcial.

Fase 2: Validação Municipal (Correlações)

Sabendo que a conversão foi o fator predominante no "Todo", precisávamos validar se isso se sustentava município a município. Criamos a base_correlacao_2026.csv organizando os turnos para aplicar a Correlação de Pearson.

Estabilidade Eleitoral: O resultado do 2º turno mudou a geografia dos votos?

Descoberta: A correlação entre os votos do 1º e 2º turno para ambos os candidatos foi de 0.9995. Isso provou que não houve "bagunça" geográfica; as bases originais (redutos) foram mantidas.

Origem dos Votos (A Conversão Local): Os ganhos do 2º turno ocorreram nas cidades onde havia muitos votos de "Outros" no 1º turno?

Descoberta: A correlação entre Outros_T1 e o GanhoCandidato no 2º turno foi extremamente forte (> 0.985 para ambos).

Média de Crescimento:

Descoberta: Ao isolar o crescimento por município, o Candidato 2 teve média de 17.1% e mediana de 16.6%, contra média de 5.2% e mediana de 5.9% do Candidato 1, mostrando uma captação pulverizada e consistente em todo o país.

Passo 5: Desenvolvimento do Dashboard (Streamlit)

Com a tese validada pelo Pandas (a virada se deu por conversão, mantendo a estabilidade regional), o Streamlit foi construído para visualizar essas descobertas.

Estrutura: O painel foi dividido em 3 partes para responder às perguntas principais criando uma 'contagem de histórica' (storytelling) dos dados. Iniciando pelo primeiro tudo, com os dados da votação para os candidatos (votos válidos), passando para os votos brancos e nulos.
Na segunda parte, foi criado um gráfico para demonstrar o 'estoque de votos' disponível para os candidatos no 2o turno e também ao lado como ficou a votação comparativamente do primeiro e segundo turno somente dos candidatos que disputaram o segundo turno.
Na terceira parte foi apresentado o gráfico de dispersão, que prova a estabilidade do crescimento dos candidatos na região. Importante: Neste gráfico, cada ponto significa uma cidade. Foi tomado o cuidade de, ao passar o mouse por cima de cada ponto exibir a informação da cidade, votos no primeiro turno e ganho no segundo turno. Embora exista essa estabilidade, visualmente é possível ver que o crescimento do candidato 2 é muito mais expressivo; fato este que é melhor evidenciado no gráfico de linhas ao lado que mostra de onde partiram e onde chegaram cada um dos candidatos; do primeiro ao segundo turno.
Abaixo, foi criada uma tabela com os dados separados por cidade; informando os dados de quantidade de votos no primeiro e segundo turno, ganhos (absolutos) e crescimento dos 2 candidatos. A tabela pode inclusive ser baixada para futuras análises.

Filtros Inteligentes: Durante a EDA, descobrimos distorções nos extremos de vantagem proporcional devido a cidades minúsculas na Zona Exterior (ZZ) - ex: Havana, Ramallah. Por isso, incluímos filtros de cidade e estado (onde pode-se remover o estado ZZ que é a nomenclatura utilizada para exterior).

Performance: Utilizamos @st.cache_data para carregamento instantâneo.

Conclusão

O projeto foi muito além de plotar gráficos. Ele atendeu aos requisitos do pipeline analítico: partiu de uma dúvida de negócio, processou big data (5.7M de linhas) usando ETL  em Python, utilizou estatística dedutiva (cálculo de potenciais máximos) e indutiva (correlação de Pearson) para desmistificar o fenômeno da virada, e culminou em uma aplicação web interativa baseada em dados matematicamente validados. Para trabalhos futuros, sugiro:
- Cruzamentos socioeconomicos: Integrar dados socioeconomicos como IDH, renda media por capta, grau de urbanização, grau de saneamento básico, assim como proporção de beneficiários de programas sociais, aposentados entre outros para correlacionar com a taxa de crescimento dos candidatos.
- Utilizar dados de eleições anteriores para comparar as dinâmicas de segundo turno e ganhos dos candidatos.
- Correlação da rejeição dos candidatos com a migração de votos dos outros candidatos.