# Comparação Tarefa 7 × Tarefa 8

## 1. Objetivo

Verificar se as avaliações registradas na Tarefa 7 são estáveis sob mudanças controladas de versão e/ou esforço de raciocínio. A comparação usa o mesmo artefato, os mesmos critérios e, sempre que possível, o mesmo prompt.

## 2. Linha de base da Tarefa 7

| Critério | Claude — T7 | Grok — T7 | Gemini — T7 | ChatGPT — T7 | Selo oficial |
|---|---|---|---|---|---|
| D | Atende, com ressalvas | Atende | Parcialmente verificável | Pendente de conferir resposta original | Atribuído |
| F | Execução parcial | Atende, com limitações | Não verificável | Pendente de conferir resposta original | Atribuído |
| S | Atende, com ressalvas | Atende | Não verificável | Pendente de conferir resposta original | Atribuído |
| R | Reprodução parcial, com divergências | Atende, com limitações | Não verificável | Pendente de conferir resposta original | Atribuído |

O resumo documental existente registra resultados para Claude, Grok e Gemini. A responsável também informou que ChatGPT foi usado na Tarefa 7 e que todas as respostas originais estão guardadas. Até que a resposta do ChatGPT seja recuperada e conferida, seus resultados permanecem pendentes; não devem ser inferidos. O registro da Tarefa 7 informa que o IoT-ID recebeu os quatro selos oficiais. Para a comparação formal, confirmar os termos exatos nas respostas originais. A tabela é uma síntese qualitativa, não uma equivalência automática entre “atende” e concessão formal de selo.

## 3. T8 — primeira resposta registrada: GPT-6, esforço padrão

A resposta está preservada em [T8_GPT6_PADRAO.md](T8_GPT6_PADRAO.md). A interface exibiu “GPT-6”; a versão exata não foi informada. A análise registrou uma tentativa de clonagem que falhou por resolução DNS e não confirmou execução do pipeline IoT-ID. Assim, a primeira resposta permite comparar a análise declarada pelo modelo, mas ainda não permite concluir que o artefato foi reproduzido.

| Critério | T7: ChatGPT | T8-GPT6-01: resposta registrada | Mudança T7→T8? | Estado da evidência |
|---|---|---|---|---|
| D | Pendente de conferir resposta original | Disponibilidade pública/documental considerada favorável | Não determinável | Revisão independente pendente |
| F | Pendente de conferir resposta original | Funcionalidade não confirmada por execução | Não determinável | Pipeline não executado; arquivos citados precisam ser conferidos |
| S | Pendente de conferir resposta original | Estrutura considerada favorável, com ressalvas | Não determinável | Inferência estrutural; sem avaliação longitudinal |
| R | Pendente de conferir resposta original | Reprodutibilidade independente não verificada | Não determinável | Resultados de referência não foram repetidos |

**Não concluir que os critérios mudaram.** A comparação não é possível até recuperar a resposta original de ChatGPT na T7 e verificar as evidências citadas na resposta T8. Além disso, a versão exata do modelo T8 não está informada, o que limita a reprodução da configuração.

## 4. Tabela comparativa T7 × T8

Preencher uma linha por critério e variante.

| Provedor/família | Critério | T7: decisão | T8: decisão | Mudança? | Evidência T7 | Evidência T8 verificada | Execução | Relação com selo oficial |
|---|---|---|---|---|---|---|---|---|
| Claude | D | Atende, com ressalvas | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Claude | F | Execução parcial | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Claude | S | Atende, com ressalvas | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Claude | R | Reprodução parcial, com divergências | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Grok | D | Atende | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Grok | F | Atende, com limitações | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Grok | S | Atende | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Grok | R | Atende, com limitações | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Gemini | D | Parcialmente verificável | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Gemini | F | Não verificável | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Gemini | S | Não verificável | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| Gemini | R | Não verificável | Pendente | Pendente | Consultar T7 | Pendente | Pendente | Pendente |
| ChatGPT | D | Pendente de conferir resposta original | Favorável quanto à disponibilidade pública, provisório | Não determinável | Recuperar resposta T7 | Revisão independente pendente | Clonagem falhou; não é teste do critério D em si | Pendente |
| ChatGPT | F | Pendente de conferir resposta original | Não confirmada por execução | Não determinável | Recuperar resposta T7 | Arquivos citados precisam ser conferidos | Pipeline não executado | Pendente |
| ChatGPT | S | Pendente de conferir resposta original | Estrutura favorável, com ressalvas | Não determinável | Recuperar resposta T7 | Revisão independente pendente | Sem teste longitudinal | Pendente |
| ChatGPT | R | Pendente de conferir resposta original | Não verificada independentemente | Não determinável | Recuperar resposta T7 | Revisão independente pendente | Resultados de referência não repetidos | Pendente |

## 5. Como interpretar as diferenças

Classificar cada comparação como:

- **Estável:** decisão e sustentação por evidências permanecem equivalentes.
- **Mudança sustentada:** a decisão muda e a variante apresenta evidência nova, verificável e pertinente.
- **Mudança não sustentada:** a decisão muda, mas a justificativa não apresenta evidência nova suficiente.
- **Diferença de acesso/ambiente:** a mudança decorre de acesso ou capacidade de execução diferente; não deve ser atribuída automaticamente à versão/esforço.
- **Inconclusiva:** não há dados suficientes para decidir.

Não considerar uma resposta melhor apenas porque é mais longa, confiante ou usa linguagem mais técnica. Não tratar a falha de DNS como falha do artefato nem como evidência de mudança de critério.

## 6. Perguntas para a discussão

1. O esforço maior alterou as decisões ou apenas expandiu as justificativas?
2. As novas evidências podem ser verificadas diretamente no repositório?
3. Alguma variante corrigiu erro factual, omissão ou inferência sem suporte?
4. Alguma variante declarou execução que não foi realizada ou confundiu resultados dos autores com reprodução independente?
5. Mudanças em F/R coincidiram com resultados observados na execução?
6. As diferenças podem ser explicadas por mudança de modelo, acesso, contexto ou ambiente?
7. O resultado aponta robustez, sensibilidade ou falta de evidência para concluir?

## 7. Conclusão — preencher após a coleta

> Os resultados da Tarefa 8 indicam que as avaliações são **[robustas / parcialmente robustas / sensíveis às configurações / inconclusivas]** para os critérios **[preencher]**. A principal diferença observada foi **[preencher]**. Essa diferença foi sustentada por **[evidências verificadas / evidências insuficientes / diferença de ambiente]**. Portanto, **[responder à pergunta de pesquisa sem generalizar além das execuções realizadas]**.

**Estado atual:** ainda não é possível classificar a robustez nem afirmar que houve mudança em D/F/S/R. Há uma resposta T8 registrada, mas a comparação T7 com ChatGPT e a revisão independente das evidências ainda estão pendentes. Não manter esta conclusão entre colchetes no relatório final; ela deve ser preenchida com resultados efetivamente obtidos.
