# Resultados detalhados dos LLMs

## 1. Síntese

| Critério | Claude | Grok | Gemini | Avaliação oficial |
|---|---|---|---|---|
| D | Atende, com ressalvas | Atende | Parcialmente verificável | Selo D |
| F | Execução parcial | Atende, com limitações | Não verificável | Selo F |
| S | Atende, com ressalvas | Atende | Não verificável | Selo S |
| R | Reprodução parcial, com divergências | Atende, com limitações | Não verificável | Selo R |

## 2. Claude

### D — Disponibilidade

Claude conseguiu clonar e inspecionar o repositório, verificando README, estrutura, código e documentação. Identificou ressalvas relacionadas à ausência de arquivo LICENSE separado, arquivos compilados versionados, diferença entre a descrição de testes no README e o conteúdo encontrado e ausência de uma suíte convencional de testes automatizados.

**Conclusão:** disponível, com ressalvas.

### F — Funcionalidade

Claude instalou dependências em ambiente Linux e executou partes do pipeline. A execução demonstrou que o código pode ser executado, mas não reproduziu integralmente o cenário com dispositivos IoT reais. Também foram observadas opções de linha de comando que não estavam todas descritas no README.

**Conclusão:** funcionalidade parcialmente verificada.

### S — Sustentabilidade

Foram identificadas separação entre canonicalização e geração de hash, funções organizadas por responsabilidade e documentação auxiliar. Também foram observados arquivo principal grande, duplicação de algumas funcionalidades, ausência de testes automatizados convencionais e mistura de português e inglês em comentários/documentação.

**Conclusão:** sustentável, com ressalvas.

### R — Reprodutibilidade

Claude recalculou hashes e comparou resultados armazenados com resultados reconstruídos. Foi identificada divergência importante no caso da TCL Smart TV Pro: o hash armazenado era reproduzido utilizando a política rich, enquanto a política stable, indicada nos registros, produzia outro valor. Também foram encontradas divergências em registros de outros dispositivos.

**Conclusão:** reprodução parcial, com divergências.

## 3. Grok

### D — Disponibilidade

Grok verificou a existência do repositório, README, código, Dockerfile, compose e arquivos relacionados.

**Conclusão:** atende.

### F — Funcionalidade

Grok executou componentes do projeto, incluindo a interface de ajuda e testes relacionados à canonicalização e fingerprint. Uma tentativa de executar o fluxo de rede completo encontrou limitações relacionadas ao ambiente e à ausência de dispositivo IoT adequado.

**Conclusão:** atende, com limitações ambientais.

### S — Sustentabilidade

Grok destacou modularização, documentação, separação das etapas, logging e organização das funções.

**Conclusão:** atende.

### R — Reprodutibilidade

Grok considerou a documentação e os resultados disponíveis suficientes para sustentar a reprodução em ambiente equivalente, reconhecendo que a reprodução completa depende de dispositivos e condições de rede compatíveis.

**Conclusão:** atende, com limitações.

## 4. Gemini

Gemini não conseguiu acessar o conteúdo do repositório devido a uma limitação de conectividade em seu ambiente. Foi registrada tentativa de acesso ao GitHub, mas a resolução de rede falhou.

Consequentemente:

- D: parcialmente verificável;
- F: não verificável;
- S: não verificável;
- R: não verificável.

Esses resultados representam uma limitação do ambiente e não constituem evidência de falha do artefato.

## 5. Evidências por modelo

| LLM | D | C | A | E |
|---|---|---|---|---|
| Claude | Sim | Sim | Sim | Sim |
| Grok | Sim | Sim | Sim | Parcial |
| Gemini | Parcial | Não | Não | Limitada à tentativa de acesso |

## 6. Relação entre análise e execução

| LLM | Critério | Análise | Execução | Relação |
|---|---|---|---|---|
| Claude | D | Disponível | Clone funcionou | Confirma |
| Claude | F | Funcional | Execução parcial | Confirma parcialmente |
| Claude | S | Sustentável | Inspeção compatível | Compatível |
| Claude | R | Reproduzível com ressalvas | Divergências | Divergência parcial |
| Grok | D | Atende | Acesso funcionou | Confirma |
| Grok | F | Atende | Execução parcial | Confirma parcialmente |
| Grok | S | Atende | Inspeção do código | Compatível |
| Grok | R | Atende | Reprodução completa não realizada | Não totalmente confirmada |
| Gemini | D | Parcial | Acesso falhou | Compatível com limitação |
| Gemini | F | Não verificável | Não executado | Não verificável |
| Gemini | S | Não verificável | Não executado | Não verificável |
| Gemini | R | Não verificável | Não executado | Não verificável |

## 7. Interpretação

A principal diferença entre Claude e Grok ocorreu na profundidade da verificação de Reprodutibilidade. Grok considerou principalmente documentação, procedimentos e resultados fornecidos pelos autores. Claude, além disso, reconstruiu resultados a partir dos dados disponíveis.

Gemini apresentou uma situação diferente, pois não conseguiu acessar o artefato. Portanto, seus resultados não devem ser usados como avaliação técnica negativa do projeto.

## 8. Comparação com a avaliação oficial

O SBRC 2026 atribuiu os quatro selos ao IoT-ID. A análise posterior encontrou compatibilidade clara para disponibilidade, confirmação parcial de funcionalidade, evidências de organização e documentação para sustentabilidade e evidências favoráveis e também divergências para reprodutibilidade.

Os resultados dos LLMs não substituem os selos oficiais. Eles constituem uma avaliação posterior do estado público do artefato e de sua verificabilidade sob diferentes ambientes.
