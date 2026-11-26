# Registro de configurações dos modelos — Tarefa 8

Este documento é o registro auditável das configurações efetivamente usadas. Preencher os campos com informações exibidas pelo provedor ou API. Não adivinhar versões a partir de nomes comerciais.

## 1. Informações recuperadas até agora

- **Modelos documentados na Tarefa 7:** Claude, Grok e Gemini.
- **Forma de acesso na Tarefa 7:** sites/interfaces das ferramentas.
- **Transcrições integrais da Tarefa 7:** não inventariadas neste repositório; os documentos consultados contêm sínteses de Claude, Grok e Gemini.
- **Artefato avaliado:** IoT-ID — https://github.com/GT-IoTEdu/sbrc26_fingerprint.
- **Situação da Tarefa 8 (23/11/2026, fechada):** Claude, 2 rodadas com esforço controlado (T8-C-01 padrão, T8-C-02 máximo) e transcrição literal; ChatGPT, 3 rodadas (T8-GPT6-01 e 02 em registro estruturado; T8-GPT6-03 com transcrição literal). Grok e Gemini não repetidos por decisão metodológica ([protocolo §11](PROTOCOLO_EXPERIMENTAL.md)).

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
| T8-GPT6-01 | GPT-6 (nome exibido) | Prompt padronizado; versão exata não informada | Esforço padrão | Configuração registrada para primeira execução | Rodada registrada em resumo estruturado; tentativa de execução independente não concluída; revisão de evidências parcial |
| T8-GPT6-02 | GPT-6 (nome exibido) | Prompt padronizado; versão exata não informada | Esforço alto solicitado pela usuária; não verificável independentemente | Esforço solicitado/registrado; versão exata não informada | Rodada analítica registrada em resumo estruturado; pipeline completo não executado; transcrição literal integral não preservada |
| T8-GPT6-03 | ChatGPT, plano gratuito; modelo padrão do plano (nome não registrado) | Prompt padronizado | Esforço padrão | Repetição intra-provedor | Rodada com transcrição literal integral; clone falhou (DNS); [ficha](T8_GPT6_03_VERIFICACAO.md) |
| T8-C-01 | Claude Opus 5.5 (`claude-opus-5-5`) | Prompt padronizado literal; agente novo com shell | Esforço padrão | Linha de base de esforço | **Concluída** em 23/11/2026; transcrição literal; [ficha](T8_CLAUDE_VERIFICACAO.md) |
| T8-C-02 | Claude Opus 5.5 (`claude-opus-5-5`) | Idêntica a T8-C-01 | Esforço **máximo** (`effort = max`) | **Somente o esforço** | **Concluída** em 23/11/2026; transcrição literal; [ficha](T8_CLAUDE_VERIFICACAO.md) |
| T8-G-01 | Grok | — | Esforço padrão | — | Não realizada (decisão metodológica, protocolo §11) |
| T8-G-02 | Grok | — | Esforço máximo | — | Não realizada (decisão metodológica, protocolo §11) |
| T8-GM-01 | Gemini | — | Esforço padrão | — | Não realizada (decisão metodológica, protocolo §11) |
| T8-GM-02 | Gemini | — | Esforço máximo | — | Não realizada (decisão metodológica, protocolo §11) |

**Importante:** as rodadas T8-C-01/02 e T8-GPT6-01/02/03 foram executadas; T8-G-01/02 e T8-GM-01/02 não foram realizadas, por decisão metodológica. ChatGPT aparece na T8 como modelo usado nas duas rodadas registradas, mas não faz parte da linha de base T7 conforme esclarecimento da responsável. Se um provedor não oferecer um controle de esforço ou não permitir confirmar o modelo, marcar como indisponível e documentar a alternativa utilizada. Não comparar “esforço máximo” entre provedores como se fossem parâmetros equivalentes.

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

## 7. Fichas preenchidas — T8-C-01 e T8-C-02

| Campo | T8-C-01 | T8-C-02 |
|---|---|---|
| Data | 2026-11-23 | 2026-11-23 |
| Provedor/interface | Anthropic; agente novo, sem histórico, em ambiente Linux em nuvem | idem |
| Nome/ID do modelo | Claude Opus 5.5 / `claude-opus-5-5` | idem |
| Esforço | padrão (parâmetro não definido) | máximo (`effort = max`) |
| Prompt | `docs/PROMPT_PADRONIZADO.md`, literal, mais instrução operacional (diretório próprio; não ler outros arquivos) | idem |
| Acesso ao repositório | clone OK (commit `167f487`) | idem |
| Resposta integral | [respostas/T8-C-01.md](respostas/T8-C-01.md) | [respostas/T8-C-02.md](respostas/T8-C-02.md) |
| Custo observado | ≈18 min; 41 chamadas de ferramenta; ≈201 mil tokens | ≈66 min; 142 chamadas; ≈457 mil tokens |
| Limitações | sem dispositivos físicos (testbed sintético); Docker Hub bloqueado | idem; daemon Docker instável |

## 8. Ficha preenchida — T8-GPT6-03

- **Data:** 2026-11-23
- **Provedor/interface:** ChatGPT, web, **plano gratuito**
- **Modelo:** padrão do plano gratuito (nome exato não registrado)
- **Esforço:** padrão (nenhum nível selecionado)
- **Prompt:** `docs/PROMPT_PADRONIZADO.md`
- **Acesso:** consulta web; clone falhou (DNS, código 128)
- **Resposta integral:** [respostas/T8-GPT6-03.md](respostas/T8-GPT6-03.md)
