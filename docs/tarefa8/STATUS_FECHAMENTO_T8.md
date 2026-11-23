# Fechamento da Tarefa 8 — checklist de conclusão

**Estado em 19/10/2026:** documentação consolidada parcialmente; execução integral do artefato e experimento controlado entre configurações ainda não concluídos.

Este documento distingue tarefas concluídas de tarefas que dependem de acesso, ambiente ou novos registros. Não converte pendências em resultados.

## 1. Correções metodológicas concluídas

- [x] Registrar que ChatGPT não foi utilizado na Tarefa 7.
- [x] Manter Claude, Grok e Gemini como os modelos documentados na linha de base T7.
- [x] Tratar GPT-6 como modelo utilizado nas rodadas documentadas da T8, sem alegar comparação longitudinal GPT-6 T7→T8.
- [x] Distinguir o selo oficial do SBRC de uma avaliação analítica independente.
- [x] Distinguir logs e hashes fornecidos pelos autores de execução independente.
- [x] Registrar a tentativa de clonagem bloqueada por DNS como limitação do ambiente, não como falha do artefato.
- [x] Registrar que os arquivos de respostas T8 existentes são sínteses estruturadas, não transcrições literais integrais.

## 2. Verificações documentais feitas

- [x] Consultar diretamente, pela integração GitHub, o README do artefato, `requirements.txt`, `canonicalize_features.py`, `fingerprint_hash.py`, `iot_id_fingerprint.py`, o estudo de variáveis imutáveis da TV TCL e os arquivos públicos de log, representação canônica e hash da execução.
- [x] Confirmar que o README descreve uma cadeia que envolve descoberta Nmap/UPnP, captura de tráfego, sondagem, análise com ferramentas externas, canonicalização e hash.
- [x] Confirmar que `requirements.txt` lista `requests>=2.25.0,<3`; isso não representa todas as dependências do sistema, que são descritas separadamente.
- [x] Conferir que o log TCL declara `canon_policy=stable`, enquanto `features_canon.txt` inclui `nmap.name` e `nmap.server`.
- [x] Conferir que o estudo `estudo-variaveis-imutaveis-smarttv.md` define a política `stable` como usando `manufacturer` e `model_name`, sem `name/server`.
- [x] Registrar a divergência entre o rótulo histórico e os campos do registro.

**Limite:** a consulta direta aos arquivos no GitHub verifica sua existência e conteúdo atual; não prova que a versão atual gerou o log histórico. A causa da divergência continua não determinada.

## 3. Testes e execuções

| Atividade | Estado | Interpretação válida |
|---|---|---|
| Acesso documental via integração GitHub | Concluído parcialmente | Arquivos públicos puderam ser inspecionados |
| Clone Git do repositório no ambiente de execução | Bloqueado por DNS; código 128 | Não houve clone local |
| Pipeline de rede IoT-ID ponta a ponta | Não executado | Funcionalidade completa não confirmada nem refutada |
| Recálculo isolado da fixture TCL | Executado em Python 3.13.5; hashes coincidiram; código 0 | Verifica serialização/hash da fixture, não o pipeline inteiro |
| Repetição integral dos resultados dos autores | Não concluída | Reprodutibilidade integral permanece sem confirmação |
| Transcrições literais integrais das rodadas GPT-6 anteriores | Não preservadas | Os relatórios atuais não podem ser citados como transcrições |

## 4. O que ainda é necessário para encerrar a investigação

