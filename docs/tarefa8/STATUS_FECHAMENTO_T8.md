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
- [ ] Obter clone do artefato em ambiente com DNS/rede funcional; registrar commit SHA exato.
- [ ] Verificar comandos de ajuda/CLI e testes de canonicalização/hash que possam ser executados sem dispositivo IoT.
- [ ] Executar o pipeline ponta a ponta somente em LAN autorizada, com permissões e dispositivo de teste disponíveis; preservar logs, PCAPs permitidos, versões e comandos.
- [ ] Identificar o commit do código que produziu a execução TCL de 24/03/2026 e comparar essa versão histórica com a atual.
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
