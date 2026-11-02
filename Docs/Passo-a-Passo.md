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

Fase 3: Validação unitária votos outros x ganhos 2T
Após verificar que a correlação entre os ganhos dos candidatos do primeiro turno tem uma correlação forte (e juntando isso a análise matemática inicial), foi gerada a correlação dos ganhos dos candidatos no segundo turno com os votos no primeiro turno. Para entender quem ganhou mais de qual candidato.
Chegou-se a seguinte matriz:
📊 MATRIZ DE CORRELAÇÃO DE PEARSON (Votos 1ºT vs Ganhos 2ºT):
              GanhoCandidato1  GanhoCandidato2
Candidato 3            0.9625           0.9835
Candidato 4            0.9789           0.9845
Candidato 5            0.9294           0.8950
Candidato 6            0.9380           0.9144
Candidato 7            0.9718           0.9836
Candidato 8            0.9663           0.9750
Candidato 9            0.9386           0.9611
Candidato 10           0.9560           0.9794
Candidato 11           0.9668           0.9815
Candidato 12           0.9633           0.9802
Candidato 13           0.9405           0.9594

Ou seja, os 2 candidatos tem uma correlação alta com os votos dos 'Outros'. Com exceção do Candidato 5 e do Cndidato 6, onde a correlação é maior par ao candidato 1 (embora sejam também as menores correlações), em todas as outras correlações, o candidato 2 se beneficiou mais do voto dos Outros.
Vamos agora para uma visão mais detalhada por estado. Será que em estados diferentes a correlação de ganhos com os Outros foi diferente? Qual foi o percentual por estado? Foi criado o script correlacao_por_estado.py 

📊 RESUMO ESTATÍSTICO POR ESTADO (UF):
UF  Municípios  Estoque Outros (1ºT)  Ganho Cand 1  Ganho Cand 2  Corr (Outros x Ganho C1)  Corr (Outros x Ganho C2)  Cresc. Médio C1 (%)  Cresc. Médio C2 (%)
SP         645               2456867       1217155       2613861                    0.9994                    0.9996                 7.25                25.36
MG         853               1010312        464238       1162163                    0.9950                    0.9979                 7.72                19.46
RJ          92                710222        202189        872372                    0.9905                    0.9996                 1.97                21.03
GO         246                587162        293446        396675                    0.9988                    0.9947                13.88                28.77
PR         399                585569        346099        511907                    0.9974                    0.9973                 7.08                20.14
RS         497                554757        300595        529793                    0.9957                    0.9928                 8.10                21.60
BA         417                453186        166176        820487                    0.9859                    0.9987                 6.84                10.96
SC         295                373893        220051        291146                    0.9856                    0.9885                 6.66                23.40
PE         185                309141         94511        563542                    0.9937                    0.9966                 4.28                13.94
CE         184                305878         62628        480861                    0.9903                    0.9983                 2.83                11.24
PA         144                272161         35983        263212                    0.9756                    0.9980                -0.89                 8.10
MA         217                205443         -9069        241930                    0.9263                    0.9879                -4.13                 7.37
DF           1                187622         69926        149597                       NaN                       NaN                 7.69                22.14
ES          78                167977         61310        151937                    0.9949                    0.9959                 4.51                15.62
AM          62                147085         -1519         98787                    0.9854                    0.9991                -5.99                 3.16
PB         223                141333         33833        252932                    0.9933                    0.9952                 2.16                13.57
RN         167                113505         16916        175633                    0.9844                    0.9977                -0.28                11.00
MT         142                113121         52518        112486                    0.9726                    0.9960                 2.51                16.60
PI         224                105708          8831        130279                    0.9868                    0.9973                -0.18                 5.90
MS          79                100148         54541        112118                    0.9952                    0.9955                 4.62                18.52
SE          75                 90395         15515        133022                    0.9888                    0.9969                 1.91                12.64
AL         102                 87752          8422        157162                    0.9831                    0.9960                -1.51                12.23
RO          52                 64470         21394         43779                    0.9109                    0.9996                 2.79                14.07
TO         139                 57145         -1405         38953                    0.9360                    0.9970                -2.63                 6.05
AP          16                 40094        -13604         10465                   -0.9795                    0.9924               -16.80                -4.77
AC          22                 31512        -15092          9743                    0.4711                    0.9884                -9.95                -0.29
ZZ         145                 29718         27597         42767                    0.8955                    0.8807                20.04                22.60
RR          15                 19817        -11647          9085                    0.1419                    0.9984               -12.29                 3.49

Com base nas informações avaliadas, os estados com maior quantidade de 'Outros' votos tiveram uma correlação muito forte com os ganhos dos candidatos; principalmente nos estados com mais de 100.000 votos de 'Outros'. Alguns estamos com menor quantidade tiveram algumas correlações bem divergentes entre os candidatos; mas não vamos considerar nesta análise, pois representam uma pequena parte do todo. Sobre o crecimetno médio, o candidato 2 conseguiu uma vantagem muito grande em relação ao candidato 1. Sendo o maior valor absoluto em SP, com quase 1,4 milhão de votos a mais de ganho em relação ao candidato 1. Agora, em percentuais, no RJ é o maior destaque, onde o candidato 1 teve um crescimento médio de 1,97% o candidato 2 obteve um crescimento médio de 21,03%. Em dados absolutos, foram 670.183 de votos a mais que o candidato 1.

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