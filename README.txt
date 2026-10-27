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
Antes de criar os gráficos, vamos responder as questões levantadas.
Foi criado o arqvuivo: eda.py 
Respondidas as perguntas, não foi chegada a uma conclusão, pois a primeira pergunta - que traria uma melhor visão da virada dos votos, trouxe uma visão muito limitada do 'Todo'


PS D:\Estudos\Dados\Projetos\Modulo2 - ProjetoFinal - 2> git add .
PS D:\Estudos\Dados\Projetos\Modulo2 - ProjetoFinal - 2> git commit -m "Extraindo e transformando os dados para análise além de melhorar as perguntas e objetivo do trabalho"
[dev c9a5115] Extraindo e transformando os dados para análise além de melhorar as perguntas e objetivo do trabalho
 5 files changed, 60 insertions(+), 162 deletions(-)
 delete mode 100644 Dados/votacao_secao_2026_BR.csv
 delete mode 100644 Fontes/eda.py
PS D:\Estudos\Dados\Projetos\Modulo2 - ProjetoFinal - 2> git push
Enumerating objects: 34, done.
Counting objects: 100% (34/34), done.
Delta compression using up to 12 threads
Compressing objects: 100% (23/23), done.
Writing objects: 100% (24/24), 230.69 MiB | 7.09 MiB/s, done.
Total 24 (delta 8), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (8/8), completed with 6 local objects.
remote: error: Trace: 21674612c4d71898346ced2c2670f8e3b252307c6c6d16320426466944c7dc44
remote: error: See https://gh.io/lfs for more information.
remote: error: File Dados/votacao_secao_2026_BR.csv is 1499.95 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/DelioH/Eleicoes_2026.git
 ! [remote rejected] dev -> dev (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/DelioH/Eleicoes_2026.git'
PS D:\Estudos\Dados\Projetos\Modulo2 - ProjetoFinal - 2> 
