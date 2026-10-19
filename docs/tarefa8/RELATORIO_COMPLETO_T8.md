# Tarefa 8 — Robustez de avaliações de artefatos por LLMs

**Artefato avaliado:** IoT-ID: *Deterministic Device Identity from Hybrid Network Fingerprinting*  
**Repositório-alvo:** https://github.com/GT-IoTEdu/sbrc26_fingerprint  
**Repositório desta atividade:** https://github.com/mariadlribeiro/artefatos-atividade-7/tree/tarefa-8  
**Data da segunda rodada registrada:** 19/10/2026  
**Modelo declarado para a rodada:** GPT-6, esforço alto solicitado pela avaliadora. *Observação:* a interface não fornece ao avaliador uma confirmação independente do nível de esforço; portanto, “alto” é metadado declarado, não uma propriedade tecnicamente verificada.

## 1. Resumo

Esta tarefa investiga a robustez de avaliações de um mesmo artefato científico feitas por modelos de linguagem. A avaliação segue os quatro critérios do processo de avaliação de artefatos do SBRC: **D — Disponibilidade, F — Funcionalidade, S — Sustentabilidade e R — Reprodutibilidade**. O protocolo distingue documentação dos autores, inspeção de código, evidência fornecida pelos autores e execução independente.

Nesta rodada GPT-6 de esforço alto solicitado, foi realizada uma **avaliação analítica baseada no repositório público e em páginas públicas**. Não foi executado o pipeline completo do IoT-ID nesta rodada. Por isso, as conclusões sobre funcionalidade e reprodutibilidade são limitadas: a presença de código, instruções e resultados armazenados não equivale à execução independente.

A revisão confirmou que o projeto está publicamente acessível, descreve um pipeline híbrido de fingerprinting e inclui código, dependências, configuração de contêiner e registros de experimentos. Também identificou uma questão que merece investigação: registros históricos de fingerprint de uma TV TCL apresentam divergência entre a política de canonicalização indicada nos registros e a política implementada no código atualmente inspecionado. Essa diferença, isoladamente, não prova falha do artefato; pode refletir mudança de versão ou inconsistência histórica.

## 2. Objetivo e perguntas de pesquisa

**Objetivo geral:** verificar em que medida as conclusões produzidas por LLMs sobre um mesmo artefato se mantêm consistentes quando muda a configuração do modelo, sem alterar o artefato ou os critérios de avaliação.

Perguntas orientadoras:

1. As conclusões sobre D, F, S e R permanecem consistentes entre as rodadas?
2. Os modelos distinguem evidência documental, código, resultados dos autores e execução independente?
3. As limitações do ambiente são corretamente separadas de falhas do artefato?
4. As conclusões são rastreáveis a evidências verificáveis?
5. As divergências entre avaliações são explicadas por evidências diferentes, pelo nível de detalhe ou por afirmações sem sustentação suficiente?

## 3. Artefato e critérios

O IoT-ID busca identificar dispositivos IoT por meio de uma impressão digital híbrida de rede. Conforme a documentação pública, o pipeline combina informações obtidas por ferramentas de descoberta e análise de rede, captura de tráfego, extração de atributos, canonicalização e geração de hash SHA-256.

| Critério | Questão examinada nesta tarefa |
|---|---|
| **D — Disponibilidade** | O repositório e os materiais necessários estão acessíveis? |
| **F — Funcionalidade** | O software executa as funções descritas, dentro das condições e dependências previstas? |
| **S — Sustentabilidade** | O artefato apresenta estrutura, documentação e informações suficientes para compreensão, uso e manutenção? |
| **R — Reprodutibilidade** | Outra pessoa consegue repetir os procedimentos e obter resultados comparáveis, com condições e evidências registradas? |

Não foram criados novos critérios, notas numéricas ou rankings. Os selos oficiais do SBRC são registrados como contexto externo, não como substitutos da avaliação independente desta atividade.

## 4. Protocolo experimental

### 4.1 Controle das condições

Para comparar as rodadas, deve-se manter:
- o mesmo artefato e o mesmo endereço do repositório;
- o mesmo prompt padronizado, salvo quando a variável experimental for explicitamente o prompt;
- os mesmos critérios D, F, S e R;
- a mesma estrutura de registro das respostas;
- a separação entre análise documental e execução real;
- a preservação integral da resposta de cada rodada, com data e configuração declarada.

A variável de interesse é a configuração do LLM (por exemplo, modelo ou esforço de raciocínio), alterada uma de cada vez. Se modelo e esforço forem alterados simultaneamente, não será possível atribuir uma diferença a apenas uma dessas variáveis.

### 4.2 Prompt padronizado

O prompt utilizado nesta rodada foi:

