# Resultados e Discussão

## 1. Resultados gerais

A avaliação foi realizada por Claude, Grok e Gemini sobre o artefato IoT-ID. O artefato recebeu oficialmente os quatro selos do SBRC 2026: Disponibilidade, Funcionalidade, Sustentabilidade e Reprodutibilidade.

| Critério | Claude | Grok | Gemini | Oficial |
|---|---|---|---|---|
| D | Atende, com ressalvas | Atende | Parcialmente verificável | Selo D |
| F | Execução parcial | Atende, com limitações | Não verificável | Selo F |
| S | Atende, com ressalvas | Atende | Não verificável | Selo S |
| R | Reprodução parcial, com divergências | Atende, com limitações | Não verificável | Selo R |

Os modelos não apresentaram conclusões totalmente convergentes. A maior aproximação ocorreu em Disponibilidade. As maiores diferenças ocorreram em Funcionalidade e, principalmente, Reprodutibilidade.

## 2. Disponibilidade

Claude e Grok verificaram o repositório público, README, código e estrutura. Claude registrou ressalvas relacionadas à licença, arquivos compilados versionados e diferença entre a descrição de testes e seu conteúdo. Grok considerou a estrutura suficiente para atendimento do critério. Gemini não conseguiu acessar o repositório e classificou o critério como parcialmente verificável.

A divergência do Gemini é uma limitação de seu ambiente, não evidência de indisponibilidade do artefato.

## 3. Funcionalidade

O IoT-ID possui pipeline com descoberta ativa por Nmap e UPnP, captura de pacotes, sondagem TCP SYN, identificação passiva por P0f, extração por TShark, canonicalização e geração de hash SHA-256.

Claude executou componentes do pipeline em Linux, mas não reproduziu integralmente o cenário com dispositivos IoT reais. Grok também executou componentes e encontrou limitações para o fluxo completo. Gemini não executou o artefato.

Assim, a execução independente confirmou partes do funcionamento, mas não reproduziu todas as condições do experimento original.

## 4. Sustentabilidade

Claude e Grok reconheceram a existência de modularização e documentação. Claude identificou como pontos de atenção a concentração da lógica em um arquivo principal, duplicação de funcionalidades e ausência de testes automatizados convencionais. Grok enfatizou organização, documentação e separação das funções.

As conclusões são compatíveis: o projeto pode ser compreendido e mantido, mas existem pontos que podem ser melhorados.

## 5. Reprodutibilidade

Reprodutibilidade foi o principal ponto de divergência. Grok considerou a documentação e os resultados disponibilizados suficientes para sustentar o critério sob condições equivalentes. Claude realizou uma verificação adicional, recalculando fingerprints e comparando os resultados com os valores armazenados.

No caso da TCL Smart TV Pro, seis execuções apresentavam o mesmo hash e20c4825..., demonstrando consistência interna. Entretanto, a reconstrução utilizando a política stable produziu outro valor. O hash armazenado foi reproduzido quando utilizada a política rich.

Também foram identificadas divergências em registros associados a outros dispositivos. O resultado não permite concluir isoladamente que todo o sistema seja não reprodutível. Ele demonstra que determinados resultados históricos não são diretamente reconstruídos pela configuração atualmente indicada.

## 6. Análise versus execução

| LLM | Critério | Análise | Execução | Relação |
|---|---|---|---|---|
| Claude | D | Disponível | Clone funcionou | Confirma |
| Claude | F | Funcional | Parcial | Confirma parcialmente |
| Claude | S | Sustentável | Inspeção compatível | Compatível |
| Claude | R | Reproduzível com ressalvas | Divergências | Divergência parcial |
| Grok | D | Atende | Acesso funcionou | Confirma |
| Grok | F | Atende | Parcial | Confirma parcialmente |
| Grok | S | Atende | Inspeção compatível | Compatível |
| Grok | R | Atende | Reprodução completa não realizada | Não totalmente confirmada |
| Gemini | D | Parcial | Acesso falhou | Compatível com limitação |
| Gemini | F | Não verificável | Não executado | Não verificável |
| Gemini | S | Não verificável | Não executado | Não verificável |
| Gemini | R | Não verificável | Não executado | Não verificável |

## 7. Convergências e divergências

Houve convergência na identificação de uma implementação concreta e documentação quando o acesso foi possível. Também houve reconhecimento de dependências de ambiente e de dispositivos IoT.

A maior divergência ocorreu em Reprodutibilidade. Grok atribuiu maior peso à documentação e aos resultados armazenados, enquanto Claude realizou reconstrução independente de hashes.

Gemini teve uma limitação de acesso diferente das demais avaliações, impedindo uma comparação técnica completa.

## 8. Comparação com os selos oficiais

A avaliação oficial do SBRC 2026 atribuiu os quatro selos ao IoT-ID. A análise posterior foi compatível com a disponibilidade, confirmou parcialmente a funcionalidade, encontrou evidências de sustentabilidade e identificou tanto evidências favoráveis quanto divergências na reprodutibilidade.

Isso não permite substituir ou invalidar a avaliação oficial. As avaliações ocorreram em momentos e condições diferentes. A análise com LLMs fornece uma verificação posterior e mais granular do estado público do artefato.

## 9. Discussão

O uso de um prompt padronizado reduziu diferenças decorrentes da formulação das instruções, mas não eliminou diferenças causadas pelo ambiente. O estudo demonstra que uma avaliação automatizada é mais informativa quando separa documentação, código, evidências dos autores e execução independente.

A principal contribuição da análise foi mostrar a diferença entre consistência interna e reprodução independente. Repetir o mesmo hash em registros fornecidos pelos autores demonstra consistência dos registros. Reproduzir o mesmo hash utilizando o código, dados e configuração disponíveis demonstra uma evidência adicional e independente.

## 10. Síntese

Os LLMs conseguiram identificar grande parte da estrutura documental e técnica do artefato, mas produziram diferentes níveis de confirmação quando a avaliação exigiu execução. A maior divergência ocorreu em Reprodutibilidade.

Os resultados indicam que LLMs podem apoiar avaliações de artefatos, desde que suas conclusões sejam acompanhadas pelas evidências, condições de execução e limitações. A avaliação automatizada deve ser tratada como complementar à verificação especializada.
