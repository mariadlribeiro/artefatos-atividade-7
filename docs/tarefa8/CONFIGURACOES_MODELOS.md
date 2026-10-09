# Registro de configurações dos modelos — Tarefa 8

Este documento é o registro auditável das configurações efetivamente usadas. Preencher os campos com informações exibidas pelo provedor ou API. Não adivinhar versões a partir de nomes comerciais.

## 1. Linha de base da Tarefa 7

| Provedor/modelo na T7 | Identificador exato | Data da avaliação original | Esforço/configuração | Prompt/entrada recuperados? | Resposta integral guardada? |
|---|---|---|---|---|---|
| Claude | Pendente de confirmação | Pendente | Pendente | Verificar registros originais | Verificar registros originais |
| Grok | Pendente de confirmação | Pendente | Pendente | Verificar registros originais | Verificar registros originais |
| Gemini | Pendente de confirmação | Pendente | Pendente | Verificar registros originais | Verificar registros originais |

Os documentos da Tarefa 7 identificam os provedores, mas não estabelecem, por si só, todos os identificadores exatos de modelo, datas e parâmetros. Esses campos precisam ser recuperados dos registros originais ou marcados como não disponíveis.

## 2. Matriz planejada para T8

| ID | Família/modelo | Configuração de referência | Variante | Única variável alterada | Status |
|---|---|---|---|---|---|
| T8-C-01 | Claude | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-C-02 | Claude | Mesmo identificador de T8-C-01 | Esforço alto/máximo disponível | Esforço | A executar |
| T8-G-01 | Grok | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-G-02 | Grok | Mesmo identificador de T8-G-01 | Esforço alto/máximo disponível | Esforço | A executar |
| T8-GM-01 | Gemini | Mesmo identificador da T7, se disponível | Esforço padrão | Linha de base de esforço | A executar |
| T8-GM-02 | Gemini | Mesmo identificador de T8-GM-01 | Esforço alto/máximo disponível | Esforço | A executar |

**Importante:** a matriz acima é um plano, não um registro de execuções concluídas. Se um provedor não oferecer um controle de esforço ou não permitir confirmar o modelo, marcar como indisponível e documentar a alternativa utilizada. Não comparar “esforço máximo” entre provedores como se fossem parâmetros equivalentes.

## 3. Ficha a preencher por execução

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

## 4. Regras para comparabilidade

1. A comparação principal altera apenas uma variável.
2. Se a versão do modelo mudou automaticamente e não pode ser fixada, registrar isso como fator de confusão.
3. Se o esforço não estiver visível, não afirmar que foi “máximo”.
4. Preservar prompt, URLs e condições de acesso.
5. Se houver execução por API, registrar os parâmetros reais enviados, removendo chaves e credenciais.
