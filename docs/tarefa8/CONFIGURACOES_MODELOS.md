# Registro de configurações dos modelos — Tarefa 8

Este documento é o registro auditável das configurações efetivamente usadas. Preencher os campos com informações exibidas pelo provedor ou API. Não adivinhar versões a partir de nomes comerciais.

## 1. Informações recuperadas até agora

- **Modelos documentados na Tarefa 7:** Claude, Grok e Gemini.
- **Forma de acesso na Tarefa 7:** sites/interfaces das ferramentas.
- **Transcrições integrais da Tarefa 7:** não inventariadas neste repositório; os documentos consultados contêm sínteses de Claude, Grok e Gemini.
- **Artefato avaliado:** IoT-ID — https://github.com/GT-IoTEdu/sbrc26_fingerprint.
- **Situação da Tarefa 8:** primeira resposta registrada; revisão independente das evidências e demais variantes pendentes.

**Nota metodológica:** conforme esclarecimento da responsável, ChatGPT não foi utilizado na Tarefa 7. Os documentos disponíveis descrevem três avaliações (Claude, Grok e Gemini); esses são os modelos registrados na linha de base atual. Se surgir documentação original adicional sobre outro modelo, o inventário poderá ser atualizado, mas não se deve presumir uma avaliação ChatGPT-T7.

## 2. Linha de base da Tarefa 7

| Provedor/modelo na T7 | Identificador exato | Data da avaliação original | Acesso | Esforço/configuração | Prompt/entrada recuperados? | Transcrição integral inventariada? |
|---|---|---|---|---|---|---|
| Claude | Pendente de conferir na resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais | Não neste repositório |
| Grok | Pendente de conferir na resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais | Não neste repositório |
| Gemini | Pendente de conferir na resposta original | Pendente | Site/interface | Pendente | Recuperar dos registros originais | Não neste repositório |

Os documentos atuais da Tarefa 7 resumem Claude, Grok e Gemini. Os nomes comerciais não são suficientes para identificar o modelo exato; usar somente os dados visíveis na interface ou na resposta original. Se a interface não mostrar uma versão, registrar “não informado”.

## 3. Matriz planejada e execução registrada na T8

| ID | Família/modelo | Configuração de referência | Variante | Única variável alterada | Status |
|---|---|---|---|---|---|
| T8-GPT6-01 | GPT-6 (nome exibido) | Prompt padronizado; versão exata não informada | Esforço padrão | Configuração registrada para primeira execução | Resposta obtida; tentativa de execução independente não concluída; revisão de evidências pendente |
| T8-C-01 | Claude | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-C-02 | Claude | Mesmo identificador de T8-C-01 | Esforço alto/máximo disponível | Esforço | A executar |
| T8-G-01 | Grok | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-G-02 | Grok | Mesmo identificador de T8-G-01 | Esforço alto/máximo disponível | Esforço | A executar |
| T8-GM-01 | Gemini | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-GM-02 | Gemini | Mesmo identificador de T8-GM-01 | Esforço alto/máximo disponível | Esforço | A executar |

**Importante:** a matriz mistura uma execução já registrada com variantes planejadas. Os demais itens são um plano, não um registro de execuções concluídas. ChatGPT aparece na T8 como modelo usado nas rodadas registradas, mas não faz parte da linha de base T7 conforme esclarecimento da responsável. Se um provedor não oferecer um controle de esforço ou não permitir confirmar o modelo, marcar como indisponível e documentar a alternativa utilizada. Não comparar “esforço máximo” entre provedores como se fossem parâmetros equivalentes.

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

## 5. Ficha preenchida — T8-GPT6-01

- **ID da execução:** T8-GPT6-01
- **Data:** 2026-10-19
- **Provedor/interface:** ChatGPT, interface web
- **Nome exibido do modelo:** GPT-6
- **ID exato do modelo:** não informado
- **Versão/release:** não informada
- **Esforço de raciocínio/configuração:** padrão
- **Prompt utilizado:** `docs/PROMPT_PADRONIZADO.md`
- **Artefato/URL fornecido:** https://github.com/GT-IoTEdu/sbrc26_fingerprint
- **Acesso ao repositório:** consulta a páginas/arquivos por integração relatada; clonagem por Git falhou por resolução DNS
- **Registro estruturado preservado em:** `docs/tarefa8/T8_GPT6_PADRAO.md`
- **Transcrição literal integral da resposta:** não arquivada separadamente
- **Execução independente do pipeline:** não concluída
- **Limitações registradas:** nmap, nping, dumpcap, tshark, p0f e Docker relatados como ausentes; erro de clonagem com código 128 relatado, sem log bruto anexado
- **Observações:** o arquivo é um registro estruturado, não uma transcrição literal palavra por palavra. Revisar os caminhos/afirmações técnicas citados antes de considerar as evidências confirmadas independentemente.

## 6. Regras para comparabilidade

1. A comparação principal altera apenas uma variável.
2. Se a versão do modelo mudou automaticamente e não pode ser fixada, registrar isso como fator de confusão.
3. Se o esforço não estiver visível, não afirmar que foi “máximo”.
4. Preservar prompt, URLs e condições de acesso.
5. Se houver execução por API, registrar os parâmetros reais enviados, removendo chaves e credenciais.
6. Não alterar retroativamente as respostas originais da Tarefa 7; correções ou esclarecimentos devem ser registrados separadamente.
7. Diferenciar sempre resposta produzida pelo modelo, evidência documental citada e execução independente realmente observada.
