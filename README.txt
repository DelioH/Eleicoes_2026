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
Foi criado o arqvuivo: analise_exploratorio.py.
Respondidas as perguntas, não foi chegada a uma conclusão, pois:
 a primeira pergunta - que traria uma melhor visão da virada dos votos, trouxe uma visão muito limitada do 'Todo'
 a segunda pergunta - trouxe um pouco de luz sobre o assunto, mas pouco relevante; entre as cidades que tiveram maior quantidade de voto em relação ao segundo turno, tivemos as maiores cidades do país; talvez uma análise relativa fizesse mais sentido
 a terceia pergunta - foi bem parecida com a resposta atnerior, exceto por brasília, tiveram a mesma ordem (grandes cidades)
Vamos voltar a objeto do estudo: 
Como se deu a virada de votos de votação?
Foi pela redução de abstenção? Foi pela redução de Brancos e Nulos? Houve alguma mudança nos estados em que os candidatos ganharam?
Embora as respostas as perguntas não tenham ajudado a elucidar totalmente a virada, entendemos que:
- Embora a redução da abstenção, a redução de votos brancos e nulos e a conversão de votos de outras candidaturas não possam ser cravadas como os fatores únicos independentes (já que nenhum somado separadamente chega ao valor de diferença de votos do candidato que virou),
 eles com certeza auxiliaram. Agora a questão é responder é: Quais fatores tiveram maior relavancia na virada dos votos?
 Em um universo de 14.098.232 (entre redução da abstenção, redução de votos brancos/nulos e conversão de votos), sendo que 10.376.694 foi o total da diferença, o que cada um dos fatores pode ter representado para a virada das eleições?
 1 - Redução na abstenção - +2.960.239 votos (pode representar até 28,5% (2.960.239 / 10.376.694))
 2 - Redução de votos Brancos/Nulos - +1.816.000 votos (pode representar até 17% (1.816.000 / 10.376.694))
 3 - Conversão de votos - +9.321.993 votos (pode representar até 89,8% (9.321.993 / 10.376.694))
Agora a pergunta que fica é: Qual fator foi mais predominante na virada das eleições?
Considerando que o primeiro e o segundo fator tivessem se convertido predominantemente em votos para o segundo candidato, o percentual máximo de representação seria de 45,5%
Desta forma, podemos concluir que a conversão de votos foi responsável por, no mínimo 54,5% (equivalente a 5.655.298 votos) da conversão de votos; ou sejam o maior fator determinante para o resultado da virada das eleições.
Esse votos bastariam para o candidato ganhar a eleição?
Votos do segundo candidato no primeiro turno + conversão dos outros candidatos: 53.879.538 + 5.655.298 = 59.534.836, contra 59.826.041.
Ou seja, só a conversão de votos dos outros candidatos não bastariam para o segundo candidato ganhar.
*Importante*: Estou considerando que os votos ganhados no primeiro turno pelos 2 candidatos não foram convertidos para o outro, nem se tornaram brancos ou nulos (o que também é uma hipótese)

Por conta disso, vamos analisar algumas correlações.
1 - Estabilidade eleitoral: Verificar se no segundo turno seguiu o mesmo padrão geográfico de votos. Assim, verificamos se houve uma mudança no padrão do voto.
Responde a pergunta: O resultado do segundo turno foi consistene com o primeiro turno? (análise nacional)
2 - Origem dos votos: Agora sim, correlacionar os fatores que identificamos na primeira análise que norteam a distribuição dos votos (Abstenção, Votos brancos e nulos e conversão de votos de outros candidatos)
Responde a pergunta: De onde podem ter vindo os votos do segundo turno?

