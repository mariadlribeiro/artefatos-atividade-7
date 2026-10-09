# Protocolo experimental — Tarefa 8

## 1. Objetivo

A Tarefa 8 estende a Tarefa 7 para verificar a robustez das avaliações de artefatos científicos quando são alteradas, de forma controlada, configurações dos modelos de linguagem. O foco é identificar mudanças nos selos, nas evidências citadas e na coerência entre avaliação analítica e execução.

## 2. Artefato e referência

- Artefato: **IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting**.
- Evento: SBRC 2026 — Salão de Ferramentas.
- Repositório: https://github.com/GT-IoTEdu/sbrc26_fingerprint
- Resultados oficiais: https://doc-artefatos.github.io/sbrc2026/results.html
- Linha de base: resultados documentados na Tarefa 7 deste repositório.

A avaliação oficial atribuiu D, F, S e R ao artefato. Isso será tratado como referência de comparação, não como prova de que toda execução posterior necessariamente reproduzirá os resultados.

## 3. Pergunta de pesquisa

As avaliações da Tarefa 7 são robustas quando se altera a versão do LLM e/ou o esforço de raciocínio?

### Questões secundárias

1. Algum selo muda entre a linha de base e a variante?
2. A variante apresenta evidências mais específicas, verificáveis e diretamente relacionadas ao critério?
3. A execução independente confirma ou contradiz a avaliação analítica?
4. A variante reduz afirmações sem evidência ou apenas produz justificativas mais longas?
5. A concordância com os selos oficiais aumenta, diminui ou permanece igual?

## 4. Critérios avaliados

- **D — Disponibilidade:** acesso ao artefato e documentação necessária.
- **F — Funcionalidade:** possibilidade de instalar/executar e observar o funcionamento.
- **S — Sustentabilidade:** organização, legibilidade, documentação e condições para manutenção.
- **R — Reprodutibilidade:** possibilidade de reconstruir os procedimentos e resultados a partir de código, dados e configurações.

Os critérios e instruções oficiais devem ser mantidos iguais aos da Tarefa 7. Não adicionar uma pontuação ou critério próprio para decidir se um selo é concedido.

## 5. Desenho do experimento

### Fase A — Recuperação da linha de base

1. Consultar `docs/PROMPT_PADRONIZADO.md`, `docs/RESULTADOS_LLM.md` e `docs/RELATORIO_COMPLETO.md`.
2. Recuperar, se disponíveis, o identificador exato do modelo, a data, a configuração de esforço e a resposta integral de cada avaliação original.
3. Registrar lacunas de informação. Não inferir a versão exata de um modelo apenas pelo nome do provedor.

### Fase B — Escolha das variantes

Executar pelo menos uma comparação controlada por modelo quando a interface permitir:

- **Experimento de esforço:** mesma família/versão de modelo, mesmo prompt e mesmas entradas, alterando apenas o esforço de raciocínio (por exemplo, padrão versus alto/máximo, conforme a opção real disponível).
- **Experimento de versão:** duas versões identificáveis da mesma família, mantendo o prompt, as entradas e o esforço tão equivalentes quanto possível.

Se não for possível controlar um dos fatores, registrar a limitação e não atribuir a diferença exclusivamente a ele. Não usar nomes de configuração presumidos: registrar exatamente o que a interface ou API informa.

### Fase C — Avaliação analítica

Para cada variante:

1. Fornecer o mesmo artefato e as instruções oficiais.
2. Solicitar avaliação dos quatro critérios D/F/S/R.
3. Exigir decisão explícita para cada critério, evidências com caminho/arquivo/trecho, limitações e grau de verificabilidade.
4. Salvar a resposta integral sem edição.
5. Verificar diretamente no repositório se as evidências citadas realmente existem e sustentam a conclusão.

### Fase D — Avaliação por execução

Quando o ambiente permitir, seguir as instruções dos autores e executar o artefato ou os componentes relevantes. Registrar sistema operacional, dependências, versões, comandos, código de saída, logs e limitações. Distinguir execução parcial de reprodução completa.

Se a execução não for possível, registrar a razão concreta (por exemplo, dependência ausente, ausência de dispositivo de rede compatível, privilégio insuficiente ou falha de acesso). Não preencher o resultado com uma inferência do LLM.

### Fase E — Comparação

Comparar cada variante com a linha de base T7 e com a avaliação oficial. Para cada mudança, registrar:

- selo antes e depois;
- evidência original e evidência nova;
- se a evidência foi conferida diretamente;
- resultado da execução;
- explicação plausível para a diferença;
- se a mudança melhora a sustentação da decisão, piora ou não altera a conclusão.

## 6. Variáveis

| Tipo | Variável | Regra |
|---|---|---|
| Independente | esforço de raciocínio ou versão | Alterar uma variável por comparação, quando possível |
| Dependentes | selos D/F/S/R | Registrar decisão de cada critério |
| Dependentes | qualidade das evidências | Verificar especificidade, existência e pertinência |
| Dependentes | concordância analítica–execução | Registrar confirmação, confirmação parcial, divergência ou não verificável |
| Controle | artefato e critérios | Permanecem iguais |
| Controle | prompt-base | Permanece igual, salvo variante explicitamente documentada |
| Controle | entradas e ambiente | Manter equivalentes ou documentar diferenças |

## 7. Tipos de evidência

Manter a classificação da Tarefa 7:

- **D:** documentação.
- **C:** código-fonte.
- **A:** evidência fornecida pelos autores.
- **E:** execução independente.

Um log ou hash armazenado pelos autores não deve ser rotulado como E. Uma tentativa de execução que falha por uma limitação do ambiente deve ter a limitação descrita separadamente da conclusão sobre o artefato.

## 8. Regras de comparação e análise

- Comparar variantes com a linha de base do mesmo modelo sempre que houver dados identificáveis.
- Comparar provedores apenas como análise complementar, pois versões e interfaces podem oferecer controles diferentes.
- Não somar selos para criar uma nota global.
- Não tratar texto mais longo como evidência de maior qualidade.
- Não declarar superioridade de uma variante com base em um único caso sem ressalvas.
- Registrar resultados inconclusivos ou não executáveis como tais.
- Não alterar retrospectivamente as respostas originais da Tarefa 7.

## 9. Limitações esperadas

Os provedores podem não revelar a versão exata ou o esforço usado; interfaces diferentes podem oferecer opções diferentes; modelos podem ter mudado entre a Tarefa 7 e a Tarefa 8; e a execução do IoT-ID depende de ambiente Linux, ferramentas de rede, permissões e dispositivos compatíveis. Essas condições devem aparecer no relatório final.

## 10. Critério para responder à pergunta de pesquisa

A robustez será discutida com base na estabilidade das decisões, na qualidade e verificabilidade das evidências e na concordância com a execução independente. A conclusão poderá ser de robustez parcial, sensibilidade a configurações ou evidência insuficiente. Não presumir antecipadamente qual resultado será obtido.
