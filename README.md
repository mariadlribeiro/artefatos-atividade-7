# Avaliação de Artefato Científico com Modelos de Linguagem

## Atividade

Este repositório contém a documentação completa da atividade de avaliação de um artefato científico utilizando modelos de linguagem de diferentes provedores.

**Artefato:** IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting

**Evento:** SBRC 2026 — Salão de Ferramentas.

**Repositório avaliado:** https://github.com/GT-IoTEdu/sbrc26_fingerprint

**Resultados oficiais:** https://doc-artefatos.github.io/sbrc2026/results.html

## Objetivo

Investigar em que medida diferentes modelos de linguagem conseguem avaliar o mesmo artefato científico utilizando os critérios D, F, S e R, realizando avaliação analítica e, quando possível, execução independente.

## Modelos

- Claude
- Grok
- Gemini

Uma resposta do DeepSeek foi excluída da comparação principal porque avaliou outro artefato, AnonShield. A exclusão preserva a equivalência experimental.

## Selos

- D — Disponibilidade
- F — Funcionalidade
- S — Sustentabilidade
- R — Reprodutibilidade

O IoT-ID recebeu oficialmente os quatro selos no SBRC 2026.

## Estrutura

- docs/RELATORIO_COMPLETO.md — relatório completo.
- docs/METODOLOGIA.md — metodologia e critérios.
- docs/PROMPT_PADRONIZADO.md — prompt utilizado.
- docs/RESULTADOS_LLM.md — resultados dos três LLMs.
- docs/EVIDENCIAS_REPRODUTIBILIDADE.md — análise dos hashes e evidências.
- docs/FLUXOGRAMA.md — fluxograma do processo.
- docs/REFERENCIAS.md — fontes utilizadas.

## Resultado resumido

| Critério | Claude | Grok | Gemini | Oficial |
|---|---|---|---|---|
| D | Atende, com ressalvas | Atende | Parcialmente verificável | Selo D |
| F | Execução parcial | Atende, com limitações | Não verificável | Selo F |
| S | Atende, com ressalvas | Atende | Não verificável | Selo S |
| R | Reprodução parcial, com divergências | Atende, com limitações | Não verificável | Selo R |

A principal divergência ocorreu em Reprodutibilidade. Claude reconstruiu fingerprints a partir dos dados disponíveis e encontrou divergências entre alguns hashes armazenados e aqueles obtidos com a implementação e a configuração atualmente disponíveis. Grok considerou a documentação e os resultados fornecidos pelos autores suficientes para sustentar o critério, embora tenha reconhecido dependências de ambiente.

## Tipos de evidência

- D — documentação;
- C — código;
- A — evidência fornecida pelos autores;
- E — execução independente.

A classificação impede que um resultado armazenado pelos autores seja tratado automaticamente como reprodução independente.

## Conclusão resumida

A utilização de um prompt padronizado não produziu avaliações completamente idênticas. As diferenças aumentaram nos critérios que dependem de execução, especialmente F e R. O estudo mostra que a avaliação por LLM depende não apenas das instruções, mas também do acesso ao artefato, das condições de execução e da possibilidade de verificar independentemente os resultados.

**Autora:** Maria de Lurdes Ribeiro


## Tarefa 8 — análise de robustez

A extensão da atividade está organizada separadamente em [`docs/tarefa8/`](docs/tarefa8/README.md), sem substituir os registros da Tarefa 7. Inclui protocolo experimental, registro de versões e esforço, prompts, tabelas de coleta, comparação T7 × T8 e fluxograma. Os resultados de T8 estão marcados como pendentes até que as novas variantes sejam efetivamente executadas e suas evidências verificadas.