1 - Estabilidade eleitoral
Para gerar essa correlação, foi necessário criar uma nova fonte de dados, já com os dados ajustados para gerar a correlação.
Foram criados os seguintes campos:
UF - Estado
Município
Candidato1_T1 - Votos no candidato 1 no 1o. turno. Pela ordem alfabética, o candidato do PL
Candidato2_T1 - Votos no candidato 2 no 1o. turno. Pela ordem alfabética, o candidato do PT
Outros_T1 - Votos nos outros candidatos no 1o. turno.
BrancosNulos_T1 - Votos em branco e nulos no 1o. turno. (agrupados os 2 pois não vamos correlacionar os 2 separadamente)
Candidato1_T2 - Votos no candidato 1 no 1o. turno. Pela ordem alfabética, o candidato do PL
Candidato2_T2 - Votos no candidato 2 no 1o. turno. Pela ordem alfabética, o candidato do PT
BrancosNulos_T2 - Votos em branco e nulos no 1o. turno. (agrupados os 2 pois não vamos correlacionar os 2 separadamente)
GanhoCandidato1 - Quantidade de votos que o candidato 1 ganhou no segundo turno.
GanhoCandidato2 - Quantidade de votos que o candidato 2 ganhou no segundo turno.
Votantes_T1 - Total de votantes no 1o. Turno.
Votantes_T2 - Total de votantes no 2o. Turno.
Var_Votantes - Votantes_T2 - Votantes_T1
Var_Votantes_Perc - Percentual Var_Votantes
Importante: Foi utilizada o nome Votantes, pois não temos a quantidade de eleitores por seção / município. Para uma futura análise, pode ser utilizada esta informação.
Desta forma, isto vai funcioanr da seguinte forma: Se em um municípo 1.000 pessoas votaram no primeiro turno e 900 no segundo, as variáveis serão:
Votantes_T1 = 1000
Votantes_T2 = 900
Var_Votantes = 900 - 1000 = -100
Var_Votantes_Perc = -100/1.000 = -10%

Criada a fonte de dados 'base_correlacao_2026.csv'que já será capaz de fazer as 2 correlações propostas

Para a primeira correlação vamos comparar os votos do candidato 1 no primeiro turno com os votos dele no segundo turno (Candidato1_T1 x Candidato1_T2)
e vamos comparar os votos do candidadato 2 no primeiro turno com os votos dele no segundo turno (Candidato2_T1 x Candidato2_T2)

Gerado gráfico de dispersão da correlação 1
os 2 candidatos tiveram uma correlação exata de 0.9996 cada um
O que sugere uma correlação forte.
Só para ter certeza se realmente eles tem a mesma correlação, vamos alterar para mostrar 10 casas decimais na correlação.
Agora sim, tem uma diferença:
Correlação Candidato 1:
0.9995793420
Correlação Candidato 2:
0.9995710227
na geração do grafico de dispersão, foi juntados os 2 gráficos lado a lado para entender melhor.
Essa correlação forte quer dizer que os 2 candidatos mantiveram o padrão de votos nos municípios.
Baseado neste resultaod, vamos agora correlacionar os ganhos, para ver como seguem o padrão; para entender se onde os candidatos já eram fortes, cresceram mais aidna
Para entender melhor, agora foi feita uma nova correlação agora dos ganhos do candidato 1 e do candidato 2. Chegou-se a seguinte informnação:
Correlação Ganhos Candidato 1:
0.9511234405

Correlação Ganhos Candidato 2:
0.9892407229

POde-se entender desta forma que os 2 candidatos tiveram um padrão de votação muito correlacionados no primeiro e segundo turno; 
já os ganhos embora muito correlacionados, foram mais estáveis para o candidato 2.

Talvez possamos medir essa estabilidade de crescimento com a media, mediana e desvio padrão e gerar um bloxpot. 
Aqui não estamos pensando no valor absoluto de crescimento, mas na estabilidade.
Adicionado indicador no analise da correlação.
Os resultados: (uma ressalva: o candidato 1, teve municípios em que ele não obteve voto; foi necesário filtrar os dados dele para fazer o calculo - mas pela própria contagem, foram só 2 municípios).
Resultado do cálculo:
Crescimento do Candidato 1
count    5714.000000
mean        5.201758
std         6.825783
50%         5.912112
Crescimento do Candidato 2
count    5716.000000
mean       17.160483
std         9.183709
50%        16.666667

Bom, foram diferenças pequenas entre a média e a mediana do candidato 1, mas existem e são proporcionamente maiores que do candidato 2. 
Mas o que mais me chamou atenção, embora não fosse o objetivo, é que a média de crescimento do candidato 2 foi bem maior, mais de 3,3 (se comparado com a média) e 2,8 se comparado a mediana.
Ou seja; os 2 cresceram, mas o candidato 2 muito mais e de forma mais equilibrada (diferença entre média e mediana). 

Agora vamos partir para a segunda correlação.