> Você deve avaliar o artefato IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting, disponível em https://github.com/GT-IoTEdu/sbrc26_fingerprint.
>
> A avaliação deve considerar os critérios do processo de avaliação de artefatos do SBRC: D — Disponibilidade; F — Funcionalidade; S — Sustentabilidade; R — Reprodutibilidade.
>
> Realize duas dimensões de avaliação:
> 1. Avaliação analítica: examine documentação, estrutura, código, dependências, instruções e resultados fornecidos pelos autores.
> 2. Avaliação por execução: quando o ambiente permitir, execute o artefato ou componentes relevantes e registre ambiente, comandos, resultados e códigos de saída.
>
> Para cada conclusão, identifique a origem da evidência:
> - D: documentação;
> - C: código;
> - A: evidência fornecida pelos autores;
> - E: execução independente.
>
> Não trate resultados armazenados pelos autores como execução independente.
>
> Registre ambiente, sistema operacional, versões, dependências, comandos, resultados, limitações e conclusão para D, F, S e R. Diferencie falha do artefato de limitação do ambiente de avaliação.
>
> Ao analisar Reprodutibilidade, diferencie existência de resultados fornecidos pelos autores, repetição desses resultados no próprio ambiente e reconstrução independente a partir do código, dados e configurações disponíveis.
>
> Não crie novos critérios, pontuações ou rankings. Não utilize avaliações de outros LLMs para formar sua conclusão.
>
> Finalize com uma tabela resumindo D, F, S e R e uma discussão das evidências.

### 4.3 Classes de evidência

- **D — Documentação:** README, instruções de instalação, explicações metodológicas e documentação do repositório.
- **C — Código:** arquivos-fonte, scripts, dependências e configuração de execução inspecionados.
- **A — Evidência dos autores:** logs, hashes, saídas e resultados armazenados no próprio artefato.
- **E — Execução independente:** comandos efetivamente executados durante a avaliação, com ambiente e resultados observáveis.

Uma evidência pode sustentar mais de uma observação, mas sua origem deve ser declarada. Um arquivo de log presente no repositório é evidência A, não E. Uma tentativa de execução bloqueada por rede ou por ausência de ferramenta deve ser registrada como limitação do ambiente, sem concluir automaticamente que o artefato falhou.

## 5. Resultados da rodada GPT-6 — esforço alto solicitado

### 5.1 Ambiente e execução

Esta rodada foi uma revisão analítica de materiais públicos. **Não foi executado o pipeline completo nesta rodada**; portanto, não há comandos de execução, códigos de saída ou resultados de runtime a relatar como evidência independente. O sistema operacional e as versões efetivamente usadas para uma execução do pipeline também não foram verificados nesta rodada.

A primeira rodada GPT-6 (registrada separadamente em `T8_GPT6_PADRAO.md`) relatou uma tentativa de clonagem que falhou por resolução DNS e ausência de ferramentas como nmap, nping, dumpcap, tshark, p0f e Docker. Como a resposta integral e os logs brutos daquela tentativa não foram preservados, essas informações devem ser tratadas como relato da rodada, não como execução independentemente auditada.

### 5.2 D — Disponibilidade

**Conclusão: disponibilidade pública confirmada.**

O repositório público foi acessível para inspeção. A árvore inclui README, documentação, código-fonte, arquivo de dependências, Dockerfile, configuração Docker Compose e diretório de registros de testes. A documentação explica requisitos e apresenta instruções para usar o pipeline.

**Evidências:** D (README e estrutura pública do repositório); C (presença dos arquivos de código e configuração).  
**Limite:** a disponibilidade pública não comprova que todas as dependências externas estejam acessíveis em qualquer ambiente, nem que o pipeline execute com sucesso.

### 5.3 F — Funcionalidade

**Conclusão: parcialmente verificável por inspeção; execução funcional completa não confirmada nesta rodada.**

A documentação descreve etapas que incluem descoberta de dispositivos e informações UPnP com Nmap, captura com dumpcap, sondagem TCP SYN com nping, extração passiva com p0f, análise de PCAP com tshark, canonicalização de atributos e geração de hash SHA-256. O código e a configuração do ambiente permitem compreender a arquitetura proposta.

Entretanto, a presença dos componentes e dos resultados armazenados não demonstra que o fluxo completo tenha sido executado com sucesso nesta rodada. A funcionalidade precisa ser verificada em uma rede compatível, com permissões adequadas e as ferramentas requeridas instaladas.

**Evidências:** D e C para a arquitetura documentada e os arquivos inspecionados; A para os registros armazenados.  
**Não há evidência E de execução completa nesta rodada.**

### 5.4 S — Sustentabilidade

**Conclusão: há sinais favoráveis de organização e documentação; manutenção de longo prazo não verificada.**

O repositório separa scripts por responsabilidade, documenta dependências e apresenta configuração para contêiner. Esses elementos facilitam a compreensão e podem ajudar a preparar o ambiente. O projeto depende, contudo, de ferramentas de sistema e de características de rede e permissões que precisam ser explicitadas na implantação.

