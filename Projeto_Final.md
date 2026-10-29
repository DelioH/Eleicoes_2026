VISUALIZAÇÃO DE DADOS E BI [T1]
Projeto Avaliativo - Módulo 2 - Semana 13


SUMÁRIO
1. CONTEXTUALIZAÇÃO	1
2. DESAFIO	2
3. RESULTADOS ESPERADOS (ENTREGA)	2
3.1. ENTREGÁVEIS OBRIGATÓRIOS	3
3.2. REGRAS DE ENTREGA E INTEGRIDADE	3
4. REQUISITOS DA APLICAÇÃO	4
4.1. TEMA E DADOS PERMITIDOS	4
4.2. TEMA E DADOS NÃO PERMITIDOS	4
4.3. REQUISITOS FUNCIONAIS MÍNIMOS	5
4.4. BOAS PRÁTICAS E SEGURANÇA	5
5. ROTEIRO DA APLICAÇÃO	5
5.1. FORMATO DA SOLUÇÃO E PIPELINE	6
5.1.1. BIBLIOTECAS E FERRAMENTAS	7
5.1.2. HIERARQUIA RECOMENDADA E PASTAS	7
5.2. DOCUMENTAÇÃO NO README.MD	8
5.3. USO DO GITHUB	9
5.4. PUBLICAÇÃO DA SOLUÇÃO (STREAMLIT)	10
5.5. VÍDEO EXPLICATIVO E DIVULGAÇÃO	11
5.6. PIPELINE DO PROJETO	11
6. CRITÉRIOS DE AVALIAÇÃO	12
Observações finais	15


1. CONTEXTUALIZAÇÃO
A análise de dados apoia organizações na compreensão de problemas, no acompanhamento de resultados e na tomada de decisões com base em evidências. Profissionais da área precisam saber obter dados de forma responsável, avaliar sua qualidade, transformá-los, explorar padrões e comunicar conclusões de maneira clara para diferentes públicos.

