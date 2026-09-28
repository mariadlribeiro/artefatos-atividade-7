# Metodologia

## 1. Seleção do artefato

Foi selecionado o artefato IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting, pertencente ao Salão de Ferramentas do SBRC 2026.

Repositório: https://github.com/GT-IoTEdu/sbrc26_fingerprint

A página oficial de resultados do SBRC 2026 lista o IoT-ID entre os artefatos do Salão de Ferramentas e apresenta os quatro selos atribuídos.

## 2. Critérios

### D — Disponibilidade

Verificação da existência do artefato em repositório estável e da documentação mínima necessária para compreender o projeto.

### F — Funcionalidade

Verificação da possibilidade de executar o artefato e observar suas funcionalidades, considerando dependências, versões, ambiente, instalação e exemplos de execução.

### S — Sustentabilidade

Verificação da organização, modularização, inteligibilidade, documentação, legibilidade e possibilidade de identificar as principais reivindicações no artefato.

### R — Reprodutibilidade

Verificação da existência de instruções e condições que permitam reproduzir as principais reivindicações e resultados apresentados.

As definições de referência estão documentadas nas instruções do processo de avaliação de artefatos: https://doc-artefatos.github.io/sbseg2024/revinstrucoes.html

## 3. Modelos

Foram utilizadas três avaliações principais: Claude, Grok e Gemini. Todos receberam instruções equivalentes.

## 4. Avaliação analítica

A avaliação analítica compreendeu leitura da documentação, inspeção da estrutura, análise do código, identificação de dependências, identificação dos procedimentos de execução e análise dos resultados disponibilizados pelos autores.

## 5. Avaliação por execução

Quando o ambiente permitiu, os modelos realizaram testes independentes. A execução independente não foi considerada equivalente à simples leitura de resultados armazenados no repositório.

## 6. Classificação das evidências

| Código | Tipo | Descrição |
|---|---|---|
| D | Documentação | README, documentação e instruções |
| C | Código | Código-fonte e implementação |
| A | Autores | Logs, hashes e resultados fornecidos |
| E | Execução | Resultado reproduzido independentemente |

## 7. Comparação

Foram realizadas três comparações: LLM × LLM; avaliação analítica × execução; e LLM × avaliação oficial.

Não foi criada pontuação, ranking ou critério adicional.

## 8. Exclusão metodológica

Uma resposta do DeepSeek foi excluída porque avaliou o artefato AnonShield, e não o IoT-ID. Comparar artefatos diferentes não permitiria atribuir as diferenças ao modelo de linguagem.

## 9. Limitações

As condições de acesso não foram idênticas. Claude e Grok conseguiram acessar e executar partes do artefato. Gemini não conseguiu acessar o repositório em seu ambiente.

O IoT-ID depende de ambiente Linux, ferramentas de rede, privilégios e dispositivos/rede compatíveis. A reprodução completa do experimento original não pôde ser realizada por todos os avaliadores.