A inspeção anterior da atividade encontrou muitos registros experimentais no diretório `testes/`, mas não encontrou uma suíte convencional facilmente identificável por padrões como `test_*.py`, `*_test.py`, `pytest.ini`, `tox.ini` ou `pyproject.toml`. Isso não significa que não existam testes manuais ou outras formas de validação; significa apenas que uma suíte automatizada convencional não foi identificada pelos padrões consultados.

Não foram realizados testes longitudinais de manutenção, instalação em múltiplos ambientes ou atualização de dependências. Assim, sustentabilidade não deve ser descrita como comprovada em longo prazo.

**Evidências:** D e C; a avaliação de manutenção permanece incompleta.

### 5.5 R — Reprodutibilidade

**Conclusão: há procedimentos e resultados de referência, mas a reprodução independente integral não foi demonstrada nesta rodada.**

A documentação descreve repetição de execuções por dispositivo e comparação de hashes, e inclui resultados de referência. Um hash armazenado pode ser recalculado a partir da representação canônica salva, mas isso confirma a consistência interna daquele registro, não que todo o pipeline tenha sido reconstruído a partir da captura de rede.

Uma auditoria parcial realizada anteriormente na atividade identificou o seguinte caso:
- arquivo de log: `testes/192.168.59.106_20260324_220537/fingerprint_pipeline.log`;
- representação canônica: `features_canon.txt`;
- hash registrado: `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51`;
- o hash SHA-256 da string canônica armazenada corresponde ao hash registrado;
- o log identifica a política como `stable`, mas a representação contém os campos `nmap.name` e `nmap.server`;
- no código inspecionado, esses campos são incluídos na política `rich`, enquanto a política `stable` usa outro conjunto de campos;
- o estudo de variáveis imutáveis da mesma TV TCL registra outro hash para a representação descrita como `stable`: `3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961`.

Isso evidencia uma divergência entre registros históricos e a lógica atual inspecionada. A causa não foi estabelecida. Possibilidades incluem diferença de versão do código, mudança de política ou inconsistência no registro. Não é adequado concluir falha definitiva do artefato sem rastrear a versão que gerou cada registro.

**Evidências:** A para logs, strings canônicas e hashes fornecidos no repositório; C para a lógica de canonicalização inspecionada. A rodada GPT-6 de esforço alto solicitado não produziu evidência E de reconstrução completa.

## 6. Síntese dos resultados GPT-6 — esforço alto solicitado

| Critério | Resultado desta rodada | Evidência disponível | Limitação principal |
|---|---|---|---|
| D — Disponibilidade | Confirmada quanto ao acesso público | D, C | Acesso público não garante execução |
| F — Funcionalidade | Parcialmente verificável por inspeção | D, C, A | Pipeline completo não executado nesta rodada |
| S — Sustentabilidade | Estrutura e documentação favoráveis, com ressalvas | D, C | Manutenção de longo prazo não testada |
| R — Reprodutibilidade | Procedimentos e resultados de referência existem; reprodução integral não demonstrada | D, C, A | Divergência de canonicalização; falta execução independente integral |

## 7. Comparação com Tarefa 7 e primeira rodada T8

### 7.1 Síntese do baseline T7

Os documentos resumidos da T7 registram:
- **Claude:** disponibilidade com ressalvas; funcionalidade parcialmente executada; sustentabilidade considerada atendida com ressalvas; reprodução parcial, com divergências no caso da TV TCL.
- **Grok:** avaliações favoráveis de disponibilidade e sustentabilidade, funcionalidade com limitações e reprodutibilidade com ressalvas; o fluxo de rede completo foi limitado pelo ambiente e pela ausência de dispositivo IoT adequado.
- **Gemini:** limitações de rede impediram acesso suficiente; disponibilidade parcialmente verificável e F/S/R não verificáveis. O bloqueio de acesso não foi tratado como falha do artefato.

Esses itens são **resumos existentes dos resultados da T7**, e não transcrições integrais das respostas originais. Conforme esclarecimento da responsável, ChatGPT não foi utilizado na T7; portanto, não existe resposta ChatGPT-T7 a localizar ou reconstruir.

### 7.2 Comparação qualitativa

| Dimensão | T7 — sínteses registradas | T8 — GPT-6 padrão (registro parcial) | T8 — GPT-6, esforço alto solicitado |
|---|---|---|---|
| Disponibilidade | Em geral acessível; Gemini teve limitação de rede | Repositório e documentação descritos como públicos | Acesso público confirmado por inspeção web |
| Funcionalidade | Parcial ou limitada pelo ambiente, variando entre modelos | Pipeline completo não executado; ferramentas ausentes na tentativa relatada | Inspeção analítica; execução completa não realizada |
| Sustentabilidade | Geralmente favorável, com ressalvas | Organização/documentação consideradas favoráveis | Estrutura documentada favorável; manutenção longitudinal não testada |
| Reprodutibilidade | Parcial, com diferenças em registro TCL; avaliações dependem do ambiente | Reprodução independente não confirmada | Reprodução integral não demonstrada; divergência de canonicalização destacada |

