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
- [Avaliação GPT-6 — esforço padrão](T8_GPT6_PADRAO.md): registro estruturado da resposta e conclusões provisórias.
- [Relatório analítico da segunda rodada GPT-6](RELATORIO_COMPLETO_T8.md): registro da avaliação com esforço alto solicitado, sem transcrição literal integral e sem verificação independente do esforço.
- [Auditoria de evidências T8](AUDITORIA_EVIDENCIAS_T8_GPT6.md): conferência dos caminhos, módulos, dependências, registros dos autores e recálculo parcial do hash.
- [Execução e rastreabilidade T8](EXECUCAO_E_RASTREABILIDADE_T8.md): tentativa real de clonagem, resultado de DNS, limites da recuperação das transcrições e resultados stable/rich.
- [Adendo histórico da canonicalização TCL](ADENDO_HISTORICO_CANONICALIZACAO_TCL.md): análise dos commits de 24 e 25/03/2026 e explicação provável para a divergência stable/rich.
- [Script de verificação isolada](verificar_hash_canonico_tcl.py): cálculo local de SHA-256 para fixture derivada dos registros públicos da TCL.
- [Verificação completa do artefato](VERIFICACAO_COMPLETA_ARTEFATO.md): clone real (commit `167f487`), `--help`, evidências de F/S e recálculo das 22 execuções de `testes/` com o código original ([script](recalcular_hashes_testes.py), [CSV](dados/recalculo_hashes_testes.csv)).
- [Comparação T7 × T8](COMPARACAO_T7_T8.md): comparação de estabilidade e concordância.
- [Fluxograma](FLUXOGRAMA_T8.md): fluxo da atividade.
- [Status de fechamento](STATUS_FECHAMENTO_T8.md): checklist do que foi verificado, limitações e condições restantes para concluir experimentalmente a T8.

## Situação dos resultados

**Duas rodadas da T8 estão registradas em formato estruturado:** T8-GPT6-01 (GPT-6 exibido, esforço padrão) e T8-GPT6-02 (GPT-6 exibido, esforço alto solicitado), ambas datadas de 2026-10-19. A versão exata não foi informada; na segunda rodada, o nível de esforço não pode ser verificado independentemente. Os registros não são transcrições literais integrais. A análise documental e a tentativa de execução não resultaram em execução integral do pipeline IoT-ID.

As conclusões das duas rodadas são provisórias. Uma auditoria documental e de código já foi registrada; ela encontrou uma divergência entre registros históricos rotulados como `stable` e o código atual. Uma tentativa de clone por Git feita em shell nesta etapa também falhou por resolução DNS (código 128). Um teste isolado da fixture TCL confirmou que o hash histórico corresponde à representação `rich`, enquanto a representação `stable` gera o hash descrito no estudo. O pipeline completo não foi executado. A T7 disponível documenta Claude, Grok e Gemini; conforme esclarecimento da responsável, ChatGPT não foi utilizado na T7. A execução das demais variantes continua pendente. Não interpretar campos pendentes como resultados negativos ou positivos e não alterar os resultados originais da Tarefa 7.

## Pergunta de pesquisa

As conclusões sobre os selos e as evidências do IoT-ID permanecem robustas quando mudamos a versão do modelo e/ou o esforço de raciocínio, mantendo o restante do protocolo tão constante quanto possível?

**Limitação atual do desenho:** a T7 documenta Claude, Grok e Gemini; a T8 registra GPT-6. Como não há uma linha de base do mesmo modelo entre as tarefas, a comparação T7–T8 atual é exploratória e não isola o efeito da versão ou do esforço de raciocínio. Para responder causalmente sobre esforço, é necessária uma comparação controlada dentro da mesma família/versão, com o mesmo prompt e apenas o esforço alterado.

## Regras de integridade

1. Avaliar o mesmo artefato e usar os mesmos critérios oficiais.
2. Preservar o prompt-base da Tarefa 7 e registrar qualquer alteração.
3. Alterar uma variável por experimento sempre que possível.
4. Guardar respostas completas, data, provedor, identificador exato do modelo e configuração.
5. Separar evidência documental, código, evidência dos autores e execução independente.
6. Conferir cada afirmação importante diretamente no repositório.
7. Não confundir impossibilidade de acesso/execução no ambiente com falha comprovada do artefato.
8. Não concluir que maior esforço ou versão mais nova é melhor sem comparar as evidências.
