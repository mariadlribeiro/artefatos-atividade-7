# Comparação Tarefa 7 × Tarefa 8

## 1. Objetivo

Verificar se as avaliações registradas na Tarefa 7 são estáveis sob mudanças controladas de versão e/ou esforço de raciocínio. A comparação usa o mesmo artefato, os mesmos critérios e, sempre que possível, o mesmo prompt.

## 2. Linha de base da Tarefa 7

| Critério | Claude — T7 | Grok — T7 | Gemini — T7 | Selo oficial |
|---|---|---|---|---|
| D | Atende, com ressalvas | Atende | Parcialmente verificável | Atribuído |
| F | Execução parcial | Atende, com limitações | Não verificável | Atribuído |
| S | Atende, com ressalvas | Atende | Não verificável | Atribuído |
| R | Reprodução parcial, com divergências | Atende, com limitações | Não verificável | Atribuído |

Os documentos disponíveis registram avaliações de Claude, Grok e Gemini na Tarefa 7. Conforme esclarecimento da responsável, ChatGPT não foi utilizado na Tarefa 7; portanto, não existe uma avaliação ChatGPT-T7 a recuperar e ela não deve aparecer como linha de base. O registro da Tarefa 7 informa que o IoT-ID recebeu os quatro selos oficiais. A tabela é uma síntese qualitativa, não uma equivalência automática entre “atende” e concessão formal de selo.

## 3. T8 — rodadas registradas de GPT-6

A T8 contém duas rodadas registradas em formato estruturado: T8-GPT6-01, com esforço padrão, e T8-GPT6-02, com esforço alto solicitado pela usuária. A interface exibiu “GPT-6” em ambos os casos; a versão exata não foi informada e o esforço da segunda rodada não pode ser verificado independentemente. Os arquivos existentes são resumos analíticos, não transcrições literais integrais. As tentativas de execução não concluíram o pipeline IoT-ID; portanto, não demonstram reprodução integral do artefato.

| Critério | Síntese T7 (Claude/Grok/Gemini) | T8-GPT6-01: esforço padrão | T8-GPT6-02: esforço alto solicitado | Mudança T7→T8? | Estado da evidência |
|---|---|---|---|---|
| D | Atende com ressalvas / atende / parcialmente verificável | Disponibilidade pública/documental considerada favorável | Disponibilidade pública/documental considerada favorável | Não determinável entre famílias | Revisão independente parcial |
| F | Execução parcial / atende com limitações / não verificável | Funcionalidade não confirmada por execução | Pipeline não confirmado por execução | Não determinável entre famílias | Pipeline completo não executado; testes parciais não substituem execução ponta a ponta |
| S | Atende com ressalvas / atende / não verificável | Estrutura considerada favorável, com ressalvas | Estrutura considerada favorável, com ressalvas | Não determinável entre famílias | Inferência estrutural; sem avaliação longitudinal |
| R | Reprodução parcial com divergências / atende com limitações / não verificável | Reprodutibilidade independente não verificada | Reprodutibilidade independente não verificada; divergência stable/rich investigada | Não determinável entre famílias | Pipeline completo e resultados de referência não foram reproduzidos integralmente |

**Não concluir que os critérios mudaram.** A comparação é exploratória entre famílias de modelos diferentes: Claude, Grok e Gemini na T7 e GPT-6 nas rodadas registradas da T8. Não é uma comparação longitudinal do ChatGPT entre T7 e T8. Além disso, a versão exata do modelo T8 não está informada, o que limita a reprodução da configuração.

## 4. Evidências novas verificadas após a auditoria

### 4.1 Esclarecimento sobre a linha de base T7

Conforme esclarecimento da responsável, ChatGPT não foi utilizado na Tarefa 7. Portanto, não existe transcrição ChatGPT-T7 a recuperar. Os documentos disponíveis sintetizam avaliações de Claude, Grok e Gemini; a comparação com T8 deve ser tratada como exploratória entre modelos/configurações, e não como mudança do mesmo modelo ao longo do tempo.

### 4.2 Tentativa de execução do pipeline

Foi realizada uma nova tentativa real de clonagem com:

```bash
git clone --depth 1 https://github.com/GT-IoTEdu/sbrc26_fingerprint.git /tmp/iotid
```

Resultado observado: `Could not resolve host: github.com`, código de saída 128. O repositório não foi clonado e o pipeline de rede não foi executado. Essa limitação ambiental não demonstra falha do artefato.

### 4.3 Teste isolado de hash stable/rich

Uma fixture baseada no registro público TCL Smart TV Pro foi serializada com as regras atuais de campos `stable` e `rich`, e o SHA-256 foi calculado localmente:

| Política | Comprimento | SHA-256 calculado | Resultado |
|---|---:|---|---|
| stable | 203 caracteres | `3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961` | Corresponde ao exemplo stable do estudo |
| rich | 277 caracteres | `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51` | Corresponde ao hash histórico rotulado stable |

O teste confirma que o hash histórico deriva da representação com `name` e `server` (rich), embora o log a rotule `stable`. Ele não executa o módulo original nem o pipeline de captura; é uma verificação isolada da serialização/hash da fixture. A causa histórica ainda não foi estabelecida.

Consulte [registro de execução e rastreabilidade](EXECUCAO_E_RASTREABILIDADE_T8.md) e [script de verificação](verificar_hash_canonico_tcl.py).

## 5. Tabela comparativa T7 × T8

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
| GPT-6 (T8) | D | Não se aplica: ChatGPT não foi usado na T7 | Favorável quanto à disponibilidade pública, provisório | Não determinável | Consultar sínteses T7 por modelo | Revisão independente pendente | Clonagem falhou; não é teste do critério D em si | Pendente |
| GPT-6 (T8) | F | Não se aplica: ChatGPT não foi usado na T7 | Não confirmada por execução | Não determinável | Consultar sínteses T7 por modelo | Arquivos citados precisam ser conferidos | Pipeline não executado | Pendente |
| GPT-6 (T8) | S | Não se aplica: ChatGPT não foi usado na T7 | Estrutura favorável, com ressalvas | Não determinável | Consultar sínteses T7 por modelo | Revisão independente pendente | Sem teste longitudinal | Pendente |
| GPT-6 (T8) | R | Não se aplica: ChatGPT não foi usado na T7 | Não verificada independentemente | Não determinável | Consultar sínteses T7 por modelo | Revisão independente pendente | Resultados de referência não repetidos | Pendente |

## 6. Como interpretar as diferenças

Classificar cada comparação como:

- **Estável:** decisão e sustentação por evidências permanecem equivalentes.
- **Mudança sustentada:** a decisão muda e a variante apresenta evidência nova, verificável e pertinente.
- **Mudança não sustentada:** a decisão muda, mas a justificativa não apresenta evidência nova suficiente.
- **Diferença de acesso/ambiente:** a mudança decorre de acesso ou capacidade de execução diferente; não deve ser atribuída automaticamente à versão/esforço.
- **Inconclusiva:** não há dados suficientes para decidir.

Não considerar uma resposta melhor apenas porque é mais longa, confiante ou usa linguagem mais técnica. Não tratar a falha de DNS como falha do artefato nem como evidência de mudança de critério.

## 7. Perguntas para a discussão

1. O esforço maior alterou as decisões ou apenas expandiu as justificativas?
2. As novas evidências podem ser verificadas diretamente no repositório?
3. Alguma variante corrigiu erro factual, omissão ou inferência sem suporte?
4. Alguma variante declarou execução que não foi realizada ou confundiu resultados dos autores com reprodução independente?
5. Mudanças em F/R coincidiram com resultados observados na execução?
6. As diferenças podem ser explicadas por mudança de modelo, acesso, contexto ou ambiente?
7. O resultado aponta robustez, sensibilidade ou falta de evidência para concluir?

## 8. Conclusão parcial atualizada

> Os resultados da Tarefa 8 indicam que as avaliações são **[robustas / parcialmente robustas / sensíveis às configurações / inconclusivas]** para os critérios **[preencher]**. A principal diferença observada foi **[preencher]**. Essa diferença foi sustentada por **[evidências verificadas / evidências insuficientes / diferença de ambiente]**. Portanto, **[responder à pergunta de pesquisa sem generalizar além das execuções realizadas]**.

**Conclusão atualizada:** a comparação de robustez entre T7 e T8 é exploratória e ainda inconclusiva: a T7 documenta Claude, Grok e Gemini, enquanto a T8 registra GPT-6; portanto, não existe uma linha de base ChatGPT-T7 e não se deve descrever o estudo como comparação longitudinal do mesmo modelo. A resposta integral da rodada GPT-6 com esforço alto solicitado também não está preservada como transcrição literal. A auditoria, entretanto, acrescentou uma evidência técnica verificável: a representação TCL rotulada historicamente como stable corresponde ao hash da política rich do código atual, enquanto a política stable descrita gera outro hash. A tentativa de execução completa foi bloqueada por DNS; portanto, essa nova evidência diz respeito à serialização/hash, não à execução do pipeline inteiro. Não atribuir essa diferença exclusivamente ao esforço do modelo nem concluir que o artefato inteiro falha em reprodutibilidade.
