# Evidências de Reprodutibilidade

## 1. Motivação

A reprodutibilidade foi o ponto de maior divergência entre as avaliações. Por isso, foi realizada análise específica dos registros disponíveis no diretório testes do artefato.

O objetivo foi investigar se os resultados poderiam ser reconstruídos utilizando código, dados e configurações disponíveis.

## 2. TCL Smart TV Pro

Foram analisadas seis execuções do dispositivo TCL Smart TV Pro. Todas apresentavam o mesmo hash:

    e20c48257b98e86fa11d7c4444e7e5da7176a1b328719ea5f46f831951392d51

A repetição demonstra consistência interna entre os registros fornecidos pelos autores.

Entretanto, a reconstrução realizada por Claude utilizando a política stable produziu um hash diferente. O hash armazenado pôde ser reproduzido quando utilizada a política rich.

Isso criou uma divergência entre a política registrada, o resultado armazenado e a política necessária para reconstrução.

## 3. Outros dispositivos

A análise também identificou divergências em registros associados a dispositivos Xiaomi e a determinadas execuções de câmera IP.

No caso Xiaomi, o resultado armazenado não foi reproduzido diretamente utilizando a implementação atual e os dados disponíveis.

No caso de IP Camera Model B, alguns hashes puderam ser associados aos dados disponíveis, enquanto outros registros apresentaram variações.

## 4. Interpretação

A existência de hashes iguais em várias execuções é evidência de consistência dos resultados registrados pelos autores. Entretanto, consistência dos registros não é equivalente à reprodução independente.

Para demonstrar reprodução independente é necessário utilizar a implementação disponível, configurações indicadas, dados disponíveis, executar o procedimento e obter o mesmo resultado.

A divergência encontrada na TCL Smart TV Pro mostra que esses passos precisam ser verificados separadamente.

## 5. Tabela

| Dispositivo | Evidência registrada | Reconstrução | Interpretação |
|---|---|---|---|
| TCL Smart TV Pro | e20c4825... | stable → diferente | Divergência |
| TCL Smart TV Pro | e20c4825... | rich → igual | Compatível com configuração alternativa |
| Samsung | 1f4e8c4a... | Reproduzido nos testes analisados | Reprodução observada |
| Xiaomi | 6397f472... | Diferente na reconstrução atual | Divergência |
| IP Camera Model B | 5b60133e... | Compatibilidade parcial | Reprodução parcial |

## 6. Implicação

O achado principal não é afirmar que o artefato é ou não é reprodutível de forma absoluta. O achado é que alguns resultados históricos armazenados no repositório não são diretamente reconstruídos pela configuração atualmente indicada. Esse resultado explica a diferença entre as avaliações de Claude e Grok sem exigir que uma das duas seja considerada simplesmente errada.
