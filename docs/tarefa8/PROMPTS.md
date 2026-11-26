# Prompts — Tarefa 8

## 1. Princípio

O prompt-base da Tarefa 7 deve ser preservado para manter comparabilidade. O conteúdo integral está em [../PROMPT_PADRONIZADO.md](../PROMPT_PADRONIZADO.md). Abaixo está uma versão operacional para repetir a avaliação; antes de executar, comparar seu texto com o prompt original e usar o original sempre que estiver disponível.

## 2. Prompt para avaliação analítica

> Avalie o artefato **IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting**, disponível em https://github.com/GT-IoTEdu/sbrc26_fingerprint, segundo os critérios oficiais D — Disponibilidade, F — Funcionalidade, S — Sustentabilidade e R — Reprodutibilidade do processo de avaliação de artefatos do SBRC.
>
> Faça uma avaliação analítica da documentação, estrutura, código, dependências, instruções de instalação e execução e resultados fornecidos pelos autores. Para cada critério, apresente a decisão, a justificativa e as evidências concretas, identificando arquivos, caminhos e trechos sempre que possível.
>
> Diferencie as evidências por origem: D (documentação), C (código), A (evidência fornecida pelos autores) e E (execução independente). Não classifique resultados dos autores como execução independente. Diferencie impossibilidade de acesso no ambiente de evidência de falha do artefato.
>
> Para R, explique se os resultados foram apenas documentados, repetidos a partir dos registros dos autores ou reconstruídos independentemente a partir de código, dados e configurações. Não crie critérios, pontuações ou rankings novos. Não use avaliações de outros modelos como evidência.
>
> Termine com uma tabela D/F/S/R, as limitações e uma lista das evidências que precisam ser verificadas diretamente no repositório.

## 3. Prompt para execução

> Siga as instruções de instalação e execução fornecidas pelos autores do IoT-ID: https://github.com/GT-IoTEdu/sbrc26_fingerprint. Antes de executar, registre o ambiente e as versões das dependências. Execute os testes ou componentes que sejam viáveis e relevantes, sem inventar dispositivos, dados ou resultados.
>
> Registre os comandos exatos, códigos de saída, logs e resultados observados. Indique quais partes do fluxo foram executadas, quais não puderam ser executadas e o motivo. Separe execução parcial de reprodução integral. Se o ambiente impedir a execução, descreva a limitação e não conclua automaticamente que o artefato falhou.
>
> Ao final, relacione os resultados observados aos critérios F e R, explicitando o que confirma, confirma parcialmente, contradiz ou não permite verificar a avaliação analítica.

## 4. Instrução da variante de esforço

Acrescentar apenas como metadado da execução, sem mudar o conteúdo do prompt:

- esforço selecionado na interface/API: **[transcrever literalmente]**
- modelo/versão: **[transcrever literalmente]**

Não inserir a frase “pense mais” ou instruções adicionais apenas em uma das condições, pois isso alteraria simultaneamente o prompt e o esforço configurado.

## 5. Instrução da variante de versão

Usar o mesmo prompt-base e a mesma configuração de esforço nas duas versões comparadas. Registrar os identificadores exatos e todas as diferenças que não puderem ser controladas.