Neste projeto final, cada aluno desenvolverá individualmente uma solução de análise de dados com Python, desde a definição de uma pergunta relevante até a publicação de uma aplicação interativa de Business Intelligence (BI) com Streamlit (https://share.streamlit.io/). O trabalho integra boas práticas de programação, estatística descritiva, visualização e documentação.

O tema é de livre escolha, desde que utilize dados públicos ou dados privados cujo uso esteja formalmente autorizado pela organização responsável. A escolha deve permitir uma análise segura, ética, viável no prazo e útil para responder a uma pergunta concreta.

2. DESAFIO
Planeje, desenvolva, documente e publique, de forma individual, um projeto completo que transforme dados em informação útil. A solução deve apresentar um problema ou oportunidade, explicar por que o tema importa, obter os dados por um método identificável, realizar a ETL (Extract, Transform, Load), e a EDA (Exploratory Data Analysis) bem como análises estatísticas com Python, além de disponibilizar uma interface de BI feita em Streamlit, publicada no serviço oficial de hospedagem do Streamlit.

Este projeto permite que seja verificada a sua capacidade de coletar, tratar, analisar, visualizar e interpretar dados utilizando Python e ferramentas modernas de análise, aplicando boas práticas de programação, estatística, limpeza de dados, exploração, modelagem básica, quando pertinente, e comunicação de insights.

Ao concluir, você deverá ser capaz de:

formular uma pergunta analítica objetiva e delimitar escopo, público e resultados esperados;
identificar, avaliar e citar uma fonte de dados e documentar como os dados foram obtidos;
implementar um processo reproduzível de ETL e registrar decisões de limpeza e transformação;
explorar os dados, calcular estatísticas adequadas e construir gráficos que apoiem a interpretação;
criar uma aplicação de BI interativa, compreensível e útil com Streamlit;
organizar código, pastas, tarefas, histórico de alterações e documentação em repositório individual;
comunicar limitações, achados, conclusões e possibilidades de uso profissional com responsabilidade.

3. RESULTADOS ESPERADOS (ENTREGA)

Você deverá entregar um projeto funcional e individual, com repositório pessoal dedicado, documentação completa, código de análise e aplicação Streamlit publicada. Também deverá publicar o projeto no repositório oficial da turma e compartilhar um vídeo explicativo de até 3 minutos em uma rede social profissional ou equivalente.
3.1. ENTREGÁVEIS OBRIGATÓRIOS
Repositório pessoal no GitHub dedicado exclusivamente ao projeto, com código, estrutura de pastas, README.md e instruções de execução.
Aplicação de BI em Streamlit publicada por deploy no serviço oficial do Streamlit; incluir no README o endereço público e instruções para acesso.
Dados ou instruções de obtenção reproduzíveis. Não publique dados privados, credenciais, tokens ou arquivos que não estejam autorizados para divulgação.
Documentação do projeto: objetivo, relevância, resultados esperados, fonte e método de captura, etapas de ETL, EDA, estatísticas, visualizações, resultados encontrados, conclusões e limitações.
Publicação do projeto no repositório oficial da turma, seguindo o procedimento e o prazo informados pelo professor.
Vídeo de até 3 minutos publicado no LinkedIn ou em outra rede social. Na publicação, marcar obrigatoriamente o professor (https://www.linkedin.com/in/rgbrunini/) , o LAB365 (https://www.linkedin.com/company/lab365/), o SENAI Santa Catarina (https://www.linkedin.com/school/senai-sc/) e a FIESC (https://www.linkedin.com/company/sistema-fiesc/).
Link do repositório pessoal, link do deploy, link da publicação do repositório da turma e link do vídeo enviados no ambiente de entrega indicado pelo professor, dentro do prazo.
3.2. REGRAS DE ENTREGA E INTEGRIDADE

Após submeter, evite alterar o conteúdo avaliado até a correção, salvo orientação do professor. Se uma correção técnica posterior for necessária, registre-a claramente. Trabalhos copiados, apresentados como próprios sem atribuição, ou que infrinjam regras de uso de dados poderão ser desconsiderados conforme as normas acadêmicas da instituição.
O código deverá ser inserido e versionado no GitHub em modo público e privado (se forem dados de empresas) e o vídeo deverá ser inserido no Google Drive em modo leitor para qualquer pessoa com o link. Os três links deverão ser disponibilizados na tarefa Módulo 2 - Projeto Avaliativo, presente na semana 13 do AVA até o dia 30/10/2026 às 22h.

Não serão aceitos projetos submetidos após a data limite da atividade, e, ou alterados depois de entregues.

Importante:
Será considerado como data final de entrega a última atualização no repositório do projeto no GitHub. Lembre-se de não modificar o código até receber sua nota.
Não esqueça de submeter os links no AVA. Os links não submetidos terão penalidade na nota.

4. REQUISITOS DA APLICAÇÃO
Os requisitos abaixo são obrigatórios, salvo quando identificados como recomendação. O tema precisa ser aprovado pelo professor quando houver dúvida sobre segurança, autorização, viabilidade ou adequação dos dados.
4.1. TEMA E DADOS PERMITIDOS
O aluno escolhe o tema. São permitidos dados públicos de fontes confiáveis ou dados privados fornecidos por uma empresa/organização, desde que exista autorização formal, assinada por representante autorizado, garantindo o uso dos dados para fins educacionais e definindo o que pode ser analisado, armazenado e divulgado. Antes de usar dados privados, o aluno deve entregar ou apresentar a autorização ao professor e seguir eventuais restrições de anonimização, acesso, retenção e publicação.
Exemplos de temas adequados: indicadores agregados de vendas ou estoque; dados abertos de mobilidade ou transporte; consumo energético agregado; preços de produtos; indicadores econômicos públicos; dados meteorológicos; catálogo público de livros ou filmes; dados de produção industrial sem identificação de pessoas; métricas de atendimento agrupadas e autorizadas; análise de acessibilidade de serviços a partir de dados públicos.
4.2. TEMA E DADOS NÃO PERMITIDOS
Não serão aceitos projetos que envolvam pesquisas médicas ou clínicas, dados pessoais sensíveis nos termos da LGPD, ou qualquer uso que possa expor, identificar, constranger ou colocar em risco pessoas ou animais. Os dados disponíveis na internet não são automaticamente livres para qualquer finalidade: o aluno deve verificar licença, termos de uso, direitos autorais e regras de acesso da fonte.
Dentre os exemplos não permitidos podemos citar: prontuários, exames, diagnósticos, tratamentos, histórico de saúde mental ou dados genéticos; informações sobre origem racial ou étnica, convicção religiosa, opinião política, filiação sindical, dados biométricos ou vida sexual; bases com nome, CPF, telefone, e-mail, endereço ou identificadores de clientes, alunos, funcionários ou pacientes; rastreamento individual de localização, rotina ou comportamento; imagens ou vídeos que identifiquem pessoas sem autorização; dados de crianças e adolescentes que possam identificá-los; experimentos ou análises que impliquem sofrimento, risco ou exposição de animais; rankings individuais que possam gerar discriminação, punição ou constrangimento.
Mesmo dados anonimizados ou agregados devem ser avaliados com cautela: grupos muito pequenos, combinações de variáveis ou recortes geográficos/temporais detalhados podem permitir a reidentificação. Em caso de dúvida, não colete nem publique os dados; converse com o professor e substitua a fonte por uma alternativa segura. A autorização da empresa não torna automaticamente adequado o uso de dados sensíveis ou de alto risco.
4.3. REQUISITOS FUNCIONAIS MÍNIMOS
A solução deve informar qual problema ou pergunta pretende responder e para quem os resultados são relevantes.
Deve obter dados por pelo menos um método documentado: API, consulta a banco de dados autorizado ou web scraping permitido pelos termos e regras do site. Também é válido utilizar arquivo público baixado de fonte oficial, descrevendo claramente a forma de obtenção.
Deve realizar ETL com Python: extração, transformação e carregamento/organização dos dados para análise. As decisões e regras aplicadas devem estar registradas.
Deve incluir EDA e estatísticas descritivas coerentes com o tipo de dado e a pergunta: distribuição, contagens, medidas resumo, comparações, tendências ou relações, conforme aplicável.
Deve apresentar gráficos legíveis, com títulos, eixos, unidades, legendas e fonte dos dados. As visualizações devem apoiar a resposta à pergunta, e não ser apenas decorativas.
Deve disponibilizar uma aplicação Streamlit com conteúdo analítico, navegação clara e pelo menos uma interação útil (por exemplo, filtros, seleção de período/categoria ou atualização de métricas), se compatível com o conjunto de dados.
Deve exibir avisos sobre limitações, recorte temporal, fonte e interpretação dos resultados, sem alegar causalidade quando a análise não a demonstrar.
O código deve poder ser executado a partir das instruções documentadas, sem depender de caminhos absolutos ou segredos expostos.
4.4. BOAS PRÁTICAS E SEGURANÇA

Use apenas dados necessários à pergunta; minimize a coleta e evite copiar bases completas sem necessidade.
Respeite licença, termos de serviço, limites de requisição e boas práticas de acesso. No web scraping, não contorne autenticação, bloqueios ou mecanismos de proteção.
Não coloque senhas, chaves de API, tokens ou credenciais no repositório. Utilize variáveis de ambiente e exemplos de configuração sem valores reais.
Se houver autorização para analisar dados privados, confirme explicitamente se também existe autorização para publicar resultados, gráficos, amostras ou a própria base. Quando a publicação não estiver autorizada, use dados sintéticos ou agregados aprovados.
Atribua as fontes, bibliotecas e referências utilizadas; identifique adaptações de exemplos externos. O trabalho e as decisões analíticas devem ser próprias do aluno.

5. ROTEIRO DA APLICAÇÃO
Siga a sequência a seguir. Registre as decisões à medida que avança: essa ação facilita a revisão, torna a análise reproduzível e ajuda a explicar o trabalho no README e no vídeo.
5.1. FORMATO DA SOLUÇÃO E PIPELINE
A solução deverá seguir obrigatoriamente o fluxo abaixo, documentando entradas, processos, saídas e decisões em cada etapa:

1. Documentação inicial: objetivo, importância e resultados esperados.
Descreva o contexto do problema, a pergunta que será investigada, quem poderia usar a resposta, por que o tema é relevante, o que está dentro e fora do escopo e quais resultados são esperados. Defina critérios realistas para considerar a análise concluída.

2. Fonte de dados e método de captura.
Informe o nome da fonte, endereço ou referência, responsável pela publicação, período e campos utilizados, licença ou termos relevantes e data de acesso. Explique se a coleta ocorre via API, banco de dados autorizado, web scraping permitido ou download de arquivo público. Descreva paginação, filtros, frequência e tratamento de falhas quando aplicável.

3. Ambiente de desenvolvimento e processo de ETL.
Utilize uma IDE ou ambiente de desenvolvimento Python. Organize a extração, transformação e carregamento em etapas claras. Trate tipos de dados, valores ausentes, duplicidades, inconsistências e formatos; registre critérios de exclusão ou correção e preserve, quando possível, uma cópia bruta que não seja publicada se houver restrição de uso.

4. EDA, estatística e gráficos.
Explore dimensões, tipos, qualidade, distribuição, tendências, grupos e relações relevantes. Escolha estatísticas adequadas à pergunta, explique o que significam e produza gráficos informativos. Registre resultados importantes e ressalvas; não confunda associação com causalidade.

5. Solução de BI em Streamlit.
Construa uma interface que apresente os indicadores e gráficos essenciais, permita explorar os dados de maneira simples e contextualize as conclusões. Inclua título, descrição, fonte, período, filtros pertinentes, interpretação dos indicadores e mensagens de erro ou ausência de dados quando necessário.

6. Deploy e verificação.
Publique a aplicação por meio do serviço oficial do Streamlit, conforme as instruções disponíveis no momento da publicação. Verifique se a aplicação abre publicamente, se os recursos carregam, se os dados estão autorizados para exibição e se o link foi incluído no README. Não inclua credenciais ou dados restritos no deploy.

7. Comunicação e conclusão.
No README, apresente os resultados encontrados, discuta o que eles indicam e o que não permitem concluir. Avalie a possibilidade de uso da solução em ambiente corporativo/profissional, incluindo valor potencial, limitações, riscos, requisitos de manutenção e melhorias futuras.

5.1.1. BIBLIOTECAS E FERRAMENTAS
Escolha bibliotecas documentadas e adequadas às etapas realizadas. A seleção deve ser justificada no README; não é necessário usar todas as opções abaixo.

Etapa
Exemplos de ferramentas
O que explicar
Coleta
requests/httpx, cliente oficial de API, SQLAlchemy ou ferramenta autorizada
Origem, autenticação segura, parâmetros, paginação e limites.
Tratamento e análise
pandas, NumPy
Regras de limpeza, transformações, tipos, validações e indicadores.
Estatística
SciPy, statsmodels ou recursos do pandas
Método escolhido, pressupostos e interpretação adequada.
Visualização
matplotlib, seaborn, plotly ou altair
Por que o gráfico é adequado e como deve ser lido.
Aplicação BI
Streamlit
Componentes interativos, filtros, métricas e publicação.


5.1.2. HIERARQUIA RECOMENDADA E PASTAS
Organize o repositório com nomes claros. A estrutura pode ser adaptada ao tema, desde que mantenha a separação entre aplicação, dados, análise e documentação. Não versione dados privados, credenciais nem arquivos que violem a licença da fonte.
Exemplo:

Caso a autorização assinada contenha dados pessoais ou informações empresariais confidenciais, não a publique no GitHub. Combine com o professor uma forma reservada de comprovar a autorização. No repositório, pode constar apenas uma declaração de que a autorização foi obtida, sem anexar o documento confidencial.

5.2. DOCUMENTAÇÃO NO README.MD

Crie um arquivo README.md na raiz do repositório pessoal. Ele deve permitir que outra pessoa entenda o projeto, confira as fontes, conheça os resultados e, quando permitido, execute a solução. Escreva com clareza, explique termos técnicos e use imagens ou diagramas somente quando ajudarem a compreensão.

Estrutura mínima obrigatória do README

Título e resumo: nome do projeto, descrição breve e assunto analisado.
Problema, objetivo e importância: pergunta orientadora, público interessado e relevância do tema.
Escopo e resultados esperados: o que será analisado, o que não será tratado e quais entregas analíticas se pretende obter.
Fonte e autorização: fonte, link, período, campos usados, licença/termos e método de captura; para dados privados, registrar que houve autorização formal, sem expor dados ou documentos confidenciais.
Pipeline e metodologia: etapas de extração, transformação, carregamento, exploração e estatística, com justificativa das principais decisões.
Bibliotecas e tecnologias: ferramentas utilizadas e função de cada uma; incluir documentação oficial ou referências relevantes.
Resultados encontrados: apresentar achados com números, gráficos ou tabelas pertinentes e explicar como respondem à pergunta do projeto.
Discussão e conclusão: interpretar resultados, reconhecer limites e indicar o que não pode ser inferido.
Aplicação profissional: discutir se e como o pipeline poderia ser usado em ambiente corporativo/profissional, requisitos de atualização, qualidade, segurança, privacidade, governança e manutenção.
Aplicação Streamlit: link do deploy, resumo das funcionalidades e instruções para navegação.
Como executar: pré-requisitos, instalação de dependências, configuração segura de variáveis, comando de execução e procedimento para obter os dados.
Estrutura de pastas: explicar os diretórios e arquivos principais.
Limitações e melhorias futuras: lacunas de dados, possíveis vieses, melhorias técnicas e análises futuras.
Créditos e referências: fontes de dados, bibliotecas, materiais consultados e contribuições externas.
Links de entrega: quadro de tarefas, repositório oficial da turma, publicação social e vídeo, conforme as regras da turma.
O README deve apresentar conclusões sustentadas pelas análises. Evite frases genéricas como “os dados mostram que...” sem indicar qual evidência sustenta a afirmação. Diferencie observação, hipótese e recomendação.

5.3. USO DO GITHUB

Utilize um repositório pessoal dedicado ao projeto, com histórico de versões e conteúdo organizado. O repositório deve permitir avaliar sua contribuição individual. Se o projeto exigir colaboração em alguma atividade de apoio, o desenvolvimento e a autoria da entrega avaliativa ainda devem estar claramente identificados como individuais.

Faça commits frequentes, pequenos e com mensagens objetivas no imperativo, por exemplo: “adiciona validação de dados ausentes” ou “cria filtro por período”.
Use branches para organizar o desenvolvimento. Recomenda-se manter main estável e utilizar develop e branches de funcionalidade quando forem úteis; o aluno deve explicar no README a estratégia adotada.
Não é obrigatório criar uma branch para cada microalteração, mas o histórico deve ser claro, coerente e demonstrar evolução real do projeto.
Inclua requirements.txt ou equivalente com as dependências necessárias e .gitignore para evitar arquivos temporários, ambientes virtuais, credenciais e dados indevidos.
Não publique segredos, arquivos de autorização confidenciais, dados privados ou material sem permissão. Revise o repositório antes de torná-lo público.
Inclua no README os links funcionais para a aplicação publicada e demais itens exigidos. Teste permissões e acesso antes da submissão.

5.4. PUBLICAÇÃO DA SOLUÇÃO (STREAMLIT)

A aplicação deve ser desenvolvida com Streamlit e publicada por deploy no serviço oficial do Streamlit. A interface deve apresentar valor analítico: indicadores e visualizações devem responder à pergunta orientadora e ser explicados de forma que um usuário não técnico compreenda seu significado.

Apresente título, objetivo, contexto, fonte dos dados e período analisado.
Organize a página em seções ou áreas de navegação de forma intuitiva.
Inclua filtros ou controles interativos quando agregarem valor, evitando opções sem utilidade para a pergunta.
Apresente rótulos, unidades, escalas e legendas adequados; sinalize filtros ativos e quantidade/recorte de dados exibidos.
Trate carregamento, erros, dados ausentes e indisponibilidade da fonte de forma compreensível.
Exiba limitações e observações importantes para evitar interpretações exageradas.
Confirme que a aplicação publicada não expõe dados ou credenciais não autorizados e que o link funciona para o avaliador.

O deploy deve utilizar apenas dados e configurações autorizados. Caso o projeto dependa de credenciais, configure-as de forma segura nas opções próprias do serviço, sem incluí-las no código ou em capturas de tela. O professor pode verificar a aplicação publicada como parte da avaliação.

5.5. VÍDEO EXPLICATIVO E DIVULGAÇÃO

Grave um vídeo com duração máxima de 3 minutos e publique-o no LinkedIn ou em outra rede social. A publicação deve marcar obrigatoriamente o professor, o LAB365, o SENAI Santa Catarina e a FIESC. Confirme os perfis corretos e as regras da plataforma com o professor; não invente marcações nem publique dados confidenciais.
Roteiro sugerido para até 3 minutos
0:00–0:30 — apresente seu nome, o tema, o problema e a pergunta que o projeto responde.
0:30–1:00 — mostre a fonte de dados e explique brevemente a forma de obtenção e as precauções adotadas.
1:00–1:45 — demonstre os principais passos de tratamento/análise e destaque um ou dois resultados encontrados.
1:45–2:30 — mostre a aplicação Streamlit e uma interação ou visualização importante.
2:30–3:00 — conclua com a utilidade potencial, uma limitação ou melhoria futura e indique onde acessar o projeto.

O vídeo deve ser objetivo, audível e respeitar o limite de tempo. Na descrição da publicação, inclua uma breve apresentação do projeto e o link do repositório ou do deploy, se permitido. Insira também o link da publicação/vídeo no README e na submissão, conforme orientação do professor. Você poderá gravar na vertical ou na horizontal. É importante que apareça seu rosto e esteja em um local com boa iluminação. Para realizar a entrega do vídeo, coloque em uma pasta do Google Drive em modo leitor para qualquer pessoa com o link, e compartilhe o mesmo na submissão do projeto no AVA. Uma dica interessante é você inserir o vídeo no readme.md do seu projeto no repositório do GitHub.

5.6. PIPELINE DO PROJETO


6. CRITÉRIOS DE AVALIAÇÃO
A tabela abaixo apresenta os critérios que serão avaliados durante a correção do projeto. O mesmo possui variação de nota de 0 (zero) a 10 (dez) como nota mínima e máxima, e possui peso de 60% sobre a avaliação do módulo. O professor pode ajustar prazos, pesos ou procedimentos administrativos e deverá comunicar eventuais mudanças à turma. A qualidade da análise será considerada junto com a clareza, a ética e a possibilidade de reproduzir ou compreender a solução.
Serão desconsiderados e atribuída a nota 0 (zero) os projetos que apresentarem plágio de soluções encontradas na internet ou de outros colegas. Lembre-se: Você está livre para utilizar outras soluções como base, mas não é permitida a cópia.

Apresentação do Projeto


Nº
Critério de Avaliação
0
1,00
1,5
1
Repositório oficial da turma e vídeo/divulgação
Itens não publicados ou vídeo excede o tempo/não cumpre marcações exigidas.
Entregas realizadas com algum link, marcação ou instrução incompleta.
Projeto publicado na turma e vídeo de até 3 min com marcações obrigatórias.


Uso adequado do GitHub e Readme.md


Nº
Critério de Avaliação
0
0,5
1,00
2
README, resultados e conclusão profissional
README ausente ou sem resultados e conclusão.
README parcial; resultados ou discussão profissional pouco desenvolvidos.
A documentação do repositório/projeto apresenta a arquitetura da solução completa, guia de instalação/execução, requisitos, decisões de projeto e diagramas/detalhes de funcionamento. 
3
Organização do repositório e versionamento
Repositório ausente/desorganizado ou sem evidência de versionamento adequado.
Estrutura e histórico presentes, com lacunas em organização ou instruções.
O repositório individual possui estrutura de arquivos/pastas organizada, mantendo boas práticas de versionamento, como o uso correto do .gitignore, ausência de arquivos desnecessários ou credenciais expostas.


Desenvolvimento da Aplicação


Nº
Critério de Avaliação
0
0,25
0,50
4
Definição do tema, objetivo e relevância
Não formulou uma pergunta/situação-problema contextualizada ou apresenta uma proposta vaga, sem delimitação do escopo técnico 
Identificou o tema e os objetivos do projeto, mas a justificativa de mercado/negócio apresentou lacunas ou o escopo técnico delimitado é amplo/restrito demais para o tempo de execução previsto no módulo 
Formulou uma situação-problema viável e contextualizada com a realidade profissional,  delimitando o escopo de execução, caracterizando com precisão o público-alvo impactado e justificando a relevância/aplicabilidade corporativa da solução. 
5
Adequação, origem e responsabilidade dos dados
Utilizou dados de procedência não identificada ou não autorizada, expondo a solução a riscos de privacidade/segurança e não documentou os métodos de extração/captura, nem especificou o recorte temporal ou as licenças de uso do conjunto de dados. 
Identificou a fonte dos dados e o método básico de captura, mas a documentação apresentou lacunas na especificação do recorte temporal, nas autorizações/licenças de uso ou nos procedimentos éticos de manipulação e anonimização dos dados. 
Selecionou e documentou de forma rigorosa fontes de dados adequadas à resolução do problema, detalhando o método de captura, o recorte temporal e as licenças/autorizações vigentes, bem como registrou os cuidados éticos, a conformidade legal e as rotinas de tratamento de dados sensíveis na documentação 
Nº
Critério de Avaliação
0
0,75
1,50
6
ETL e qualidade do processo
O ETL é ausente, não executável ou sem tratamento coerente.
O ETL funciona e é reproduzível, mas o código não possui organização modular clara ou falta documentação explicativa sobre as decisões de tratamento tomadas. 
Construiu pipeline de ETL organizando o código em etapas lógicas e reproduzíveis, documentando as decisões técnicas de tratamento de dados e justificando as transformações realizadas. 
7
EDA, estatística e visualizações
Não apresenta exploração ou gráficos úteis; interpretações sem apoio.
Escolheu gráficos adequados e legíveis, porém limitou-se a descrever o conteúdo na imagem, sem realizar inferências ou interpretações analíticas sobre o contexto técnico do problema. 
Construiu visualizações de dados adequadas ao tipo de variável e contexto, garantindo legibilidade estética (cores, eixos, rótulos e contraste) e elaborou inferências fundamentadas na análise dos resultados. 
8
Aplicação Streamlit e deploy
Aplicação ausente, inacessível ou sem relação com a análise.
A aplicação funciona e está publicada, porém a interface/navegação é confusa, ou a interatividade não foi aplicada quando necessária, comprometendo a experiência do usuário. 
A aplicação entregue encontra-se publicada (deploy ativo), funcional e com interface intuitiva/clara, disponibilizando recursos interativos condizentes com as necessidades da regra de negócio. 
Nº
Critério de Avaliação
0
0,50
1,00
9
Comunicação, ética e reprodutibilidade
Não explicou limites, expôs dados/segredos ou não permitiu compreender o processo.
Comunicação compreensível, mas com limitações ou cuidados pouco discutidos.
Comunicou as análises de forma compreensível, mas realizou conclusões precipitadas sem ressaltar limitações ou incertezas dos dados, ou apresentou falhas pontuais no alinhamento de práticas responsáveis. 
Comunicou os achados da análise de forma clara e objetiva, apresentando interpretações fundamentadas e cautelosas sobre as limitações dos dados, além de adotar práticas éticas e responsáveis no manuseio e compartilhamento das informações. 

Total: 10,00 pontos.
7. OBSERVAÇÕES FINAIS

Projetos com exposição indevida de dados pessoais, dados sensíveis, credenciais ou dados privados não autorizados poderão ser interrompidos e encaminhados para avaliação do professor, independentemente da qualidade técnica.
A autorização empresarial deve ser verificável, mas documentos confidenciais não devem ser publicados. A divulgação dos resultados depende do escopo da autorização.
A avaliação valoriza a autoria individual, a transparência metodológica e a capacidade de explicar escolhas e limitações. O uso de referências é permitido e incentivado quando citado; cópia não atribuída não é aceita.
Em caso de dúvida sobre tema, fonte, scraping, autorização, segurança ou deploy, consulte o professor antes de coletar ou publicar os dados.
