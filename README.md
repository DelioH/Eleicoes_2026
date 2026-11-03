# 📊 Análise da Dinâmica e Virada Eleitoral (1º e 2º Turno - 2026)

## 1. Título e Resumo
O projeto consiste em uma análise aprofundada sobre a dinâmica de votação, abstenções e transferência de votos entre o 1º e o 2º turno das eleições brasileiras de 2026. Através do cruzamento de dados oficiais do Tribunal Superior Eleitoral (TSE), a aplicação investiga os fatores matemáticos e geográficos que determinaram a virada eleitoral.

## 2. Problema, Objetivo e Importância
*   **Pergunta Orientadora:** Como se deu a virada de votos no 2º turno? O resultado foi impulsionado pela redução da abstenção, pela redução de votos brancos e nulos, ou pela conversão de votos de outros candidatos?
*   **Público Interessado:** Analistas de dados, estrategistas de campanhas, jornalistas políticos e cidadãos interessados em transparência eleitoral.
*   **Importância:** Compreender as raízes estatísticas de uma virada eleitoral permite desmistificar narrativas políticas, baseando as conclusões em evidências matemáticas sólidas sobre estabilidade eleitoral e origem dos votos.

## 3. Escopo e Resultados Esperados
O escopo abrange a totalidade dos municípios brasileiros e zonas no exterior. Os resultados esperados incluem um dashboard interativo (utilizando o StreamLit) capaz de apresentar:
*   A proporção de conversão de votos de terceiros candidatos.
*   Cidades com maiores variações de engajamento (abstenção e comparecimento).
*   Análise de estabilidade eleitoral (se o padrão de votação do 1º turno se manteve no 2º).
*   *Fora do escopo (Fase 1):* Análises condicionais envolvendo o horário de apuração das urnas (após as 17 horas) e fatores socioeconômicos (IDH).

## 4. Fonte e Autorização
*   **Fonte Oficial:** Tribunal Superior Eleitoral (TSE) - Repositório de Dados Abertos.
*   **Base Utilizada:** Detalhe da apuração por seção eleitoral de 2026 (`detalhe_votacao_secao_2026.zip`).
*   **Captura e Licença:** Arquivo público oficial de livre acesso obtido via download direto do repositório do TSE. Os dados são agregados por seção/município e não ferem a Lei Geral de Proteção de Dados (LGPD).

## 5. Pipeline e Metodologia (ETL e EDA)
*   **Extração (E):** Leitura de arquivo bruto contendo 5.731.614 linhas e 26 colunas.
*   **Transformação (T):** Agrupamento dos dados focando nas colunas essenciais (`NR_TURNO`, `SG_UF`, `CD_MUNICIPIO`, `NM_MUNICIPIO`, `NM_VOTAVEL`, `QT_VOTOS`). A base foi filtrada (cargo 'Presidente') e reduzida para 89.669 linhas no arquivo `votacao_agrupada_2026.csv`. Foi criada também a base `base_correlacao_2026.csv` para cálculos de correlação.
*   **Análise Exploratória (EDA):** Testes estatísticos de média, mediana, desvio padrão e correlação de Pearson para medir a estabilidade e o padrão de crescimento dos candidatos finalistas.

## 6. Bibliotecas e Tecnologias
*   **Pandas & NumPy:** Utilizados no processo de ETL para filtragem, agrupamento (groupby) e cálculos estatísticos de correlação.
*   **Streamlit:** Framework escolhido para o desenvolvimento do Dashboard.

## 7. Resultados Encontrados
*   **Fator de Virada:** A conversão de votos (de candidatos eliminados no 1º turno) representou a maioria do potencial da diferença, sendo responsável por, no mínimo, 54,5% (cerca de 5,6 milhões de votos) da conversão real que consolidou a virada eleitoral, minimizando o impacto exclusivo de abstenções ou nulos. Esse dado é baseado em números, porém não pode ser tomado como uma verdade absoluta pois, como não temos acesso ao voto de cada eleitor e se o mesmo votou no primeiro ou no segundo turno ou em ambos não temos como marcar essa resultado incontestável.
*   **Estabilidade Eleitoral Forte:** A correlação geográfica entre os votos do 1º e 2º turno foi extremamente forte para ambos os candidatos (>0.999), demonstrando que as bases regionais foram mantidas de forma consistente.
*   **Média de Crescimento:** O Candidato que obteve a virada apresentou um crescimento de votos no 2º turno substancialmente maior (média de 17.1% e mediana de 16.6% por município) em comparação ao oponente (média de 5.2% e mediana de 5.9%).
*   **Origem dos Votos:** Houve uma fortíssima correlação (> 0.985) entre os ganhos no 2º turno e a quantidade de votos recebida por "Outros Candidatos" no 1º turno, evidenciando uma associação direta na transferência pulverizada de votos a nível municipal (o que dá mais força ao primeiro resultado matemático encontrado).
*   **Correlação de origem dos votos entre cada um dos candidatos do primeiro turno com os ganhos dos finalistas no seguno turno** Criar uma matriz de correlação entre cada candidato que foi para o segundo turno e cada candidato que ficou no primeiro turno, para entender a correlação entre os votos para os outros candidatos do primeiro turno e os que ficaram para o segundo turno.

