# T8-C-01 e T8-C-02 (Claude): fichas e verificação das evidências

Respostas brutas: [respostas/T8-C-01.md](respostas/T8-C-01.md) e [respostas/T8-C-02.md](respostas/T8-C-02.md). Referência para a verificação: [VERIFICACAO_COMPLETA_ARTEFATO.md](VERIFICACAO_COMPLETA_ARTEFATO.md). Condições de execução: [PROTOCOLO_EXPERIMENTAL.md §12](PROTOCOLO_EXPERIMENTAL.md).

## 1. Configuração

| Campo | T8-C-01 | T8-C-02 |
|---|---|---|
| Modelo | Claude Opus 5.5 (`claude-opus-5-5`) | Claude Opus 5.5 (`claude-opus-5-5`) |
| Esforço | padrão | **máximo** (`effort = max`) |
| Prompt | P1 literal | P1 literal |
| Ambiente | agente novo; Linux em nuvem; shell, git, Python, internet | idem |
| Data | 23/11/2026 | 23/11/2026 |
| Commit avaliado | `167f487` | `167f487` |
| Duração / chamadas de ferramenta / tokens | ≈18 min / 41 / ≈201 mil | ≈66 min / 142 / ≈457 mil |
| Clonou o repositório? | Sim | Sim |
| Executou o pipeline? | Sim, em testbed sintético (6 *namespaces* com UPnP emulado) | Sim, em laboratório L2 isolado (6 *namespaces* com UPnP emulado) |
| Consultou fontes externas? | Não | Sim: instruções oficiais SBRC 2026 e artigo publicado |
| Transcrição literal preservada? | Sim | Sim |

**Única variável alterada entre as duas rodadas: o esforço.** O modelo, o prompt, o ambiente, a data e o commit são os mesmos.

## 2. Decisões

| Selo | T8-C-01 (padrão) | T8-C-02 (máximo) | Oficial |
|---|---|---|---|
| D | Atendido (com ressalvas) | Sustentado | Concedido |
| F | Atendido com ressalvas | Sustentado com ressalvas | Concedido |
| S | Atendido com ressalvas | Sustentado com ressalvas | Concedido |
| R | **Parcialmente atendido** | **Parcialmente sustentado** | Concedido |

As decisões são **idênticas** nas duas configurações.

## 3. Verificação das evidências citadas (F e R)

Legenda: **Conf.** = confirmada diretamente no artefato · **Conf. (log)** = conferida nos registros de execução do avaliador · **Inex.** = inexistente · **Incor.** = incorreta.

