# Verificação completa do artefato com clone local (T8)

> Complementa [AUDITORIA_EVIDENCIAS_T8_GPT6.md](AUDITORIA_EVIDENCIAS_T8_GPT6.md), [ADENDO_HISTORICO_CANONICALIZACAO_TCL.md](ADENDO_HISTORICO_CANONICALIZACAO_TCL.md) e [SAIDA_TESTE_HASH_TCL.md](SAIDA_TESTE_HASH_TCL.md). Aqueles documentos tratam da fixture TCL. Este usa um **clone real** do artefato e o **código original** (`canonicalize_features.py`, `fingerprint_hash.py`) sobre **as 22 execuções** de `testes/`. Atende aos itens pendentes do [checklist de fechamento](STATUS_FECHAMENTO_T8.md) sobre clone com SHA e comandos executáveis sem dispositivo IoT.

Este documento é a **referência de verdade** usada na T8 para conferir as evidências citadas pelas LLMs (itens 10 e 14 do enunciado). Tudo o que está aqui foi verificado diretamente no repositório do artefato. Os comandos estão registrados e podem ser reexecutados.

## 1. Ambiente da verificação

| Item | Valor |
|---|---|
| Artefato | https://github.com/GT-IoTEdu/sbrc26_fingerprint |
| Commit verificado | `167f48792858630020a408147ade001e5c977f78` (09/05/2026, último commit) |
| Data da verificação | 23/11/2026 |
| Sistema | Linux x86_64, Python 3.13 |
| Executor | Claude Opus 5.5 (`claude-opus-5-5`), em ambiente de nuvem com shell e acesso ao GitHub. **Não é uma rodada da matriz de configurações**: é verificação de referência, feita com um script reexecutável por qualquer pessoa |
| Script | [`recalcular_hashes_testes.py`](recalcular_hashes_testes.py) |
| Saída completa | [`dados/recalculo_hashes_testes.csv`](dados/recalculo_hashes_testes.csv) |

Limitação: o ambiente não tinha nmap, p0f, tshark, dumpcap nem dispositivos IoT. Por isso o pipeline de captura em rede **não** foi executado. Foram executadas as etapas offline (canonicalização + hash) sobre os bundles brutos que os autores deixaram em `testes/`.

## 2. Evidências relacionadas ao Selo F

| # | Evidência (citada na T7) | Quem citou | Verificação no artefato | Resultado |
|---|---|---|---|---|
| F1 | Existe Dockerfile e docker-compose | Grok | `Dockerfile` (Ubuntu 22.04 + nmap, tshark, p0f) e `docker-compose.yml` (network_mode host, NET_ADMIN/NET_RAW) presentes | **Confirmada** |
| F2 | README traz dependências, instalação e exemplo mínimo | Claude, Grok | Seções *Requirements*, *Installation*, *Docker*, *Minimal Working Example* presentes | **Confirmada** |
| F3 | Há opções de CLI não documentadas no README | Claude | Das 12 opções do `--help`, só `--seconds`, `--iface` e `--cleanup` aparecem no README. Não documentadas: `--mode`, `--wsl_distro`, `--dumpcap_path`, `--canon_policy`, `--probe_count`, `--probe_delay`, `--log-level`, `--log-console`, `--scan-max-hosts` | **Confirmada** |
| F4 | `iot_id_fingerprint.py --help` executa | Grok | `python3 iot_id_fingerprint.py --help` → exit 0, uso impresso | **Confirmada (E)** |
| F5 | Canonicalização + hash executam sobre dados reais | Claude, Grok | `python3 fingerprint_hash.py testes/<run>/fingerprint.json --policy {stable,rich}` executa e imprime CANON_STRING e hash | **Confirmada (E)** |
| F6 | Fluxo completo de rede não roda sem dispositivo IoT | Claude, Grok | Requer `--iface`, privilégios de captura e um alvo na LAN (README, Hardware/Requirements) | **Confirmada** (limitação de ambiente, não falha do artefato) |

Prova de execução (F5), execução TCL `192.168.59.106_20260324_214710`:

```
$ python3 fingerprint_hash.py testes/192.168.59.106_20260324_214710/fingerprint.json --policy stable
=== FINGERPRINT_HASH ===
3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961
$ python3 fingerprint_hash.py testes/192.168.59.106_20260324_214710/fingerprint.json --policy rich
=== FINGERPRINT_HASH ===
e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51
armazenado: e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51
```

## 3. Evidências relacionadas ao Selo S

| # | Evidência | Verificação | Resultado |
|---|---|---|---|
| S1 | Ausência de arquivo LICENSE separado | Não há `LICENSE*`. A licença (BSD, RNP) está só numa seção do README | **Confirmada** |
| S2 | Arquivos compilados versionados | `__pycache__/*.cpython-39.pyc` versionados | **Confirmada** |
| S3 | `testes/` descrito como "test scripts" mas contém saídas | README: *"testes/ # Test scripts and validation data"*. O conteúdo são saídas de execuções (logs, JSON, hashes) e notas em `.md`/`.txt`; não há scripts de teste | **Confirmada** |
| S4 | Sem suíte de testes automatizados | Não há pytest/unittest nem diretório `tests/` | **Confirmada** |
| S5 | Arquivo principal grande | `iot_id_fingerprint.py` tem 1.271 linhas (43 KB) | **Confirmada** |

## 4. Evidências relacionadas ao Selo R (recálculo independente)

Recálculo de **todas as 22 execuções** de `testes/`. Todos os logs registram `canon_policy=stable`. Em todas, o SHA-256 do `features_canon.txt` armazenado é igual ao hash armazenado, ou seja, os registros dos autores são internamente consistentes.

| Dispositivo (IP) | Execuções | Data | Hash armazenado | `stable` atual | `rich` atual | Situação |
|---|---|---|---|---|---|---|
| TCL Smart TV Pro (.106) | 6 | 24/03 | `e20c4825` | `3ce29174` ✗ | `e20c4825` ✓ | Reproduz só com `rich`, embora o log diga `stable` |
| Xiaomi MiTV-AESP0 (.105) | 5 | 24/03 | `6397f472` | `1468ff0c` ✗ | `cadeb628`/`648c6cd4` ✗ | **Não reproduz com nenhuma política** |
| Sem UPnP (.100)¹ | 1 | 24/03 | `5b60133e` | ✓ | ✓ | Reproduz (canon só com TTL) |
| Sem UPnP (.100)¹ | 2 | 24/03 | `8ebcb041`, `2031f041` | `a08a14b7` ✗ | `a08a14b7` ✗ | Não reproduz |
| Samsung UN32J4303 (.111) | 5 | 25/03 | `1f4e8c4a` | ✓ | `a3e1a812` ✗ | **Reproduz com `stable`** (coerente com o log) |
| Sem UPnP (.3) | 3 | 25/03 | `a08a14b7` (2×), `5b60133e` (1×) | ✓ | ✓ | Reproduz, mas o mesmo IP gerou 2 hashes diferentes |

¹ O documento dos autores `testes/artigo-sbseg-fingerprint.md` identifica `192.168.59.100` como "Smartphone Samsung".

**Resumo:** 9 das 22 execuções reproduzem com a política registrada (`stable`). Outras 6 (TCL) reproduzem só com `rich`. As 5 do Xiaomi e 2 do `.100` não reproduzem.

### 4.1 Diagnóstico das divergências