**Interpretação:** há convergência qualitativa entre as rodadas no ponto central: acesso e documentação podem ser verificados, mas a funcionalidade completa e a reprodução independente não devem ser afirmadas sem execução observável. A análise de esforço alto detalha a divergência entre a política `stable` indicada no registro TCL e os campos contidos na representação canônica.

Essa comparação é provisória. Os resumos da T7 não possuem a mesma granularidade de uma transcrição integral com evidências por afirmação. Além disso, a configuração de esforço do modelo não pode ser confirmada independentemente a partir do texto da conversa. Portanto, não é possível atribuir diferenças exclusivamente ao esforço de raciocínio.

## 8. Ameaças à validade

1. **Ausência de transcrições completas da T7:** limita a comparação linha a linha e a codificação consistente das conclusões.
2. **Resposta integral não arquivada da primeira rodada T8:** o arquivo existente é um resumo estruturado, não a transcrição literal.
3. **Ausência de execução completa na rodada atual:** conclusões de F e R são necessariamente limitadas.
4. **Configuração de esforço não verificável externamente:** “alto” é a configuração solicitada/registrada, mas não confirmada por telemetria.
5. **Dependência de rede e hardware:** descoberta e fingerprinting dependem de ferramentas, permissões, topologia e dispositivos reais.
6. **Possível deriva entre versões:** diferenças entre logs antigos e o código atual podem refletir versões distintas.
7. **Avaliação analítica baseada em materiais públicos:** a inspeção documental não substitui instalação, execução e repetição independente.

## 9. Próximos passos para fechar o experimento

- [ ] Manter a linha de base T7 limitada aos modelos documentados; se surgir registro original adicional, atualizar o inventário com base nele.
- [ ] Arquivar integralmente as respostas de cada rodada T8, sem reescrevê-las como se fossem transcrições.
- [ ] Registrar data, nome de modelo exibido, esforço selecionado, prompt exato e limitações.
- [ ] Fazer ao menos uma execução controlada em ambiente compatível, registrando SO, versões, dependências, comandos, código de saída e logs.
- [ ] Rastrear a versão do código que produziu os registros da TV TCL e explicar a divergência de política/hash.
- [ ] Comparar as respostas com uma matriz comum: conclusão por critério, tipo de evidência citado, afirmações não sustentadas, limitações reconhecidas e divergências.
- [ ] Não preencher resultados ausentes por inferência; marcar explicitamente “não executado”, “não localizado” ou “não verificável”.

## 10. Conclusão

A rodada GPT-6 de esforço alto solicitado sustenta a disponibilidade pública do IoT-ID e identifica documentação, código e registros relevantes para sua análise. A organização do projeto e a documentação são sinais positivos para compreensão e uso, embora a manutenção de longo prazo não tenha sido testada.

A funcionalidade integral e a reprodutibilidade independente permanecem inconclusivas nesta rodada, pois o pipeline completo não foi executado. A auditoria parcial de registros identificou uma divergência entre a política de canonicalização declarada e os campos presentes em um registro de fingerprint da TV TCL. Essa divergência é um ponto concreto para investigação, não prova isolada de falha.

Em comparação com os resumos da T7 e com a primeira rodada T8, a conclusão geral é consistente: LLMs podem ajudar a localizar documentação, descrever arquitetura e levantar inconsistências, mas suas avaliações precisam distinguir rigorosamente resultados dos autores de execução independente. A robustez entre modelos só poderá ser estimada com maior confiança quando as respostas integrais, configurações e evidências de execução estiverem arquivadas de forma comparável.

## 11. Referências

1. **Repositório do artefato IoT-ID.** https://github.com/GT-IoTEdu/sbrc26_fingerprint
2. **Resultados oficiais da avaliação de artefatos do SBRC 2026.** https://doc-artefatos.github.io/sbrc2026/results.html
3. **Repositório da atividade T7/T8.** https://github.com/mariadlribeiro/artefatos-atividade-7/tree/tarefa-8
4. **Documentos de protocolo e baseline da atividade:** `docs/PROMPT_PADRONIZADO.md`, `docs/RESULTADOS_LLM.md`, `docs/RELATORIO_COMPLETO.md` e os arquivos em `docs/tarefa8/`.

---

**Nota de integridade:** este relatório registra o que foi inspecionado e o que não foi executado. Não deve ser interpretado como certificação independente dos quatro critérios do SBRC, nem como substituto da avaliação oficial do artefato.
