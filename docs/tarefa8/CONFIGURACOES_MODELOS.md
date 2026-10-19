# Registro de configurações dos modelos — Tarefa 8

Este documento é o registro auditável das configurações efetivamente usadas. Preencher os campos com informações exibidas pelo provedor ou API. Não adivinhar versões a partir de nomes comerciais.

## 1. Informações recuperadas até agora

- **Ferramentas usadas na Tarefa 7, conforme informação da responsável:** Claude, Grok, Gemini e ChatGPT.
- **Forma de acesso na Tarefa 7:** sites/interfaces das ferramentas.
- **Respostas integrais da Tarefa 7:** a responsável informa que todas estão guardadas.
- **Artefato avaliado:** IoT-ID — https://github.com/GT-IoTEdu/sbrc26_fingerprint.
- **Situação da Tarefa 8:** protocolo e tabelas preparados; nenhuma nova avaliação foi registrada como executada nesta etapa.

**Pendência de reconciliação documental:** os arquivos atuais `docs/PROMPT_PADRONIZADO.md`, `docs/RESULTADOS_LLM.md` e `docs/RELATORIO_COMPLETO.md` descrevem três avaliações (Claude, Grok e Gemini), enquanto a responsável informa que também houve uma avaliação com ChatGPT. A resposta original do ChatGPT deve ser localizada e comparada com os demais registros antes de decidir se ela faz parte da linha de base comparável. Não inferir seu resultado nem excluí-la sem verificar a resposta guardada.

## 2. Linha de base da Tarefa 7

| Provedor/modelo na T7 | Identificador exato | Data da avaliação original | Acesso | Esforço/configuração | Prompt/entrada recuperados? | Resposta integral guardada? |
|---|---|---|---|---|---|---|
| Claude | Pendente de conferir na interface/resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais | Sim, conforme informação da responsável |
| Grok | Pendente de conferir na interface/resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais | Sim, conforme informação da responsável |
| Gemini | Pendente de conferir na interface/resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais | Sim, conforme informação da responsável |
| ChatGPT | Pendente de conferir na interface/resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais e comparar com o prompt-base | Sim, conforme informação da responsável |

Os documentos atuais da Tarefa 7 resumem Claude, Grok e Gemini, mas não registram o ChatGPT na tabela de resultados. Os nomes comerciais não são suficientes para identificar o modelo exato; usar somente os dados visíveis na interface ou na resposta original. Se a interface não mostrar uma versão, registrar “não informado”.

## 3. Matriz planejada para T8

| ID | Família/modelo | Configuração de referência | Variante | Única variável alterada | Status |
|---|---|---|---|---|---|
| T8-C-01 | Claude | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-C-02 | Claude | Mesmo identificador de T8-C-01 | Esforço alto/máximo disponível | Esforço | A executar |
| T8-G-01 | Grok | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-G-02 | Grok | Mesmo identificador de T8-G-01 | Esforço alto/máximo disponível | Esforço | A executar |
| T8-GM-01 | Gemini | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-GM-02 | Gemini | Mesmo identificador de T8-GM-01 | Esforço alto/máximo disponível | Esforço | A executar |

**Importante:** a matriz acima é um plano, não um registro de execuções concluídas. O ChatGPT foi acrescentado ao registro da linha de base porque a responsável confirmou seu uso na T7; sua inclusão em novos experimentos deve ser definida após recuperar a resposta original e verificar a disponibilidade de controles de esforço/versão na interface. Se um provedor não oferecer um controle de esforço ou não permitir confirmar o modelo, marcar como indisponível e documentar a alternativa utilizada. Não comparar “esforço máximo” entre provedores como se fossem parâmetros equivalentes.

## 4. Ficha a preencher por execução

Copiar esta ficha para cada execução realizada:

- **ID da execução:**
- **Data e hora (fuso horário):**
- **Provedor/interface/API:**
- **Nome exibido do modelo:**
- **ID exato do modelo, se disponível:**
- **Versão/release, se disponível:**
- **Esforço de raciocínio/configuração exatamente como exibido:**
- **Temperatura e demais parâmetros, se acessíveis:**
- **Prompt utilizado e versão do arquivo:**
- **Artefato/URL fornecido:**
- **Acesso ao repositório funcionou?**
- **Resposta integral salva em:**
- **Houve erro, truncamento ou limitação?**
- **Observações:**

## 5. Regras para comparabilidade

1. A comparação principal altera apenas uma variável.
2. Se a versão do modelo mudou automaticamente e não pode ser fixada, registrar isso como fator de confusão.
3. Se o esforço não estiver visível, não afirmar que foi “máximo”.
4. Preservar prompt, URLs e condições de acesso.
5. Se houver execução por API, registrar os parâmetros reais enviados, removendo chaves e credenciais.
6. Não alterar retroativamente as respostas originais da Tarefa 7; correções ou esclarecimentos devem ser registrados separadamente.
