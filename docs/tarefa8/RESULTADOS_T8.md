# Resultados da Tarefa 8

## 1. Estado da coleta

**Status: uma resposta T8 registrada; auditoria independente parcial concluída; demais variantes pendentes.** A execução T8-GPT6-01 foi obtida em 2026-10-19 usando o nome de modelo exibido GPT-6 e esforço de raciocínio padrão. A versão exata não foi informada. O registro estruturado está em [T8_GPT6_PADRAO.md](T8_GPT6_PADRAO.md). Ele não é uma transcrição literal palavra por palavra; a transcrição integral original não foi arquivada separadamente. A auditoria das afirmações e arquivos citados está em [AUDITORIA_EVIDENCIAS_T8_GPT6.md](AUDITORIA_EVIDENCIAS_T8_GPT6.md).

Esta execução contém análise documental e de código relatada pelo modelo e uma tentativa de execução independente que não foi concluída. Portanto, não representa uma execução bem-sucedida do pipeline IoT-ID, nem uma verificação independente de todas as afirmações da resposta.

A linha de base resumida da Tarefa 7 está documentada em [../RESULTADOS_LLM.md](../RESULTADOS_LLM.md). Os resultados oficiais do evento estão em https://doc-artefatos.github.io/sbrc2026/results.html.

## 2. Registro por execução

| ID | Provedor/modelo e versão | Esforço | Tipo de avaliação | D | F | S | R | Registro estruturado salvo? | Transcrição literal integral? | Evidências verificadas por revisão independente? |
|---|---|---|---|---|---|---|---|---|---|
| T8-GPT6-01 | GPT-6; versão exata não informada | Padrão | Analítica + tentativa de execução | Acesso público confirmado na auditoria | Não confirmada por execução completa | Estrutura documentada; sem teste longitudinal | Não confirmada; divergência histórica/código identificada | Sim | Não arquivada separadamente | Parcial: inspeção dos arquivos e recálculo de hash |
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
| A preencher | Pendente | Pendente | Pendente | Pendente | Pendente | Pendente |

O resultado da tentativa está registrado conforme a resposta do modelo, mas não há log bruto anexado. Não classificar como teste de funcionalidade concluído nem como falha do artefato. Se apenas alguns componentes forem executados no futuro, classificar como parcial e listar os componentes.

## 5. Resumo por critério

| Critério | Linha de base T7 | Variante T8-GPT6-01 | O selo mudou? | Evidência nova verificada diretamente | Execução confirma? | Interpretação |
|---|---|---|---|---|---|---|
| D | Consultar T7 | Disponibilidade pública/documental considerada favorável na resposta | Não determinado | Não; revisão independente pendente | Não se aplica à disponibilidade em si; clonagem falhou | Provisório |
| F | Consultar T7 | Pipeline não confirmado por execução | Não determinado | Não; arquivos citados precisam ser conferidos | Não | Inconclusivo para funcionalidade executada |
| S | Consultar T7 | Estrutura considerada favorável, com ressalvas | Não determinado | Não; revisão independente pendente | Não | Inferência estrutural, sem teste longitudinal |
| R | Consultar T7 | Reprodutibilidade independente não verificada | Não determinado | Não; procedimento e referências precisam ser conferidos | Não | Inconclusivo quanto à reprodução independente |

Não converter campos pendentes em resultados negativos ou positivos. A avaliação qualitativa de uma resposta de LLM não equivale automaticamente a uma decisão oficial de atribuição de selo.

## 6. Resumo parcial

- **Variantes T8 com registro estruturado:** 1 (T8-GPT6-01).
- **Transcrição literal integral da resposta:** não arquivada separadamente.
- **Modelo exibido:** GPT-6.
- **Esforço:** padrão.
- **Versão exata:** não informada.
- **Avaliação analítica:** resposta obtida e preservada.
- **Execução independente do pipeline:** não concluída.
- **Motivo relatado:** falha de resolução DNS na clonagem e ausência de ferramentas de rede no ambiente.
- **Selos que permaneceram estáveis ou mudaram:** ainda não determinado.
- **Evidências novas verificadas diretamente:** arquivos principais existem; código/README foram inspecionados; uma string canônica histórica teve o SHA-256 recalculado e foi encontrada divergência entre o registro rotulado `stable` e o código atual.
- **Afirmações sem verificação independente:** ambiente e erro de clonagem da resposta original não têm log bruto anexado; o pipeline de rede completo não foi executado.
- **Limitações:** a resposta é um resultado do modelo, não comprova reprodução do pipeline. A auditoria detalhada está em `AUDITORIA_EVIDENCIAS_T8_GPT6.md`; a resposta original de ChatGPT da T7 não foi localizada.

A discussão final deve ser atualizada depois da recuperação da resposta original do ChatGPT da T7 e da coleta controlada de outras variantes.
