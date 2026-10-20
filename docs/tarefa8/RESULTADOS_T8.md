# Resultados da Tarefa 8

## 1. Estado da coleta

**Status: duas rodadas GPT-6 registradas em formato estruturado; auditoria independente parcial concluída; demais variantes planejadas pendentes.** T8-GPT6-01 foi registrada em 2026-10-19 com esforço padrão; T8-GPT6-02 foi registrada na mesma data com esforço alto solicitado pela usuária. Em ambas, o nome exibido foi GPT-6 e a versão exata não foi informada. Na segunda rodada, o nível de esforço é metadado solicitado/registrado, não verificado independentemente. Os registros estruturados não são transcrições literais integrais, e as respostas originais completas não foram arquivadas separadamente. Consulte [T8_GPT6_PADRAO.md](T8_GPT6_PADRAO.md), o relatório analítico da segunda rodada e [AUDITORIA_EVIDENCIAS_T8_GPT6.md](AUDITORIA_EVIDENCIAS_T8_GPT6.md).

As rodadas contêm análise documental/código e registros de tentativas de execução que não concluíram o pipeline completo. Portanto, nenhuma delas representa execução bem-sucedida do pipeline IoT-ID, nem verificação independente de todas as afirmações produzidas.

A linha de base resumida da Tarefa 7 está documentada em [../RESULTADOS_LLM.md](../RESULTADOS_LLM.md). Os resultados oficiais do evento estão em https://doc-artefatos.github.io/sbrc2026/results.html.

## 2. Registro por execução

| ID | Provedor/modelo e versão | Esforço | Tipo de avaliação | D | F | S | R | Registro estruturado salvo? | Transcrição literal integral? | Evidências verificadas por revisão independente? |
|---|---|---|---|---|---|---|---|---|---|
| T8-GPT6-01 | GPT-6; versão exata não informada | Padrão | Analítica + tentativa de execução | Acesso público confirmado na auditoria | Não confirmada por execução completa | Estrutura documentada; sem teste longitudinal | Não confirmada; divergência histórica/código identificada | Sim | Não arquivada separadamente | Parcial: inspeção dos arquivos e recálculo de hash |
| T8-GPT6-02 | GPT-6; versão exata não informada | Alto solicitado pela usuária; configuração não verificável independentemente | Analítica por consulta ao repositório público | Acesso público confirmado | Pipeline completo não executado | Estrutura documental favorável; sem teste longitudinal | Procedimento e hashes de referência encontrados; reprodução integral não demonstrada | Resumo analítico salvo; transcrição literal não recuperada | Não | Parcial: inspeção documental e nova verificação isolada stable/rich |
| T8-C-01 | A preencher | A preencher | Analítica | Pendente | Pendente | Pendente | Pendente | Não | Não |
| T8-C-02 | A preencher | A preencher | Analítica | Pendente | Pendente | Pendente | Pendente | Não | Não |
| T8-G-01 | A preencher | A preencher | Analítica | Pendente | Pendente | Pendente | Pendente | Não | Não |
| T8-G-02 | A preencher | A preencher | Analítica | Pendente | Pendente | Pendente | Pendente | Não | Não |
| T8-GM-01 | A preencher | A preencher | Analítica | Pendente | Pendente | Pendente | Pendente | Não | Não |
| T8-GM-02 | A preencher | A preencher | Analítica | Pendente | Pendente | Pendente | Pendente | Não | Não |

Os identificadores T8-C, T8-G e T8-GM são rótulos internos para organizar a coleta; não representam nomes oficiais de modelos. O registro GPT-6 não permite inferir versão exata a partir do nome exibido.

## 3. Verificação das evidências

Para cada execução, preencher:

| ID da execução | Critério | Decisão do modelo | Evidência/caminho citado | Evidência existe? | Sustenta a decisão? | Tipo D/C/A/E | Observação |
|---|---|---|---|---|---|---|---|
| T8-GPT6-01 | D | Favorável quanto à disponibilidade pública | Repositório e README do artefato | Pendente de revisão independente completa | Pendente | D | Resposta cita documentação pública; clonagem não foi concluída |
| T8-GPT6-01 | F | Pipeline não confirmado por execução completa | Módulos de fingerprinting e exemplos no README | Sim, arquivos existem; pipeline não foi executado | Parcialmente sustentada documentalmente | C/A | Inspeção de código não equivale à execução do fluxo de rede |
| T8-GPT6-01 | S | Estrutura favorável, com ressalvas | Módulos, documentação e requirements.txt | Pendente de revisão independente completa | Pendente | C/D | Inferência estrutural; não houve avaliação longitudinal |
| T8-GPT6-01 | R | Não confirmada por reprodução completa | Procedimento, registros TCL e código de canonicalização | Sim; recálculo parcial encontrou divergência stable/rich | Parcial, com ressalva importante | D/C/A/E parcial | Hash armazenado consistente entre seis arquivos, mas a string histórica inclui campos rich apesar do rótulo stable |

Uma evidência é considerada verificada somente depois de abrir o arquivo, trecho, comando ou resultado referido e confirmar que ele existe e é pertinente. A auditoria verificou a existência dos quatro módulos principais, README, requirements e arquivos de Docker, inspecionou registros de execução e encontrou uma divergência entre um hash histórico rotulado como stable e a política stable descrita no código atual. Ver detalhes e escopo em [AUDITORIA_EVIDENCIAS_T8_GPT6.md](AUDITORIA_EVIDENCIAS_T8_GPT6.md).

