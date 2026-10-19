# Auditoria de evidências — T8-GPT6-01

- **Data da auditoria:** 2026-10-19
- **Objeto:** afirmações técnicas na resposta T8 registrada como GPT-6, esforço padrão
- **Repositório do artefato:** https://github.com/GT-IoTEdu/sbrc26_fingerprint
- **Branch do artefato consultada:** `main`
- **Natureza:** revisão documental/código + verificação independente parcial de hash; não é execução do pipeline de rede
- **Integridade:** nenhum arquivo do repositório do artefato foi alterado.

## 1. Busca da resposta original do ChatGPT na Tarefa 7

Foram consultados:
- `docs/PROMPT_PADRONIZADO.md`
- `docs/RESULTADOS_LLM.md`
- `docs/RELATORIO_COMPLETO.md`
- A biblioteca de arquivos acessível no ChatGPT, por busca semântica e listagem dos arquivos disponíveis.

**Resultado:** a resposta original do ChatGPT da Tarefa 7 não foi localizada nas fontes acessíveis nesta auditoria. Os relatórios do repositório descrevem avaliações de Claude, Grok e Gemini; o `PROMPT_PADRONIZADO.md` afirma que o prompt foi usado como base para três avaliações. Isso confirma que o material atualmente registrado no repositório não contém uma linha de resultado do ChatGPT. Não prova que a responsável não tenha uma cópia salva em outro lugar.

**Consequência:** as quatro decisões D/F/S/R do ChatGPT na T7 continuam pendentes. Não inferir os resultados a partir da resposta GPT-6 da T8 nem de outros LLMs. Para fechar a comparação, será necessário incorporar a resposta original ou registrar formalmente que não foi recuperada.

## 2. Existência dos arquivos citados na resposta T8

Os caminhos abaixo foram consultados diretamente no repositório público. Os valores SHA são os identificadores Git Blob dos arquivos na revisão consultada.

| Arquivo | Existe? | SHA do blob | O que confirma |
|---|---|---|---|
| `README.md` | Sim | `18607e4ef668224fc4aa13c4085f206cf38a2132` | Arquitetura, requisitos, instalação, exemplos e seção de reprodução |
| `iot_id_fingerprint.py` | Sim | `aa2940b76c30f3a2ef451f8472454f1dd296b813` | Pipeline principal e invocação de ferramentas externas |
| `iot_net_scanner.py` | Sim | `2f80db752020ce53e20c45ec14c66e682a6bb94a` | Descoberta de rede/UPnP |
| `canonicalize_features.py` | Sim | `c82540bf2329f0e702e28ea91c32939d2d1e154f` | Normalização, construção do objeto canônico e serialização JSON |
| `fingerprint_hash.py` | Sim | `e325146bcac91833b0ad201e1ba7e4ff43dbdfdb` | Cálculo de hash a partir da string canônica |
| `requirements.txt` | Sim | `2d4097affef632fbbd02c69123fa99d78495c7d8` | Declara `requests>=2.25.0,<3` |
| `Dockerfile` | Sim | `45ca8fbdff706dccd7d3e31b158aca3543e2816d` | Imagem Ubuntu 22.04 e dependências de sistema |
| `docker-compose.yml` | Sim | `f12c56715ce4d10a22806e677818ce46853ae3c1` | Rede host e capacidades `NET_ADMIN`/`NET_RAW` |

A existência dos arquivos e a correspondência dos seus papéis foram confirmadas. Isso não comprova, por si só, que o pipeline funcione em qualquer ambiente.

## 3. Fluxo e dependências

O README descreve o seguinte fluxo: Nmap/UPnP, captura com dumpcap, sondagem TCP SYN por nping, extração passiva por p0f, extração de atributos de PCAP por tshark, canonicalização e SHA-256. O código principal usa subprocessos para invocar comandos externos.

O README indica Linux, Python 3.8 ou superior, acesso à LAN e privilégios para sondagem/captura. O `requirements.txt` declara somente a dependência Python `requests>=2.25.0,<3`; as demais ferramentas são dependências de sistema. O Dockerfile instala Nmap, TShark, Wireshark Common, p0f e iproute2; o compose usa rede host e concede capacidades de rede.

**Conclusão:** as afirmações da resposta sobre módulos, dependência Python, contêiner e ferramentas de rede são sustentadas pela documentação e pelos arquivos atuais. A versão de cada ferramenta declarada no README é uma especificação/recomendação documental, não uma medição de versão realizada nesta auditoria.

## 4. Registros de execução dos autores versus suíte de testes

A árvore Git consultada tem 383 entradas (292 arquivos). Em `testes/` há 278 arquivos, principalmente saídas de execuções e registros: 66 JSON, 179 TXT, 28 LOG, 3 Markdown e 2 PNG. Há pastas de execuções identificadas por IP e timestamp, contendo bundles, strings canônicas, hashes e logs de pipeline.

A busca pela árvore não encontrou arquivos convencionais `test_*.py` ou `*_test.py`, nem `pytest.ini`, `tox.ini` ou `pyproject.toml`. Isso significa que a árvore examinada contém evidências de execução e dados de teste, mas não foi localizada uma suíte Python automatizada convencional. Não significa que o artefato não possa ser testado manualmente ou que não existam testes fora dessa árvore.

## 5. Verificação independente parcial do SHA-256

Foi selecionado o registro TCL Smart TV Pro:

- Log: [`testes/192.168.59.106_20260324_220537/fingerprint_pipeline.log`](https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/testes/192.168.59.106_20260324_220537/fingerprint_pipeline.log)
- String canônica armazenada: [`features_canon.txt`](https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/testes/192.168.59.106_20260324_220537/features_canon.txt)
- Hash armazenado: [`fingerprint_sha256.txt`](https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/testes/192.168.59.106_20260324_220537/fingerprint_sha256.txt)
- Hash armazenado: `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51`

O log relata `canon_policy=stable` e registra uma string canônica de 277 caracteres contendo `nmap.name` e `nmap.server`. O hash SHA-256 dessa string, recalculado independentemente a partir do texto armazenado, corresponde ao hash `e20c4825...` do arquivo.

**Divergência encontrada:** o `canonicalize_features.py` atualmente publicado adiciona `name` e `server` ao objeto canônico IoT somente quando a política é `rich`; na política `stable`, inclui `manufacturer` e `model_name`, sem esses dois campos. Para a string canônica correspondente à política `stable` descrita no documento `testes/estudo-variaveis-imutaveis-smarttv.md`, o SHA-256 calculado independentemente é `3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961`, diferente do hash armazenado.

Isso mostra uma inconsistência entre o log/artefatos históricos rotulados como `stable` e o comportamento descrito pelo código atual. A causa exata não foi estabelecida nesta auditoria: pode haver diferença de versão entre o código que gerou os registros e o código atualmente publicado, ou registros/documentação históricos que não correspondem à versão atual. Não é correto ocultar essa divergência nem declarar que o pipeline completo foi reproduzido.

Seis arquivos `fingerprint_sha256.txt` de execuções TCL listadas em `testes/192.168.59.106_20260324_*` foram conferidos e contêm o mesmo hash `e20c4825...`. Isso é evidência documental de consistência entre os valores armazenados pelos autores, não uma reprodução independente de seis execuções.

**Escopo da verificação:** foi recalculado o hash de uma string fornecida pelo repositório; não foi executado o pipeline de captura, extração ou canonicalização a partir de uma rede/dispositivo IoT real. Portanto, classificar como verificação independente parcial da etapa de hash, com entrada fornecida pelos autores.

## 6. Resultado por afirmação da resposta T8

| Afirmação | Resultado da auditoria |
|---|---|
| O repositório e o README são públicos e consultáveis | Confirmado |
| Os quatro módulos citados existem | Confirmado |
| Há `Dockerfile`, `docker-compose.yml` e `requirements.txt` | Confirmado |
| O fluxo usa ferramentas de sondagem/captura e SHA-256 | Confirmado documentalmente e por inspeção de código |
| Há exemplos e hashes registrados pelos autores | Confirmado |
| Os resultados de referência foram reproduzidos nesta avaliação | **Não**; apenas uma string canônica fornecida pelos autores teve seu hash recalculado |
| O pipeline completo foi executado | **Não** |
| A ausência de ferramentas/DNS relatada na resposta anterior foi reproduzida nesta auditoria | **Não**; o relato de ambiente anterior não tem log bruto anexado |
| A resposta original do ChatGPT da T7 foi recuperada | **Não** |
| Há uma divergência entre registros históricos `stable` e código atual | Confirmada na comparação do log, da string armazenada e do código atual |

## 7. Efeito sobre D/F/S/R

| Critério | Estado após auditoria |
|---|---|
| **D — Disponibilidade** | Acesso público ao repositório e aos arquivos confirmado. |
| **F — Funcionalidade** | Não confirmado por execução completa; código e fluxo foram inspecionados. |
| **S — Sustentabilidade** | Modularização e configuração documentadas; a árvore não apresenta suíte convencional de testes automatizados, e a diferença entre registros e código atual é um ponto de manutenção/rastreabilidade. Não foi avaliada manutenção a longo prazo. |
| **R — Reprodutibilidade** | Evidência de repetição dos hashes armazenados pelos autores; uma verificação parcial do hash foi feita. A divergência entre os registros rotulados `stable` e o código atual impede afirmar que a reprodução independente do procedimento foi concluída. |

Essas conclusões são resultados desta auditoria, não decisões oficiais de concessão ou retirada de selos. Os quatro selos oficiais aparecem na linha do IoT-ID na página oficial de resultados do SBRC 2026: https://doc-artefatos.github.io/sbrc2026/results.html.

## 8. Variantes de LLM/esforço

Não foi possível controlar o seletor de modelo/esforço da interface ChatGPT por meio das ferramentas disponíveis nesta sessão, nem executar diretamente Claude, Grok ou Gemini com configurações controladas. Assim, **nenhuma nova variante de LLM/esforço é declarada como executada**. A resposta T8-GPT6-01 permanece a única resposta de variante registrada. Não comparar uma nova resposta sem identificar modelo e esforço reais.

Para realizar a comparação controlada, executar manualmente o mesmo prompt em duas configurações disponíveis, salvar cada resposta integral sem edição e registrar o nome de modelo e o esforço exatamente como exibidos. Não presumir equivalência de esforços entre provedores.

## 9. Fontes principais

- README: https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/README.md
- Canonicalização atual: https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/canonicalize_features.py
- Hash atual: https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/fingerprint_hash.py
- Pipeline principal: https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/iot_id_fingerprint.py
- Estudo de variáveis estáveis: https://github.com/GT-IoTEdu/sbrc26_fingerprint/blob/main/testes/estudo-variaveis-imutaveis-smarttv.md
- Execução TCL: https://github.com/GT-IoTEdu/sbrc26_fingerprint/tree/main/testes/192.168.59.106_20260324_220537
- Resultados oficiais: https://doc-artefatos.github.io/sbrc2026/results.html