- [x] Executar a lógica de `verificar_hash_canonico_tcl.py` em Python 3.13.5 e guardar a saída bruta em `docs/tarefa8/SAIDA_TESTE_HASH_TCL.md`; ambos os hashes esperados coincidiram (código de saída 0). **Limite:** execução sobre a fixture do script, não sobre o módulo original do IoT-ID.
- [x] Obter clone do artefato em ambiente com DNS/rede funcional; registrar commit SHA exato. **Feito em 23/11/2026:** commit `167f48792858630020a408147ade001e5c977f78` (ver [verificação completa](VERIFICACAO_COMPLETA_ARTEFATO.md)).
- [x] Verificar comandos de ajuda/CLI e testes de canonicalização/hash que possam ser executados sem dispositivo IoT. **Feito em 23/11/2026:** `iot_id_fingerprint.py --help` (código 0); `fingerprint_hash.py` e o módulo original de canonicalização executados sobre as 22 execuções de `testes/`. Resultado: 9/22 reproduzem com `stable`, 6 (TCL) só com `rich`, 7 (Xiaomi e duas do IP `.100`) com nenhuma política.
- [ ] Executar o pipeline ponta a ponta somente em LAN autorizada, com permissões e dispositivo de teste disponíveis; preservar logs, PCAPs permitidos, versões e comandos.
- [ ] Identificar o commit do código que produziu a execução TCL de 24/03/2026 e comparar essa versão histórica com a atual. *(Parcial: o [adendo](ADENDO_HISTORICO_CANONICALIZACAO_TCL.md) explica o TCL; a [verificação completa](VERIFICACAO_COMPLETA_ARTEFATO.md) mostra o mesmo padrão temporal, com todas as execuções de 24/03 que têm mais campos que o TTL divergindo e todas as de 25/03 reproduzindo, mas o caso Xiaomi segue sem causa determinada.)*
- [ ] Para novas avaliações LLM, salvar prompt e resposta literal integral imediatamente, com data, modelo exibido e configuração selecionada.
- [ ] Se a pergunta de pesquisa continuar sendo sobre efeito do esforço de raciocínio, fazer comparação controlada com a mesma família/versão e o mesmo prompt, alterando apenas o esforço quando essa opção estiver disponível e identificável.
- [ ] Se não for possível controlar a versão ou o esforço, declarar a comparação como exploratória e não atribuir causalidade à configuração.
- [ ] Atualizar os resultados somente depois que os novos testes forem realmente executados.

## 5. Estado por critério D/F/S/R

- **D — Disponibilidade:** arquivos públicos acessíveis por integração; clone Git não funcionou no ambiente de execução por DNS.
- **F — Funcionalidade:** arquitetura e módulos inspecionados; pipeline completo não executado.
- **S — Sustentabilidade:** documentação e separação de módulos são sinais favoráveis; manutenção de longo prazo e testes em ambientes diversos não foram avaliados.
- **R — Reprodutibilidade:** existem registros e hashes de referência; a fixture stable/rich foi analisada isoladamente, mas a execução integral não foi reproduzida e a origem histórica da divergência não foi determinada.

## 6. Critério de encerramento

A Tarefa 8 pode ser considerada **documentalmente organizada e com o teste isolado da fixture executado, mas experimentalmente incompleta** até que a limitação do pipeline completo seja resolvida ou formalmente mantida como limitação. Se a disciplina exigir execução real do artefato, a tarefa não deve ser marcada como concluída antes dessa etapa.

Nenhum resultado ausente deve ser inventado, inferido a partir de outro LLM ou descrito como execução realizada.


## 7. Atualização de 20/10/2026 — histórico de canonicalização

- [x] Consultar o histórico Git de `canonicalize_features.py` no clone local.
- [x] Inspecionar a versão do commit `00f38c003de12c9140695baaac4039d12b48ddf7`, datado de 24/03/2026.
- [x] Inspecionar o diff de `f2b8930d3ac1bd91b08deee7b99a804bbc533521`, datado de 25/03/2026.
- [x] Confirmar que a versão anterior incluía os quatro campos Nmap disponíveis sem restringi-los pela política.
- [x] Confirmar que a alteração posterior passou a restringir `server` e `name` à política `rich` para IoT.
- [x] Documentar uma explicação provável para o registro histórico rotulado `stable` que contém os campos de `rich`.

**Limite mantido:** como o log não registra o SHA do commit executado, a versão exata que gerou a captura de 24/03 não está comprovada. O pipeline completo continua não executado; a tarefa permanece experimentalmente incompleta se a disciplina exigir execução ponta a ponta.

Detalhes: [Adendo histórico da canonicalização TCL](ADENDO_HISTORICO_CANONICALIZACAO_TCL.md).
