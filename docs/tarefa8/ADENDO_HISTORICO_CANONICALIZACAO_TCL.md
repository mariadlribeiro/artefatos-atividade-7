# Adendo de rastreabilidade — canonicalização da TV TCL

**Data da atualização:** 20/10/2026  
**Repositório analisado:** https://github.com/GT-IoTEdu/sbrc26_fingerprint  
**Execução histórica:** `testes/192.168.59.106_20260324_220537/`  
**Escopo:** inspeção de histórico Git e comparação das regras de canonicalização; não é execução ponta a ponta do pipeline.

## 1. Evidências coletadas

Na cópia local do artefato, a responsável executou:

```powershell
git log --oneline --all -- .\canonicalize_features.py
git log -p -5 -- .\canonicalize_features.py
```

O histórico inclui:

- `00f38c003de12c9140695baaac4039d12b48ddf7` — “Update canonicalize_features.py”, datado de 24/03/2026;
- `f2b8930d3ac1bd91b08deee7b99a804bbc533521` — “fingerprint_iot_update”, datado de 25/03/2026.

A inspeção do arquivo `canonicalize_features.py` no commit `00f38c0` mostrou que os campos `server`, `name`, `manufacturer` e `model_name` eram normalizados e adicionados a `nmap_canon` quando disponíveis, sem condicionar a inclusão desses campos à política `stable` ou `rich`.

O diff de `f2b8930` introduziu a resolução de `host_kind` e alterou a regra para dispositivos IoT: `manufacturer` e `model_name` são incluídos em `stable`; `server` e `name` são incluídos somente quando a política é `rich`.

A inspeção local do JSON histórico confirmou estes campos na seção Nmap:

- `manufacturer`: `TCL`
- `model_name`: `Smart TV Pro`
- `name`: `Smart TV Pro`
- `server`: `UPnP/1.0, DLNADOC/1.50 Platinum/1.0.5.13`
- `report_for`: `192.168.59.106`

O log de 24/03/2026 declara `canon_policy=stable`, mas registra uma representação canônica de 277 caracteres contendo `name` e `server`, com SHA-256 `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51`.

## 2. Comparação dos resultados

| Evidência | Política/regra | Tamanho | SHA-256 |
|---|---|---:|---|
| Código atual executado localmente | `stable` | 203 | `3ce29174f6c15f666c6096b10ed456dc224910ed321fbe9c6086daaa7d6f2961` |
| Código atual executado localmente | `rich` | 277 | `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51` |
| Log histórico de 24/03/2026 | Rotulado `stable`, mas inclui `name` e `server` | 277 | `e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51` |

## 3. Interpretação

A evolução do código entre os commits de 24 e 25 de março é **uma explicação provável, apoiada pelo histórico Git**, para a divergência entre a política declarada no log histórico e os campos da representação canônica. O código anterior incluía os quatro campos disponíveis; a alteração posterior introduziu a distinção atual entre `stable` e `rich`.

Não é possível afirmar qual commit exato produziu a execução histórica, porque o log não registra o SHA do commit utilizado. A data dos commits e a compatibilidade do comportamento sustentam a hipótese, mas não provam a versão efetivamente executada.

## 4. Efeito sobre a avaliação D/F/S/R

- **D — Disponibilidade:** esta análise não altera a conclusão de que os arquivos públicos foram acessíveis.
- **F — Funcionalidade:** não foi executado novamente o pipeline completo; esta evidência não comprova funcionalidade ponta a ponta.
- **S — Sustentabilidade:** a mudança de regra entre versões reforça a importância de versionar e documentar as políticas de canonicalização.
- **R — Reprodutibilidade:** a divergência foi reproduzida no cálculo isolado da fixture e agora tem uma explicação provável apoiada pelo histórico de código. A reprodução integral do pipeline continua sem confirmação.

## 5. Conclusão e pendências

**Conclusão:** há evidência de que a implementação da canonicalização mudou entre os commits de 24 e 25/03/2026, de forma compatível com a divergência observada no fingerprint da TV TCL. O hash histórico corresponde à representação rica na versão atual, embora o log o rotule como `stable`.

**Ainda pendente:** identificar o SHA exato do código executado em 24/03/2026 ou obter outra evidência que permita vinculá-lo a uma versão específica. A execução completa do pipeline em uma LAN autorizada também permanece pendente.

Esta constatação deve ser descrita como uma divergência de rastreabilidade/versionamento com explicação provável, e não como prova isolada de falha geral do IoT-ID.
