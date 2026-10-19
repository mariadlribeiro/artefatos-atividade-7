# Tarefa 8 — Robustez da avaliação de artefatos com LLMs

Esta pasta complementa a Tarefa 7 sem alterar os resultados originais. O objetivo é investigar se as avaliações do artefato **IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting** permanecem estáveis quando se alteram, de forma controlada, a versão do modelo ou o esforço de raciocínio.

- **Artefato:** https://github.com/GT-IoTEdu/sbrc26_fingerprint
- **Evento:** SBRC 2026 — Salão de Ferramentas
- **Resultados oficiais:** https://doc-artefatos.github.io/sbrc2026/results.html
- **Tarefa 7 neste repositório:** documentos em `docs/`
- **Critérios:** D — Disponibilidade; F — Funcionalidade; S — Sustentabilidade; R — Reprodutibilidade.

## Documentos desta etapa

- [Protocolo experimental](PROTOCOLO_EXPERIMENTAL.md): desenho do estudo, variáveis controladas e procedimento.
- [Configurações dos modelos](CONFIGURACOES_MODELOS.md): registro das versões, provedores e esforço.
- [Prompts](PROMPTS.md): prompt-base e instruções para as variantes.
- [Resultados da Tarefa 8](RESULTADOS_T8.md): registro das respostas e da verificação das evidências.
- [Avaliação GPT-6 — esforço padrão](T8_GPT6_PADRAO.md): resposta registrada, ambiente relatado, conclusões provisórias e limitações.
- [Comparação T7 × T8](COMPARACAO_T7_T8.md): comparação de estabilidade e concordância.
- [Fluxograma](FLUXOGRAMA_T8.md): fluxo da atividade.

## Situação dos resultados

**Uma resposta da T8 foi registrada:** T8-GPT6-01, com nome de modelo exibido GPT-6, esforço padrão e data de 2026-10-19. A versão exata não foi informada. A resposta contém análise documental/de código e relata uma tentativa de clonagem que falhou por resolução DNS; o pipeline IoT-ID não foi executado integralmente.

As conclusões dessa resposta são provisórias. A revisão independente dos caminhos e das afirmações técnicas citadas ainda está pendente, assim como a recuperação da resposta original de ChatGPT na Tarefa 7 e a execução das demais variantes. Não interpretar campos pendentes como resultados negativos ou positivos e não alterar os resultados originais da Tarefa 7.

## Pergunta de pesquisa

As conclusões sobre os selos e as evidências do IoT-ID permanecem robustas quando mudamos a versão do modelo e/ou o esforço de raciocínio, mantendo o restante do protocolo tão constante quanto possível?

## Regras de integridade

1. Avaliar o mesmo artefato e usar os mesmos critérios oficiais.
2. Preservar o prompt-base da Tarefa 7 e registrar qualquer alteração.
3. Alterar uma variável por experimento sempre que possível.
4. Guardar respostas completas, data, provedor, identificador exato do modelo e configuração.
5. Separar evidência documental, código, evidência dos autores e execução independente.
6. Conferir cada afirmação importante diretamente no repositório.
7. Não confundir impossibilidade de acesso/execução no ambiente com falha comprovada do artefato.
8. Não concluir que maior esforço ou versão mais nova é melhor sem comparar as evidências.
