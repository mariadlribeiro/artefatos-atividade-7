# Registro de execução e rastreabilidade — T8

**Data:** 19/10/2026  
**Objetivo:** recuperar a linha de base T7, preservar respostas T8, tentar executar o artefato e aprofundar a divergência de canonicalização.  
**Repositório do artefato:** https://github.com/GT-IoTEdu/sbrc26_fingerprint  
**Branch consultada:** `main`

## 1. Esclarecimento sobre a linha de base da T7

Os documentos disponíveis da Tarefa 7 (`docs/RESULTADOS_LLM.md`, `docs/RELATORIO_COMPLETO.md`, `docs/PROMPT_PADRONIZADO.md`) resumem avaliações de Claude, Grok e Gemini.

**Correção metodológica:** conforme esclarecimento da responsável, ChatGPT não foi utilizado na Tarefa 7. Assim, não existe transcrição ChatGPT-T7 a recuperar e não se devem criar resultados D/F/S/R para esse modelo na linha de base. A comparação T7–T8 é exploratória entre os modelos documentados na T7 e GPT-6 na T8, não uma comparação longitudinal do mesmo modelo.

## 2. Integridade das transcrições T8

### T8-GPT6-01 — esforço padrão

O arquivo `T8_GPT6_PADRAO.md` é um registro estruturado e explicitamente **não literal**. Não foi possível recuperar a transcrição integral palavra por palavra da resposta original a partir das fontes disponíveis nesta sessão.

### T8-GPT6-02 — esforço alto solicitado

A avaliação da rodada anterior está disponível na conversa, mas não há uma captura literal recuperável por ferramenta nesta sessão para anexá-la com garantia de fidelidade. O relatório `RELATORIO_COMPLETO_T8.md` e o resumo da rodada não devem ser rotulados como transcrições literais.

**Ação de integridade:** preservar os registros existentes com seu rótulo correto. Para futuras rodadas, copiar a resposta integral imediatamente para um arquivo dedicado antes de editar ou resumir. Uma nova avaliação redigida agora deve receber um novo ID e não ser apresentada como transcrição retroativa da resposta anterior.

## 3. Tentativa real de obter o repositório e executar o pipeline

Comando executado neste ambiente:

```bash
git clone --depth 1 https://github.com/GT-IoTEdu/sbrc26_fingerprint.git /tmp/iotid
```

Resultado observado:

```text
Cloning into '/tmp/iotid'...
fatal: unable to access 'https://github.com/GT-IoTEdu/sbrc26_fingerprint.git/': Could not resolve host: github.com
```

O comando terminou com código de saída **128**. Portanto, o clone não foi criado e não foi possível instalar dependências a partir do repositório nem executar o pipeline de rede nesta tentativa. O acesso ao conteúdo por meio da integração GitHub permitiu inspeção documental, mas não equivale a uma cópia local executável.

O README do IoT-ID recomenda Linux, Python 3.8+, acesso à LAN, privilégios para sondagem/captura e ferramentas externas (Nmap, nping, dumpcap, tshark e p0f). Também requer dispositivo(s) de rede acessíveis para um ensaio real. Nenhuma captura de tráfego ou execução ponta a ponta foi realizada nesta sessão.

**Classificação:** tentativa de execução bloqueada por DNS/ambiente; não é teste funcional concluído e não demonstra falha do artefato.

## 4. Execução isolada para investigar stable/rich

Foi executado um script independente com a fixture extraída dos arquivos públicos da execução TCL Smart TV Pro. O script replica as regras documentadas de inclusão dos campos para comparar as representações canônicas; não importa o módulo original, não executa o pipeline de rede e não substitui uma reprodução integral. O script está em [`verificar_hash_canonico_tcl.py`](verificar_hash_canonico_tcl.py).

### Entrada utilizada

- `manufacturer`: `TCL`
- `model_name`: `Smart TV Pro`
- `name`: `Smart TV Pro`
- `server`: `UPnP/1.0, DLNADOC/1.50 Platinum/1.0.5.13`
- `server_synack_raw_sig_set`: `4:64+0:0:1460:65535,0:mss:df:0`
- `pcap_syn`: `mss=1460`, `ttl=64`, `window_size=65535`

### Resultados observados

| Política reconstruída | Tamanho da string | SHA-256 calculado | Corresponde ao registro esperado? |
|---|---:|---|---|
| `stable` | 203 caracteres | `3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961` | Sim, corresponde ao hash descrito para stable no estudo de variáveis imutáveis |
| `rich` | 277 caracteres | `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51` | Sim, corresponde ao hash do log/arquivo histórico rotulado stable |

A string de 277 caracteres contém `nmap.name` e `nmap.server`. No código atual inspecionado, esses campos são incluídos na política `rich`, enquanto `stable` inclui `manufacturer` e `model_name` sem `name/server`. O hash histórico é reproduzido pela representação rica; o hash documentado para stable é reproduzido pela representação estável.

### Interpretação e limites

A divergência foi reproduzida no nível da **serialização/hash de uma fixture**. Isso sustenta a conclusão de que o registro histórico contém os campos de `rich`, apesar de estar rotulado `stable`. Não estabelece a causa histórica: pode haver versão anterior do código, alteração de política ou inconsistência no registro. Para resolver a causa, seria necessário localizar o commit/versão exata que gerou o log, comparar o arquivo de canonicalização daquela versão e, idealmente, executar o bundle histórico através das duas versões.

## 5. Estado atualizado por critério

| Critério | Estado após esta rodada |
|---|---|
| D — Disponibilidade | Acesso público aos arquivos confirmado pela integração GitHub; clone por Git falhou nesta execução por resolução DNS. |
| F — Funcionalidade | Pipeline de rede não executado; permanece sem confirmação ponta a ponta. |
| S — Sustentabilidade | Código/documentação inspecionados; manutenção longitudinal não testada. Divergência histórica reforça a necessidade de rastreabilidade de versões. |
| R — Reprodutibilidade | Hashes da fixture reconstruídos de forma independente; divergência stable/rich confirmada. Pipeline e captura real não reproduzidos. |

## 6. Pendências para completar

- [ ] Confirmar, se necessário, se os documentos T7 disponíveis representam todos os modelos utilizados; os registros consultados documentam Claude, Grok e Gemini.
- [ ] Copiar as respostas integrais de cada nova rodada T8 sem alterações e registrar ID, data, modelo exibido e esforço selecionado.
- [ ] Obter o repositório por uma conexão com DNS funcional.
- [ ] Executar os testes de ajuda/CLI e canonicalização em ambiente Python compatível.
- [ ] Executar pipeline de rede somente em LAN autorizada e com dispositivo de teste disponível.
- [ ] Identificar o commit do artefato que gerou a execução TCL de 24/03/2026.
- [ ] Atualizar a comparação T7×T8 depois da recuperação da resposta original e de evidências executadas adicionais.

## 7. Conclusão

Conforme esclarecimento da responsável, ChatGPT não foi utilizado na T7, portanto não há transcrição ChatGPT-T7 a recuperar. As transcrições literais das duas rodadas T8 anteriores também não foram recuperadas. A tentativa real de clonagem do artefato falhou por DNS, impedindo a execução ponta a ponta. Foi possível, entretanto, realizar uma verificação isolada e reproduzível dos hashes stable/rich: o hash histórico corresponde à string rica de 277 caracteres, enquanto a política estável descrita no estudo gera a string de 203 caracteres e o hash `3ce29174...`. A causa histórica continua em aberto.

Não há evidência suficiente para afirmar que o pipeline completo foi executado nesta sessão ou que os resultados dos critérios F/R foram integralmente reproduzidos.
