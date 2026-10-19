# T8-GPT6-01 — Avaliação do IoT-ID com GPT-6 e esforço padrão

- **Data registrada:** 2026-10-19
- **Provedor/modelo exibido:** GPT-6
- **Versão exata:** não informada pela interface
- **Configuração:** esforço de raciocínio padrão
- **Prompt:** `docs/PROMPT_PADRONIZADO.md`
- **Tipo de avaliação:** análise documental e de código; tentativa de execução independente não concluída
- **Status do registro:** resposta preservada; conclusões provisórias
- **Resposta integral original:** foi produzida na conversa da Tarefa 8. Este arquivo preserva o conteúdo e organiza as evidências para registro. As conclusões não equivalem a selos oficiais.

## 1. Síntese

A avaliação separa a análise do repositório da execução independente. Encontrar comandos e resultados no README não significa que o programa foi executado nem que os experimentos foram reproduzidos.

O artefato avaliado é **IoT-ID: Deterministic Device Identity from Hybrid Network Fingerprinting**, no repositório [GT-IoTEdu/sbrc26_fingerprint](https://github.com/GT-IoTEdu/sbrc26_fingerprint). A documentação descreve uma abordagem de fingerprinting de dispositivos IoT que combina sondagem ativa e análise passiva de tráfego, normaliza atributos e gera uma impressão digital com SHA-256. A descrição detalhada deve ser conferida no [README do artefato](https://github.com/GT-IoTEdu/sbrc26_fingerprint).

## 2. Ambiente e tentativa de execução

A resposta da avaliação registrou o seguinte ambiente:

| Item | Valor registrado |
|---|---|
| Sistema operacional | Linux |
| Arquitetura | x86_64 |
| Python | 3.13.5 |
| `requests` | 2.32.5 |
| Clonagem por Git | Falhou por erro de resolução DNS |
| Código de saída da clonagem | 128 |
| `nmap`, `nping`, `dumpcap`, `tshark`, `p0f` | Não encontrados no ambiente relatado |
| Docker | Não encontrado no ambiente relatado |

Comando tentado:

```bash
git clone --depth 1 https://github.com/GT-IoTEdu/sbrc26_fingerprint.git /tmp/sbrc26_fingerprint
```

**Resultado relatado:** a clonagem não foi concluída porque houve falha na resolução de `github.com`. A resposta consultou páginas e arquivos do GitHub por uma integração, o que permitiu uma análise documental parcial, mas não substituiu a clonagem nem a execução do pipeline.

**Limitação do registro:** não foi anexado um log bruto de terminal. Os detalhes do ambiente e da tentativa são preservados como informações relatadas pela resposta de avaliação; não devem ser apresentados como um log de execução auditado independentemente.

## 3. Avaliação por critério

### D — Disponibilidade

**Evidências citadas**
- **[D]** O repositório é público e sua documentação pode ser consultada online.
- **[D]** O README descreve o artefato, sua estrutura, requisitos, instalação, utilização, resultados de exemplo e considerações de segurança.
- **[C]** A análise relatou ter consultado módulos principais, arquivo de dependências e arquivos de configuração de contêiner.

**Limitação:** a clonagem por Git não foi concluída neste ambiente. Isso não demonstra que o repositório esteja indisponível para outros usuários.

**Conclusão provisória:** há evidência favorável de disponibilidade pública e documental. O download via Git não foi concluído na tentativa relatada.

### F — Funcionalidade

**Evidências citadas**
- **[D]** O README descreve o fluxo de descoberta ativa, captura de pacotes, sondagem TCP, extração de características, canonicalização e geração de hash SHA-256.
- **[C]** A resposta relata ter consultado os módulos `iot_id_fingerprint.py`, `iot_net_scanner.py`, `canonicalize_features.py` e `fingerprint_hash.py`.
- **[C]** A análise relata funções para normalização de características, ordenação de chaves JSON e cálculo de hash a partir de uma representação canônica.
- **[A]** O README contém exemplos de saída e hashes de referência. Esses valores são resultados documentados pelos autores, não resultados produzidos nesta avaliação.

**Limitação:** o pipeline completo não foi executado. A tentativa de clonagem falhou e as ferramentas de rede necessárias não estavam disponíveis no ambiente relatado.

**Conclusão provisória:** a implementação e o procedimento estão documentados, mas a produção dos resultados esperados não foi confirmada por execução independente. Não há base para declarar falha funcional do artefato.

### S — Sustentabilidade

**Evidências citadas**
- **[C]** A organização relatada separa responsabilidades em módulos, incluindo canonicalização, geração de hash, descoberta e pipeline principal.
- **[D]** Há documentação de instalação, parâmetros, arquivos de saída, execução em contêiner e cuidados de segurança.
- **[C]** O `requirements.txt` consultado declara `requests>=2.25.0,<3`.

**Pontos de atenção**
- A execução depende de ferramentas externas e pode exigir privilégios elevados para captura e sondagem.
- O procedimento documentado depende de Linux e de dispositivos acessíveis na rede local.
- A faixa de versões da dependência Python não fixa uma versão exata, o que pode afetar a reconstrução do ambiente.
- Modularidade e documentação são indícios favoráveis, mas não demonstram, por si sós, manutenção a longo prazo.

**Conclusão provisória:** a organização do código e a documentação favorecem manutenção e adaptação. A sustentabilidade foi avaliada por evidências estruturais, não por manutenção prolongada ou adaptação prática.

### R — Reprodutibilidade

**Evidências citadas**
- **[D]** O README descreve um procedimento para repetir medições e comparar fingerprints.
- **[A]** Há hashes de referência e exemplos de dispositivos apresentados pelos autores.
- **[D]** A documentação reconhece que a reprodução estrita depende dos mesmos dispositivos físicos e versões de firmware, além de descrever uma modalidade funcional e comparativa.

**Três níveis que não devem ser confundidos**
1. **Resultados dos autores:** há valores de referência documentados.
2. **Repetição no ambiente original:** os exemplos não foram repetidos pela avaliação.
3. **Reconstrução independente:** não foi possível reconstruir e executar o experimento completo a partir do código, das dependências e dos dispositivos necessários.

**Conclusão provisória:** o procedimento de reprodução está descrito, mas a reprodutibilidade independente permanece não verificada. As limitações do ambiente não demonstram que os experimentos sejam irreprodutíveis.

## 4. Quadro-resumo

| Critério | Evidência analítica | Execução independente | Conclusão desta avaliação |
|---|---|---|---|
| **D — Disponibilidade** | Repositório público e documentação consultáveis | Clonagem não concluída | Favorável quanto à disponibilidade pública |
| **F — Funcionalidade** | Código e procedimento documentados | Pipeline completo não executado | Não confirmada por execução |
| **S — Sustentabilidade** | Código modular e documentação | Sem teste de manutenção ou adaptação | Estrutura favorável, com ressalvas |
| **R — Reprodutibilidade** | Procedimentos e hashes de referência documentados | Resultados não reproduzidos independentemente | Não verificada |

Esta tabela resume a análise realizada; não representa atribuição ou retirada de selos oficiais.

## 5. Relação com a avaliação oficial

A resposta consultou a página oficial de resultados do SBRC 2026 e registrou que o IoT-ID recebeu os quatro selos — Disponibilidade, Funcionalidade, Sustentabilidade e Reprodutibilidade. Consulte a [página oficial de resultados](https://doc-artefatos.github.io/sbrc2026/results.html).

A avaliação oficial e esta análise têm condições e evidências diferentes. A ausência de reprodução nesta execução não contradiz necessariamente os selos oficiais; significa apenas que esta avaliação não conseguiu reproduzir os experimentos.

## 6. Discussão

A principal evidência favorável é a existência de repositório público, documentação de uso, requisitos explícitos, módulos separados e procedimentos para gerar e comparar fingerprints. A documentação também descreve dependências de rede e de privilégios e reconhece limitações associadas à disponibilidade dos mesmos dispositivos físicos.

A principal limitação desta avaliação é a ausência de execução independente. A falha de clonagem por DNS e a indisponibilidade das ferramentas necessárias impedem confirmar funcionalidade e reproduzir resultados. Esses fatores são limitações do ambiente, não evidências de defeito no artefato.

A presença de hashes e logs no repositório comprova que os autores disponibilizaram registros, mas não demonstra que esta avaliação os reproduziu. Para testar reprodutibilidade de forma independente, seria necessário executar o código, registrar as versões instaladas, utilizar um ambiente de rede adequado e comparar os resultados obtidos com os valores de referência.

## 7. Registro da execução T8

- **Modelo registrado:** GPT-6
- **Esforço:** padrão
- **Versão exata:** não informada pela interface
- **Avaliação analítica:** realizada com base na documentação e nos arquivos de código consultados pela resposta
- **Execução independente do pipeline:** não concluída
- **Motivo principal:** falha de resolução DNS ao clonar o repositório; ferramentas de rede ausentes no ambiente relatado
- **Resultados D/F/S/R:** conclusões provisórias conforme as seções acima
- **Resposta preservada no Git:** sim, neste arquivo
- **Evidências verificadas diretamente por uma segunda revisão independente:** não
- **Comparação com a resposta original do ChatGPT na Tarefa 7:** pendente de recuperar e conferir a resposta original

## 8. Referências

- Repositório do artefato: https://github.com/GT-IoTEdu/sbrc26_fingerprint
- README do artefato: https://github.com/GT-IoTEdu/sbrc26_fingerprint
- Resultados oficiais do SBRC 2026: https://doc-artefatos.github.io/sbrc2026/results.html
- Prompt padronizado do experimento: [../PROMPT_PADRONIZADO.md](../PROMPT_PADRONIZADO.md)
