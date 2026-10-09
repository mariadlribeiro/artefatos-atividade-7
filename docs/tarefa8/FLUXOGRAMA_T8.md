# Fluxograma — Tarefa 8

```mermaid
flowchart TD
    A["Recuperar artefato e resultados T7"] --> B["Confirmar prompt, modelos e critérios oficiais"]
    B --> C["Registrar identificadores e configurações"]
    C --> D["Selecionar variante controlada"]
    D --> E["Avaliação analítica: D, F, S e R"]
    D --> F["Execução independente, quando viável"]
    E --> G["Guardar resposta integral e verificar evidências"]
    F --> H["Guardar comandos, ambiente e resultados observados"]
    G --> I["Comparar T7 × T8"]
    H --> I
    I --> J["Comparar com os selos oficiais"]
    J --> K["Classificar estabilidade, mudança ou inconclusão"]
    K --> L["Discutir robustez e limitações"]
```

## Explicação

1. A linha de base da Tarefa 7 é recuperada sem alterar os resultados originais.
2. Cada variante registra modelo, versão, esforço, prompt e data.
3. A avaliação analítica e a execução são registradas separadamente.
4. As evidências citadas são conferidas diretamente no repositório.
5. A comparação considera mudanças de decisão, qualidade das evidências e concordância com a execução.
6. A conclusão responde à robustez sem presumir que versões mais novas ou maior esforço sejam necessariamente melhores.