| # | Evidência | C-01 | C-02 | Verificação | Situação |
|---|---|:-:|:-:|---|---|
| 1 | Repositório público, clone anônimo, commit `167f487` | ✓ | ✓ | Clone próprio no mesmo commit | Conf. |
| 2 | Sem arquivo `LICENSE`; BSD só no README, sem variante | ✓ | ✓ | `LICENSE` inexistente; README l. 531 | Conf. |
| 3 | `iot_id_fingerprint.py --help` falha em Python 3.8 (l. 633) e 3.9 (l. 656); README declara 3.8+ e Ubuntu 20.04 | ✓ | ✓ | Reexecutado: 3.8 e 3.9 → `TypeError`, código 1; README l. 90–91 | Conf. |
| 4 | `Dockerfile` não instala `sudo`; código chama `sudo nmap` (l. 532, 608) e o orquestrador chama `sudo "$PYTHON"` (l. 143) | ✓ | ✓ | grep no Dockerfile e no código | Conf. |
| 5 | Parser `"Name:" in line` também casa com `Model Name:` | ✓ | ✓ | `iot_id_fingerprint.py` l. 624–628; `iot_net_scanner.py` l. 66–67 | Conf. |
| 6 | Falha de canonização retorna código 0 | ✓ | ✓ | `except Exception` em l. 1105–1109 sem `sys.exit`; `main()` sem código de retorno | Conf. |
| 7 | `fingerprint_subnet.sh` versionado sem bit de execução | ✓ | — | `git ls-files -s` → `100644` | Conf. |
| 8 | Claim #1 usa `cd /fingerprint`, caminho inexistente | ✓ | ✓ | README l. 344 | Conf. |
| 9 | Saída do scanner no README em inglês e no código em português | ✓ | ✓ | README l. 238/242 × `iot_net_scanner.py` l. 116/129 | Conf. |
| 10 | `__pycache__` com `bundle_snapshot.cpython-39.pyc`, de módulo inexistente | ✓ | ✓ | `ls __pycache__`; `bundle_snapshot.py` não existe | Conf. |
| 11 | Sem PCAPs em `testes/` | ✓ | ✓ | Nenhum `*.pcap*` | Conf. |
| 12 | Recomputação dos 22 bundles: integridade 22/22; Samsung reproduz com `stable`; **TCL só com `rich`**; **Xiaomi com nenhuma política** | ✓ | ✓ | Idêntico ao recálculo independente (9/22 com `stable`) | Conf. |
| 13 | Hash da "IP Camera Model B" (`5b60133e…`) = SHA-256 de `{"pcap_syn":{"ttl":"64"}}` | ✓ | ✓ | Recalculado | Conf. |
| 14 | Instabilidade dos hosts sem UPnP nos dados dos autores (.100: 3 hashes em 3 execuções; .3: 2 em 3) | ✓ | ✓ | Conferido em `fingerprint_sha256.txt` | Conf. |
| 15 | Pipeline determinístico no laboratório; modelos idênticos → mesmo hash; L7 desambigua pilhas idênticas (Claim #2) | ✓ | ✓ | Hashes nos diretórios `runs*` de cada avaliador (C-01: `c5cb0fe5` 5×, `e69707b2` 4×, `dfec7471` 3×; C-02: `736497ed` para devA1 e devA2) | Conf. (log) |
| 16 | Hosts sem UPnP e sem portas colidem em `5b60133e…` no laboratório | ✓ | ✓ | C-01: `runs_noupnp` (2 hosts); C-02: devE (3×) | Conf. (log) |
| 17 | Imagem Docker não construída: Docker Hub bloqueado pelo proxy | ✓ | ✓ | Limitação do ambiente, corretamente separada de falha do artefato | Conf. (log) |
| 18 | Script `upnp-info` nunca roda (nmap só varre TCP; o script exige UDP 1900) | — | ✓ | Nenhuma das 22 saídas nmap dos autores contém `upnp-info` | Conf. |
| 19 | Log da impressora inconsistente: SHA-256 da CANON impressa = `2e7933c6…` ≠ `93ef878c…` publicado | — | ✓ | Recálculo independente | Conf. |
| 20 | 5 hashes da tabela sem dados reconstruídos a partir dos atributos do artigo (UnionTV `994f1313`, FiberHome `14407342`, C500 `c61f2883`, Bulb `993e9afc`, Camera B `5b60133e`) | — | ✓ | Recalculados: os 5 batem | Conf. |
| 21 | Xiaomi não reproduz com nenhuma das 8 versões históricas de `canonicalize_features.py`; CANON contém `"name":"TV do quarto"` (apelido configurável) | — | ✓ | `name` conferido; teste das 8 versões conferido nos logs do avaliador | Conf. / Conf. (log) |
| 22 | Hash de host sem UPnP muda com tráfego incidental visível (E13b) | — | ✓ | `lab_runs_summary`: devC `0bd9c28d` (4×) → `254d9d3d` (1×) | Conf. (log) |
| 23 | Versões declaradas (nmap 7.95, tshark 4.4.15) ≠ registradas nos dados dos autores (7.94SVN) | — | ✓ | Saídas nmap em `testes/` | Conf. |

**Resumo:** C-01 citou 17 evidências-chave e C-02, 22. **Nenhuma inexistente, nenhuma incorreta.** Tudo o que pôde ser conferido no artefato foi confirmado; o restante está coerente com os registros de execução dos próprios avaliadores.

## 4. Indicadores-chave

| Indicador | T7 (Claude) | T8-C-01 | T8-C-02 |
|---|---|---|---|
| Detectou a divergência TCL `stable` × `rich`? | Sim | Sim | Sim |
| Detectou que o Xiaomi não reproduz com nenhuma política? | Parcial ("não reproduzido diretamente") | Sim | Sim, inclusive em 8 versões históricas |
| Identificou `5b60133e` como hash degenerado de TTL? | Não | Sim | Sim |
| Detectou a inconsistência do log da impressora? | Não | Não | Sim |
| Separou A de E? | Sim | Sim | Sim, com a categoria extra "E sobre A" |
| Executou o pipeline completo? | Não (execução parcial) | Sim (testbed sintético) | Sim (laboratório emulado) |
| Evidências inexistentes ou incorretas | — | 0 | 0 |
| Selos F e R iguais aos oficiais? | F parcial; R não | F sim; R não | F sim; R não |

## 5. O que o esforço máximo acrescentou (T8-C-02 × T8-C-01)

Com os mesmos veredictos, o esforço máximo **aumentou a cobertura e a profundidade das evidências**, sem mudar nenhuma decisão:

- verificou **todos os 12 hashes distintos** da tabela publicada (7 consistentes, 3 inconsistentes, 2 não verificáveis), contra 4 de 15 linhas na C-01;
- testou as **8 versões históricas** do módulo de canonização;
- encontrou dois problemas novos no artefato: `upnp-info` ineficaz e log da impressora inconsistente;
- mostrou experimentalmente que o hash de hosts sem UPnP depende do tráfego incidental;
- consultou por iniciativa própria as instruções oficiais do SBRC 2026 e o artigo publicado.

Custo: cerca de 2,3 vezes mais tokens, 3,5 vezes mais chamadas de ferramenta e 3,6 vezes mais tempo.
