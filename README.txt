*26.10.2026*
Perguntas:
5 cidades com maior votação proporcional de cada candidadato (2 mais bem posicionados)
5 cidades com maior alteração de quantidade de eleitores (que tiveram mais votos). Considero aqui a quantidade de votos
5 cidades maior quantidade de nulos e brancos.
Impacto das Urnas apuradas depois das 17 horas.
Em quantas cidades cada um ganhou

Dados disponíveis em:
https://dadosabertos.tse.jus.br/dataset/resultados-2026
Localizar o item:
Detalhe da apuração por seção eleitoral
Arquivo: https://cdn.tse.jus.br/estatistica/sead/odsele/detalhe_votacao_secao/detalhe_votacao_secao_2026.zip

Campos:
DT_GERACAO	HH_GERACAO	ANO_ELEICAO	CD_TIPO_ELEICAO	NM_TIPO_ELEICAO	NR_TURNO	CD_ELEICAO	DS_ELEICAO	DT_ELEICAO	TP_ABRANGENCIA	SG_UF	SG_UE	NM_UE	CD_MUNICIPIO	NM_MUNICIPIO	NR_ZONA	NR_SECAO	CD_CARGO	DS_CARGO	NR_VOTAVEL	NM_VOTAVEL	QT_VOTOS	NR_LOCAL_VOTACAO	SQ_CANDIDATO	NM_LOCAL_VOTACAO	DS_LOCAL_VOTACAO_ENDERECO

Tópicos de estudo:
Questão principal: Como se deu a virada de votos de votação?
Foi pela redução de abstenção? Foi pela redução de Brancos e Nulos? Houve alguma mudança nos estados em que os candidatos ganharam?
1. Vantagem Proporcional: Quais são os cinco municípios onde cada um dos dois candidatos finalistas obteve a maior margem percentual de votos?

2. Variação de Engajamento: Quais cinco cidades apresentaram a maior variação absoluta no total de votos registrados (crescimento ou queda) entre o primeiro e o segundo turno?

3. Incidência de Votos Inválidos: Em quais cinco municípios ocorreu a maior proporção de votos brancos e nulos, indicando menor engajamento direto com as chapas finalistas?

4. Análise de Horário (Condicional): Existe alguma variação estatística no padrão de resultados das urnas que registraram votos após as 17 horas em comparação ao cenário geral de apuração? Vai depdender se essa informação estará disponível.

5. Questão extra: Dos cinco maiores e menores dentro de cada Estado e ver se encontra alguma relação (População, IDH, e etc.)

*Extração dos dados*
Foram encontradas 26 columnas e 5.731.614 linhas

*Transformação dos dados*
Considerando que não vamos precisar utilizar os dados específicos por sessão e várias colunas, o arquivo original foi simplificado, agrupando os dados principais para análise. Restaram apenas as colunas:
NR_TURNO	SG_UF	CD_MUNICIPIO	NM_MUNICIPIO	NM_VOTAVEL	QT_VOTOS
Resultando assim, em um aruqivo contendo 6 colunas e 89.669 linhas.
Gerado o arquivo votacao_agrupada_2026.csv.
Amostra dos dados:
NR_TURNO SG_UF  CD_MUNICIPIO NM_MUNICIPIO               NM_VOTAVEL  QT_VOTOS
0         1    AC          1007       BUJARI       AUGUSTO JORGE CURY       165
1         1    AC          1007       BUJARI  CLARIANA ZACARKIM BARAO         3
2         1    AC          1007       BUJARI     EDMILSON SILVA COSTA         3

*Análise exploratório*
Antes de começar a criar os gráficos e responder as perguntas tema da análise, optou-se por fazer uma análise superficial dos dados para entender melhor a situação dos 2 turnos da eleição.
Perguntas:
- Quantos pessoas/votos tivemos por turno (votos nominais e brancos/nulos)?
- Qual a quantidade de votos para cada um dos candidados nos 2 turnos?
- Quanto houve de diferença do primeiro turno em relação ao segundo
Analisando os dados, tivemos as seguinte informações:
No primeiro turno tivemos 125.275.835 votos, sendo 5.969.801 brancos e nulos
Já no segundo turno tivemos 128.236.074 votos, sendo 4.153.801 brancos e nulos
Sendo assim, do primeiro para o segundo turno, tivemos um aumento de 2.960.239 votos totais 
Além disso, tivemos uma redução dos votos brancos/nulos. de 5.969.801 para 4.153.801
Um total de 1.816.000 a mais de votos válidos.
Ou seja, no total, tivemos 4.776.239 (2.960.239 + 1.816.000) votos a mais.
Ou:
(128.236.074 - 4.153.801) = 124.082.273 votos válidos
(125.275.835 - 5.969.801) = 119.306.034 votos válidos
Considerando somente votos válidos, tivemos (124.082.273 - 119.306.034) = +4.776.239 votos válidos, ou seja: +4%

Agora, olhando o cenários dos candidados que foram para o segundo turno, tivemos:
FLAVIO NANTES BOLSONARO
  1º Turno: 56.104.503
  2º Turno: 59.826.041
  Diferença: +3.721.538, ou seja, +6,7%

LUIZ INÁCIO LULA DA SILVA
  1º Turno: 53.879.538
  2º Turno: 64.256.232
  Diferença: +10.376.694, ou seja, +19,26%

O segundo candidato virou a eleição no segundo turno, embora o primeiro candidato tenha tido crescimento em relação ao primeiro turno.
Agora, considerando os votos totais válidos do primeiro turno; podemos dizer que ele absorveu todos os outros votos?
AUGUSTO JORGE CURY: 3.448.569
CLARIANA ZACARKIM BARAO: 40.043
EDMILSON SILVA COSTA: 22.693
HERTZ DA CONCEICAO DIAS: 43.103
LEONARDO ALVES DE ARAUJO: 5.246
RENAN ANTONIO FERREIRA DOS SANTOS: 2.675.887
ROMEU ZEMA NETO: 326.488
RONALDO RAMOS CAIADO: 2.605.148
RUI COSTA PIMENTA: 15.024
SAMARA MARTINS DA SILVA FEITOSA: 122.911
WILSON GRASSI JUNIOR: 16.881
Somando todos os votos dos outros candidatos, tem-se 9.321.993 votos válidos, junto com o o que tivemos a mais de votos no segundo turno +4.776.239 e subtraindo os votos que foram para o primeiro candidato, -3.721.538,
temos: (9.321.993 + 4.776.239) - 3.721.538 = 10.376.694 que é a quantidade a mais de votos do segundo candidato em relação ao segundo turno.
Com este cenário, vamos nos aprofundar na análise para entender melhor de onde veio esta diferença.

Antes de criar os gráficos, vamos responder as questões levantadas.
Foi criado o arqvuivo: analise_exploratorio.py 
Respondidas as perguntas, não foi chegada a uma conclusão, pois a primeira pergunta - que traria uma melhor visão da virada dos votos, trouxe uma visão muito limitada do 'Todo'