## 8. Discussão e Conclusão
A hipótese inicial de que a virada seria pautada unicamente por grandes variações de abstenção ou votos brancos/nulos não se sustentou como fator isolado. A análise comprova que, embora tenham auxiliado (representando 28,5% e 17% do potencial da diferença, respectivamente), a eleição foi decidida de fato pela eficiência na captação (conversão) dos eleitores de chapas eliminadas no 1º turno, com uma manutenção rigorosa do padrão geográfico de votação.

## 9. Aplicação Profissional
Este pipeline analítico possui forte aplicabilidade no mercado de inteligência política, jornalismo de dados e consultoria estratégica. Institutos de pesquisa poderiam adaptar o código para consumir as bases do TSE, monitorando tendências de abstenção ou calculando zonas de maior aderência para campanhas de segundo turno, otimizando investimentos e logística de campanha.

## 10. Aplicação Streamlit (Dashboard de BI)
*   **Link do Dashboard:** https://eleicoes2026-jp6fwhf3fmfeze3fbgbqul.streamlit.app/
*   **Resumo:** O dashboard permite explorar as variações de engajamento, visualizar os rankings de vantagem proporcional por estado e investigar as viradas eleitorais, filtrando os dados para evitar distorções de urnas do exterior. Além disso, traz informações detalhadas por munícipio ou por estado em uma tabela com os dados de votação.

## 11. Como Executar o Projeto
1.  Garanta a instalação do Python e das bibliotecas: 'pip install pandas streamlit'
2.  Extraia o arquivo bruto do TSE ('detalhe_votacao_secao_2026.csv') na pasta '/dados'
3.  Execute a extração e transformação: 'python fontes/transformacao.py'
4.  Crie o arquivo para correlação: 'python fontes/ger_base_analise_correlacao.py'
5.  Gere as análises exploratórias: 'python fontes/analise_exploratorio_inicial.py', 'python fontes/analise_exploratorio.py', 'python fontes/analise_correlacao_1.py', 'python fontes/analise_correlacao_2.py'
6.  Crie o ambiente virtual para utilização do StreamLit:
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install streamlit
    pip install pandas matplotlib ploty

6.  Inicie o painel BI com o comando: `streamlit run BI-StreamLit/app.py`

## 12. Estrutura de Pastas
*   '/dados': Contém os CSVs brutos e os otimizados.
*   '/fontes': Armazena os scripts Python de ETL e EDA (transformacao.py, analise_exploratorio_inicial.py, analise_exploratorio.py, analise_correlacao_1.py, analise_correlacao_2.py).
*   '/BI-StreamLit/app.py': Arquivo principal da aplicação Streamlit.


## 13. Limitações e Melhorias Futuras
*   **Limitações:** A análise estatística mede *associações matemáticas* agregadas por município, não rastreando a transferência individual do eleitor (o que é impossível devido ao sigilo do voto). 
*   **Melhorias Futuras (Fase 2):** Utilização de regressão para encontrar as 'transferencias' de votos dos candidatos que não foram para o segundo turno para o segundo turno.Inclusão de dados detalhados de logs para medir o impacto de urnas apuradas após as 17h, além do cruzamento com indicadores do Atlas Brasil (IDH) para entender o perfil socioeconômico das cidades com maiores índices de virada.

## 14. Links de Entrega
*   **Repositório Oficial da Turma:** `[Inserir Link]`
*   **Repostiório pessoal:** https://github.com/DelioH/Eleicoes_2026
*   **Vídeo Explicativo (YouTube):** `[Inserir Link]`
*   **Dashboard StreamLit:** https://eleicoes2026-jp6fwhf3fmfeze3fbgbqul.streamlit.app/