- **TCL.** A CANON_STRING armazenada inclui `nmap.name` e `nmap.server`. No código atual, esses campos só entram na política `rich`. Ao mesmo tempo, `testes/artigo-sbseg-fingerprint.md` (seção 5.1) afirma que `server` foi removido do `stable`. A explicação mais provável é que o hash foi gerado com uma versão anterior da canonicalização.
- **Xiaomi.** A CANON_STRING armazenada inclui `name`, mas não `server`. Essa combinação não é produzida pelo código atual em nenhuma política, o que é mais um indício de versão anterior do código.
- **`.100` (2ª e 3ª execuções).** A CANON_STRING armazenada não tem `sack_perm` e `ts_present`, que o código atual inclui.
- **Relação com o adendo histórico.** O [adendo](ADENDO_HISTORICO_CANONICALIZACAO_TCL.md) mostra que a versão de 24/03 (`00f38c0`) incluía os quatro campos Nmap sem restrição por política. Isso explica o TCL. Já o Xiaomi armazenado tem `name` **sem** `server`, combinação que não sai daquela regra aplicada ao bundle atual (que contém `server`). A causa específica do Xiaomi fica **não determinada**.
- **Padrão temporal.** Todas as execuções de **24/03** com mais campos que o TTL divergem. Todas as de **25/03** reproduzem. O histórico do artefato mostra `canonicalize_features.py` alterado em 24/03 (`00f38c0`), 25/03 (`f2b8930`), 27/03 e 08/05. Isso é compatível com resultados de 24/03 gerados antes da versão final do código. A explicação é uma inferência a partir das datas; não foi provada fazendo checkout das versões antigas.

### 4.2 Tabela "Reference Fingerprints" do README (15 linhas)

| Hash | Dispositivo no README | Dados brutos em `testes/`? | Verificação |
|---|---|---|---|
| `e20c4825` | TCL Smart TV Pro | Sim | Só com `rich` |
| `1f4e8c4a` | Samsung UN32J4303 (1) e (2) | Sim | ✓ `stable` |
| `6397f472` | Xiaomi | Sim | ✗ |
| `5b60133e` | IP Camera Model B | Hash presente, mas em execuções dos IPs `.100` e `.3`, nenhuma identificada como câmera | Corresponde a uma CANON_STRING só com `{"pcap_syn":{"ttl":"64"}}`, ou seja, uma impressão degenerada compartilhada por hosts diferentes |
| `410528d0` | Samsung 55" | Só log de console (`testes/smartTV.txt`) | ✓ SHA-256 da CANON_STRING impressa = hash impresso |
| `93ef878c` | Impressora HP | Só log de console (`testes/impressoraWifi.txt`) | ✗ SHA-256 da CANON_STRING impressa = `2e7933c6…` (diferente do hash impresso) |
| `994f1313`, `14407342`, `993e9afc`, `50f17366`, `dce0ee76`, `c61f2883` | UnionTV, FiberHome, Lâmpada, Xbox, TP-Link, Câmera A | Não | Não verificável offline |

### 4.3 Correções em relação à T7

- A T7 ([`../EVIDENCIAS_REPRODUTIBILIDADE.md`](../EVIDENCIAS_REPRODUTIBILIDADE.md)) associou `5b60133e` a "IP Camera Model B, compatibilidade parcial". Em `testes/` esse hash aparece apenas em execuções dos IPs `.100` (smartphone, segundo os autores) e `.3`. Não há execução identificada como câmera. O hash reproduz, mas representa só o TTL.
- A T7 disse que o Xiaomi "não foi reproduzido diretamente". Confirmado, e com um detalhe novo: ele não reproduz **nem com `rich`**.
- A divergência TCL stable × rich da T7 está **confirmada exatamente**.

## 5. Como usar nas rodadas da T8

Ao preencher a seção "Verificação das evidências" de [RESULTADOS_T8.md](RESULTADOS_T8.md), classifique cada evidência citada pela LLM como:

- **Confirmada:** consta nas tabelas acima ou foi conferida no repositório.
- **Inexistente:** a LLM citou algo que não existe no artefato.
- **Incorreta:** existe, mas foi descrita errado (ex.: afirmar que o TCL reproduz com `stable`).
- **Não verificável:** depende de dispositivo ou rede.

Indicadores objetivos para comparar configurações (T8-C/G/GM-01 × -02):

1. Detectou a divergência TCL `stable` × `rich`?
2. Detectou que o Xiaomi não reproduz com nenhuma política?
3. Distinguiu resultado dos autores (A) de execução independente (E)?
4. Citou alguma evidência inexistente?

## 6. Reexecução

```bash
git clone https://github.com/GT-IoTEdu/sbrc26_fingerprint.git
git -C sbrc26_fingerprint checkout 167f48792858630020a408147ade001e5c977f78
python3 docs/tarefa8/recalcular_hashes_testes.py sbrc26_fingerprint saida.json
```
