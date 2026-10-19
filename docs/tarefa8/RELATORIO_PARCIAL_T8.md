# Relatório parcial — Tarefa 8: robustez das avaliações de artefatos com LLMs

## 1. Objetivo

Investigar se a avaliação do artefato **IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting**, realizada com LLMs, permanece consistente quando são alteradas configurações do modelo, especialmente versão e esforço de raciocínio. A Tarefa 8 estende a Tarefa 7; por isso, mantém-se o mesmo artefato e os critérios oficiais do SBRC: D — Disponibilidade, F — Funcionalidade, S — Sustentabilidade e R — Reprodutibilidade.

- Repositório avaliado: https://github.com/GT-IoTEdu/sbrc26_fingerprint
- Resultados oficiais: https://doc-artefatos.github.io/sbrc2026/results.html
- Registros experimentais: [pasta docs/tarefa8](https://github.com/mariadlribeiro/artefatos-atividade-7/tree/tarefa-8/docs/tarefa8)

## 2. Protocolo

A comparação deve manter constantes o artefato, o prompt-base, as instruções oficiais e as entradas, alterando uma configuração por vez sempre que possível. Para cada resposta, registram-se o provedor, o nome e a versão exibidos do modelo, o esforço selecionado, a data, a resposta integral e as evidências citadas.

As evidências são classificadas como D (documentação), C (código), A (material fornecido pelos autores) ou E (execução independente). Registros e resultados armazenados pelos autores não são considerados execução independente. A impossibilidade de executar por limitação de ambiente não comprova falha do artefato.

## 3. Avaliação T8 registrada

A execução T8-GPT6-01 foi registrada em 19/10/2026. A interface identificou o modelo como GPT-6 e o esforço como padrão; a versão exata do modelo não foi informada. Foi preservado um registro estruturado da resposta, mas não uma transcrição literal integral separada.

A resposta relatou uma tentativa de clonagem do repositório que falhou por resolução DNS e não confirmou a execução completa do pipeline. Como não há log bruto anexado, o erro de ambiente permanece um relato da resposta, não uma falha independentemente reproduzida nesta auditoria.

### Síntese provisória por critério

| Critério | Evidência disponível | Conclusão provisória |
|---|---|---|
| D — Disponibilidade | Repositório e documentação pública; existência confirmada na auditoria | Disponibilidade documental favorável; acesso por clonagem não foi concluído no ambiente relatado |
| F — Funcionalidade | Módulos principais e instruções de execução identificados; pipeline completo não executado | Funcionalidade por execução independente não confirmada |
| S — Sustentabilidade | Estrutura modular, README, dependências e configuração Docker identificados | Organização documental favorável, mas manutenção a longo prazo não foi testada |
| R — Reprodutibilidade | Registros dos autores e recálculo parcial de hash; divergência entre registro histórico rotulado como stable e código atual | Reprodução integral não confirmada; há uma inconsistência que requer investigação adicional |

Estas conclusões não constituem uma nova atribuição oficial de selos. Elas descrevem o alcance das evidências examinadas nesta etapa.

## 4. Auditoria independente parcial

A auditoria confirmou a existência do README, dos módulos principais de fingerprinting, do arquivo de dependências e dos arquivos Docker. Também inspecionou registros históricos do dispositivo TCL Smart TV Pro.

O hash SHA-256 armazenado para uma string canônica coincide com o hash recalculado dessa mesma string. Entretanto, a string histórica associada à política denominada stable contém campos name e server, enquanto a implementação atual analisada inclui esses campos na política rich, não na stable. Portanto, existe uma divergência entre o registro histórico e a política descrita no código atual. A causa não foi determinada e não deve ser atribuída automaticamente a uma falha do artefato.

Essa verificação é parcial: recalcular o hash de uma string já fornecida não equivale a executar a captura de rede, extrair as características, canonicalizar os dados e reproduzir integralmente o pipeline.

Detalhes técnicos: [Auditoria de evidências T8 GPT-6](AUDITORIA_EVIDENCIAS_T8_GPT6.md).

## 5. Comparação com a Tarefa 7

Os registros existentes da Tarefa 7 sintetizam avaliações de Claude, Grok e Gemini. Eles indicam que o artefato recebeu os quatro selos oficiais, mas as avaliações dos modelos apresentaram diferentes limitações: execução parcial, limitações de ambiente e impossibilidade de acesso. A resposta original de ChatGPT utilizada na Tarefa 7 ainda precisa ser recuperada e conferida.

| Item | Tarefa 7 | Tarefa 8 até o momento |
|---|---|---|
| Artefato e critérios | IoT-ID; D/F/S/R | Mantidos |
| Prompt | Prompt padronizado da atividade | Mantido na primeira avaliação registrada |
| Configuração do modelo | Respostas de diferentes provedores documentadas; detalhes variam | GPT-6, esforço padrão; versão exata não informada |
| Execução independente completa | Varia conforme a avaliação original | Não concluída na execução T8 registrada |
| Verificação das evidências | Síntese existente nos documentos T7 | Auditoria direta parcial, incluindo a divergência stable/rich |
| Mudança nos selos | Linha de base a conferir nas respostas originais | Não determinável com os dados atuais |

Não é possível afirmar, neste momento, que os selos mudaram ou permaneceram estáveis para ChatGPT entre T7 e T8. A resposta original da T7 e ao menos uma variante T8 controlada adicional são necessárias para essa comparação.

## 6. Próximas etapas experimentais

1. Recuperar e arquivar a resposta integral de ChatGPT da Tarefa 7, sem reescrevê-la.
2. Executar uma segunda avaliação do mesmo artefato com o mesmo prompt e uma configuração de esforço diferente, se disponível. Registrar literalmente o nome da configuração exibida na interface.
3. Se houver versões identificáveis da mesma família, realizar uma comparação separada entre versões, mantendo o esforço tão equivalente quanto possível.
4. Conferir diretamente no repositório cada arquivo, trecho, comando e resultado usado para sustentar as decisões F e R.
5. Repetir, quando o ambiente permitir, os procedimentos dos autores e registrar comandos, versões, códigos de saída e logs.
6. Atualizar a tabela T7 × T8 e o fluxograma somente com resultados efetivamente coletados.

## 7. Conclusão parcial

Com as evidências atuais, **não é possível concluir se as avaliações são robustas ou sensíveis às configurações do modelo**. Há uma avaliação T8 registrada com esforço padrão e uma auditoria documental/de código parcial, mas não há uma segunda configuração controlada nem a resposta original de ChatGPT da Tarefa 7 conferida. A execução integral do pipeline também não foi confirmada.

O resultado mais importante até aqui é metodológico: a análise documental e o recálculo de um hash permitem verificar partes específicas da evidência, mas não substituem a reprodução completa do pipeline. A divergência histórica entre a política stable e o código atual deve ser investigada antes de qualquer conclusão mais forte sobre reprodutibilidade. A conclusão final deverá ser atualizada após a coleta das variantes e a recuperação da linha de base, sem preencher lacunas por inferência.
