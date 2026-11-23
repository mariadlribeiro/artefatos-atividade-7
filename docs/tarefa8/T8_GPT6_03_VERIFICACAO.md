# T8-GPT6-03 — ficha e verificação das evidências

Resposta bruta: [respostas/T8-GPT6-03.md](respostas/T8-GPT6-03.md). Referência para a verificação: [VERIFICACAO_COMPLETA_ARTEFATO.md](VERIFICACAO_COMPLETA_ARTEFATO.md) (clone no commit `167f487`).

## 1. Configuração

| Campo | Valor |
|---|---|
| Provedor / interface | ChatGPT (web) |
| Modelo exibido | **a confirmar** |
| Esforço / modo | **a confirmar** |
| Prompt | `docs/PROMPT_PADRONIZADO.md`, sem alterações |
| Data | 23/11/2026 |
| Acessou o repositório? | Por consulta web (cita "GitHub+1"); clone por Git falhou (DNS, código 128) |
| Transcrição literal preservada? | **Sim** (primeira rodada GPT-6 com resposta integral arquivada) |

ChatGPT não fez parte da T7. Esta rodada não preenche a matriz Claude/Grok/Gemini, mas serve como **terceira repetição do mesmo provedor** e permite medir a estabilidade intra-modelo em relação a T8-GPT6-01 e T8-GPT6-02.

## 2. Decisões

| Selo | Avaliação analítica | Execução | Tipos de evidência |
|---|---|---|---|
| D | Atendido | Clone falhou (limitação de ambiente) | D, C |
| F | Implementação identificada; funcionamento completo não validado | Nenhum módulo do IoT-ID executado | D, C, A |
| S | Favorável, com ressalvas de versionamento | — | D, C |
| R | Parcialmente demonstrada | SHA-256 da CANON_STRING do README recalculado → `e20c4825…` (coincide) | D, C, A, E limitada |

## 3. Verificação das evidências citadas

| # | Evidência citada | Selo | Verificação no artefato | Situação |
|---|---|---|---|---|
| 1 | Estrutura de arquivos (4 módulos .py, `fingerprint_subnet.sh`, `requirements.txt`, Dockerfile, compose, `docs/`, `testes/`) | D | Todos existem | Confirmada |
| 2 | Licença BSD | D/S | Declarada numa seção do README; **não há arquivo LICENSE** | Confirmada, com imprecisão (não menciona a ausência do arquivo) |
| 3 | Pipeline em 7 etapas (Nmap, dumpcap, Nping, p0f, TShark, canonicalização, SHA-256) | F | Coerente com README e `iot_id_fingerprint.py` | Confirmada |
| 4 | Dois modos de identificação: IoT/UPnP e *mobile* | F | `infer_host_kind`, `extract_mobile_passive_tshark`, `nmap_mobile_scan` em `iot_id_fingerprint.py` | Confirmada |
| 5 | Nping executado com `check=False` | F | `iot_id_fingerprint.py`, linha 889: `run(nping_cmd, check=False)` | Confirmada (achado novo, não presente na T7) |
| 6 | `requirements.txt` só com `requests>=2.25.0,<3`; Dockerfile sem fixar versões das ferramentas | S | Confirmado nos dois arquivos | Confirmada |
| 7 | Repetição padrão de 5 execuções por IP | R | README, linha 348 | Confirmada |
| 8 | Autores distinguem reprodução estrita (mesmo dispositivo/firmware) de funcional/comparativa | R | README, *Reproducibility Notes*, linhas 467–470 | Confirmada |
| 9 | Não há capturas PCAP de referência | R | `testes/` não contém arquivos `.pcap` (o `--cleanup` os remove) | Confirmada |
| 10 | "Os resultados de referência são apresentados principalmente no README"; a documentação não disponibiliza os elementos para reconstrução | R | **Incorreta/incompleta:** `testes/` contém 22 execuções com o bundle bruto (`fingerprint.json`), a CANON_STRING e o hash, o que permite reconstruir offline a etapa canonicalização → hash | Incorreta |
| 11 | SHA-256 da CANON_STRING do exemplo do README = `e20c4825…` | R | Correto, mas verifica só a **consistência interna** do registro (tipo A), não a reconstrução. O exemplo do README roda sem `--canon_policy`, ou seja, com o padrão `stable`; a CANON_STRING mostrada inclui `name` e `server`, que no código atual só entram em `rich`. Com o código atual e `stable`, o resultado é `3ce29174…` | Confirmada a conta; **interpretação incompleta** |
| 12 | Ambiente (kernel 6.18.57, Python 3.13.5, ferramentas ausentes); clone com código 128 | E | Não verificável externamente; sem log bruto | Não verificável |

**Resumo:** 9 confirmadas, 1 incorreta (nº 10), 1 com interpretação incompleta (nº 11), 1 não verificável. Nenhuma evidência inexistente (alucinação).

## 4. Indicadores-chave

| Indicador | Resultado |
|---|---|
| Detectou a divergência TCL `stable` × `rich`? | **Não.** Recalculou o hash da string já pronta e concluiu que ela "produz o valor esperado", sem perceber que a string não corresponde à política padrão |
| Detectou que o Xiaomi não reproduz? | Não (não examinou `testes/`) |
| Separou evidência dos autores (A) de execução independente (E)? | Sim, de forma explícita e correta |
| Executou módulos do artefato? | Não |
| Selos F e R iguais aos oficiais? | Não concede claramente nenhum dos dois (F "não validado", R "parcial"); o oficial concedeu ambos |

## 5. Comparação com as rodadas anteriores do mesmo provedor

| Aspecto | T8-GPT6-01 (padrão) | T8-GPT6-02 (alto solicitado) | T8-GPT6-03 |
|---|---|---|---|
| D | Favorável | Favorável | Atendido |
| F | Não confirmada por execução | Pipeline não executado | Não validado independentemente |
| R | Não confirmada; divergência apontada **pela auditoria posterior**, não pelo modelo | Reprodução integral não demonstrada; segundo `RELATORIO_COMPLETO_T8.md`, a análise de esforço alto **detalha a divergência `stable`/`rich`** do TCL | Parcial; divergência **não** detectada |
| Clone | Falhou (DNS, 128) | Falhou (DNS, 128) | Falhou (DNS, 128) |

As três rodadas chegam ao mesmo veredito qualitativo para D, F e R: **estabilidade intra-provedor**. A diferença está na profundidade. Segundo o relatório, só a rodada de esforço alto (T8-GPT6-02) apontou a divergência `stable`/`rich`. A T8-GPT6-03 recalculou o mesmo hash, mas não confrontou a CANON_STRING com o código.

**Depende da configuração desta rodada:** se T8-GPT6-03 usou esforço padrão, o resultado é coerente com a hipótese de que mais esforço leva a uma verificação mais profunda. Se usou esforço alto, isso mostra que a detecção não é estável nem com o mesmo esforço. Por isso é essencial confirmar o modelo e o esforço desta rodada. O relatório de T8-GPT6-02 não é uma transcrição literal; convém conferir se a divergência foi apontada pelo modelo ou pela revisão.
