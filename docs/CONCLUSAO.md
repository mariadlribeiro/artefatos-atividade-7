# Conclusão

Este trabalho realizou uma avaliação comparativa do artefato IoT-ID utilizando três modelos de linguagem de diferentes provedores: Claude, Grok e Gemini. Foram considerados os critérios de Disponibilidade, Funcionalidade, Sustentabilidade e Reprodutibilidade utilizados no processo de avaliação de artefatos do SBRC.

O procedimento utilizou um prompt padronizado e distinguiu avaliação analítica de execução independente. Também foram classificadas as evidências em documentação, código, evidências dos autores e execução.

Os resultados demonstraram que o uso de um mesmo prompt não produz necessariamente conclusões idênticas. Claude e Grok apresentaram resultados próximos em disponibilidade e funcionalidade, mas divergiram principalmente em reprodutibilidade. Gemini não conseguiu acessar o repositório em seu ambiente, mostrando que a capacidade de avaliação também depende das condições de acesso e execução.

O principal achado foi a diferença entre consistência dos resultados fornecidos pelos autores e reprodução independente. No caso da TCL Smart TV Pro, seis registros apresentaram o mesmo hash, mas a reconstrução utilizando a política stable indicada nos registros produziu valor diferente. O hash armazenado pôde ser reproduzido utilizando a política rich. Também foram observadas divergências em outros registros.

Esse resultado não permite afirmar que a avaliação oficial esteja incorreta. O artefato recebeu oficialmente os quatro selos no SBRC 2026, enquanto a avaliação deste estudo foi posterior e utilizou a versão pública disponível e diferentes condições de execução. A análise dos LLMs acrescenta uma perspectiva de verificação independente e mais detalhada.

O estudo mostra que LLMs podem apoiar a avaliação de artefatos científicos, especialmente na organização de evidências, inspeção documental, análise de código e execução de procedimentos. Entretanto, as conclusões devem estar vinculadas às evidências efetivamente observadas e às limitações do ambiente.

Como trabalho futuro, recomenda-se repetir o procedimento com mais artefatos, diferentes categorias de software e ambientes controlados, além de comparar avaliações exclusivamente documentais com avaliações que permitam execução completa.

Em síntese, o experimento mostrou convergência parcial entre os modelos e entre as avaliações dos modelos e os selos oficiais. As maiores diferenças apareceram quando a avaliação exigiu execução e reprodução de resultados, demonstrando a importância da evidência experimental na avaliação de artefatos científicos.
