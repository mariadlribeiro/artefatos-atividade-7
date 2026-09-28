# Fluxograma do processo

## Fluxo geral

    [Selecionar artefato IoT-ID]
                 |
                 v
    [Identificar critérios D/F/S/R]
                 |
                 v
       [Prompt padronizado]
                 |
                 v
        [Aplicar aos LLMs]
          /       |       \
         v        v        v
     [Claude]   [Grok]   [Gemini]
         |        |        |
     análise   análise   análise
      + exec.   + exec.  + tentativa
         \        |        /
          \       |       /
           v      v      v
       [Registrar evidências]
                 |
                 v
       [Classificar D/C/A/E]
                 |
                 v
       [Comparar LLM x LLM]
                 |
                 v
     [Análise x execução]
                 |
                 v
     [Comparar com oficial]
                 |
                 v
       [Convergências e
        divergências]
                 |
                 v
            [Discussão]
                 |
                 v
           [Conclusão]

## Legenda

- D: documentação;
- C: código;
- A: evidência dos autores;
- E: execução independente.

O fluxo separa explicitamente análise e execução porque uma conclusão documental não equivale a uma confirmação experimental.
