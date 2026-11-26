# Fluxograma — Tarefa 8

> Atualizado em 23/11/2026 com as configurações efetivamente executadas (T8-C-01/02, T8-GPT6-01/02/03), a verificação direta no artefato e as comparações por esforço, T7 × T8 e com os selos oficiais.

```mermaid
flowchart TD
    A["Artefato IoT-ID<br/>commit 167f487"] --> B["Selos oficiais SBRC 2026<br/>D, F, S, R"]
    A --> P["Prompt padronizado P1<br/>(igual à T7)"]

    subgraph T7["Tarefa 7 — linha de base"]
        P --> T7C["Claude"]
        P --> T7G["Grok"]
        P --> T7M["Gemini"]
    end

    subgraph T8["Tarefa 8 — variações controladas"]
        P --> C1["T8-C-01<br/>Claude Opus 5.5, esforço padrão"]
        P --> C2["T8-C-02<br/>Claude Opus 5.5, esforço máximo"]
        P --> G1["T8-GPT6-01 / 03<br/>ChatGPT, esforço padrão"]
        P --> G2["T8-GPT6-02<br/>ChatGPT, esforço alto"]
        X["Grok e Gemini<br/>não repetidos (decisão §11)"]
    end

    C1 & C2 & G1 & G2 --> AN["Avaliação analítica<br/>D/F/S/R + evidências D/C/A/E"]
    AN --> EX["Avaliação por execução<br/>clone, testbed, recomputação"]
    EX --> RAW["Salvar resposta literal<br/>e configuração"]

    A --> VER["Verificação direta no artefato<br/>clone + script (22 execuções)"]
    RAW --> CHK{"Cada evidência existe<br/>e está correta?"}
    VER --> CHK
    CHK --> CLS["Confirmada / Inexistente /<br/>Incorreta / Não verificável"]

    CLS --> CMP1["Esforço: C-01 × C-02<br/>GPT6 padrão × alto"]
    T7C --> CMP2
    CMP1 --> CMP2["T7 × T8 (Claude)"]
    CMP2 --> CMP3["Comparar com selos oficiais"]
    B --> CMP3
    CMP3 --> CONC["Conclusão:<br/>robustez e sensibilidade"]
```

## Explicação

1. A linha de base da Tarefa 7 é recuperada sem alterar os resultados originais.
2. Cada variante registra modelo, versão, esforço, prompt e data.
3. A avaliação analítica e a execução são registradas separadamente.
4. As evidências citadas são conferidas diretamente no repositório.
5. A comparação considera mudanças de decisão, qualidade das evidências e concordância com a execução.
6. A conclusão responde à robustez sem presumir que versões mais novas ou maior esforço sejam necessariamente melhores.