## 4. Execução independente

| ID | Ambiente e versões | Comando/procedimento | Resultado observado | Código de saída/log | Parte do fluxo executada | Limitação |
|---|---|---|---|---|---|---|
| T8-GPT6-01 | Linux x86_64; Python 3.13.5; requests 2.32.5, conforme resposta registrada | `git clone --depth 1 https://github.com/GT-IoTEdu/sbrc26_fingerprint.git /tmp/sbrc26_fingerprint` | Clonagem não concluída; erro de resolução DNS relatado | Código 128 relatado; log bruto não anexado | Nenhuma execução completa do pipeline confirmada | Falha de resolução DNS; nmap, nping, dumpcap, tshark, p0f e Docker relatados como ausentes |
| T8-GPT6-02 | Ambiente da sessão atual; clone por Git tentou em shell Linux | `git clone --depth 1 https://github.com/GT-IoTEdu/sbrc26_fingerprint.git /tmp/iotid` | Falha: `Could not resolve host: github.com` | Código 128; saída do terminal observada | Nenhuma etapa do pipeline | DNS/rede sem resolução; inspeção via integração não substitui clone |

O resultado da tentativa está registrado conforme a resposta do modelo, mas não há log bruto anexado. Não classificar como teste de funcionalidade concluído nem como falha do artefato. Se apenas alguns componentes forem executados no futuro, classificar como parcial e listar os componentes.

## 5. Resumo por critério

| Critério | Linha de base T7 | Variante T8-GPT6-01 | O selo mudou? | Evidência nova verificada diretamente | Execução confirma? | Interpretação |
|---|---|---|---|---|---|---|
| D | Consultar T7 | Disponibilidade pública/documental considerada favorável na resposta | Não determinado | Não; revisão independente pendente | Não se aplica à disponibilidade em si; clonagem falhou | Provisório |
| F | Consultar T7 | Pipeline não confirmado por execução | Não determinado | Não; arquivos citados precisam ser conferidos | Não | Inconclusivo para funcionalidade executada |
| S | Consultar T7 | Estrutura considerada favorável, com ressalvas | Não determinado | Não; revisão independente pendente | Não | Inferência estrutural, sem teste longitudinal |
| R | Consultar T7 | Reprodutibilidade independente não verificada | Não determinado | Não; procedimento e referências precisam ser conferidos | Não | Inconclusivo quanto à reprodução independente |

Não converter campos pendentes em resultados negativos ou positivos. A avaliação qualitativa de uma resposta de LLM não equivale automaticamente a uma decisão oficial de atribuição de selo.

## 6. Resultado novo: verificação isolada da divergência stable/rich

Foi executado um teste local de serialização e SHA-256 sobre uma fixture baseada nos dados públicos da TCL Smart TV Pro. O script está em [`verificar_hash_canonico_tcl.py`](verificar_hash_canonico_tcl.py).

| Política | Tamanho da string | Hash calculado | Correspondência |
|---|---:|---|---|
| stable | 203 caracteres | `3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961` | Corresponde ao exemplo stable do estudo |
| rich | 277 caracteres | `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51` | Corresponde ao hash histórico rotulado stable |

O teste confirma a divergência entre o rótulo histórico e os campos da string. Não executa o pipeline original nem captura tráfego. O motivo histórico (por exemplo, versão antiga ou registro incorreto) permanece indeterminado.

## 7. Resumo parcial

- **Rodadas T8 registradas em forma estruturada:** 2 (T8-GPT6-01, esforço padrão; T8-GPT6-02, esforço alto solicitado). A segunda não tem transcrição literal preservada e o esforço não pode ser verificado independentemente.
- **Transcrição literal integral das respostas anteriores:** não recuperada/arquivada separadamente; os arquivos existentes são registros estruturados ou relatórios, não cópias literais.
- **Modelo exibido:** GPT-6.
- **Esforço registrado:** padrão na T8-GPT6-01; alto solicitado na T8-GPT6-02, sem verificação independente do nível efetivo.
- **Versão exata:** não informada.
- **Avaliação analítica:** duas respostas registradas em forma estruturada; transcrições integrais não preservadas separadamente.
- **Execução independente do pipeline:** não concluída.
- **Motivo relatado:** falha de resolução DNS na clonagem e ausência de ferramentas de rede no ambiente.
- **Selos que permaneceram estáveis ou mudaram:** ainda não determinado.
- **Evidências novas verificadas diretamente:** arquivos principais existem; README e canonicalização foram inspecionados; clone por Git falhou com código 128 por DNS; teste local da fixture confirmou hash stable `3ce29174...` e hash rich `e20c4825...`, este último correspondente ao registro histórico rotulado `stable`.
- **Afirmações sem verificação independente:** ambiente e erro de clonagem da resposta original não têm log bruto anexado; o pipeline de rede completo não foi executado.
- **Limitações:** a resposta é um resultado do modelo, não comprova reprodução do pipeline. A auditoria detalhada está em `AUDITORIA_EVIDENCIAS_T8_GPT6.md`; ChatGPT não foi utilizado na T7, conforme esclarecimento da responsável; portanto, não existe resposta ChatGPT-T7 a recuperar.

A comparação de robustez permanece exploratória e inconclusiva: a T7 documenta Claude, Grok e Gemini, enquanto a T8 registra GPT-6, sem uma linha de base ChatGPT-T7. Também não há transcrição literal integral das rodadas T8. A evidência stable/rich é uma descoberta técnica independente, mas não substitui a execução completa do pipeline.
