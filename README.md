# FUTOSHIKI

A ideia do jogo é preencher o tabuleiro de forma que mesmo número não pode ser repetido na mesma coluna e linha
    Alguns números podem vir preenchidos já nas células e para dificultar as jogadas,algumas células podem ter restrições como: ">","V", as quais definem os números possíveis jogadas
    Para resolver o puzzle, foram implementados dois algoritmos: Backtracking e o Local Beam Search

## BACKTRACKING

O grafo é montado a partir dos números que podem ser jogados em uma determinada celula, o mesmo serve para seus nós adjacentes(vizinhos). Como existem restrições numéricas para as células, para cada nó devem ser verificadas as restrições de jogadas para não adicionar nós que não levam a uma jogada válida no grafo.
Com este algoritmo foi realizada uma simulação com 20 tabuleiros com diferentes tamanhos e restrições. Como o algoritmo é exato, foi implementado um limite de 15 segundos para a tomada de decisão, caso este limite seja atingido, o tabuleiro do nó atual do grafo é retornado. Para cada tabuleiro retornado pelo gráfico, seja ele vencedor ou não, é contabilizada a quantidade de restrições violadas

| Tabuleiro  |  Restrições violadas  |
| ------------------- | ------------------- |
|   Easy 4x4    |  0 |
|   Extreme 4x4 |  0 |
|   Extreme 4x4 alternativa jogo 2 |  0 |
|   Extreme 4x4 |  0 |
|   Extreme 4x4  |  0 |
|   Extreme 4x4  |  0 |
|   Easy 5x5 |  0 |
|   Extreme 5x5  |  0 |
|   Trivial 5x5 |  0 |
|   Extreme 6x6 |  0 |
|   Trivial 6x6 |  0 |
|   Easy 6x6  |  6.23 |
|   Tricky 6x6 |  3.16 |
|   Extreme 6x6 |  5.56 |
|   Trivial 7x7 |  2.53 |
|   Extreme 7x7  |  10.8 |
|   Easy 7x7  |  5.93 |
|   Tricky 7x7  |  10.86 |
|   Easy 8x8  |  18.9 |
|   Extreme 9x9 |  6.2 |


## LOCAL BEAM SEARCH COM K=4
Como o algoritmo de backtrackin é exato, não é suficiente para tabuleiros muito grandes, neste caso, acima de 6 dimensões. Foi necessário então implementar o algoritmo de Local Beam Search. Este algoritmo é baseado em número de K, este K é o número de instãncias que serão utilizadas para tentar achar uma solução que minimize o número de restrições violadas. O algoritmo consiste em: para ca K, inicialmente é gerada uma solução aleatória e a partir dela gerada seus vizinhos. Destes vizinhos, são escolhidos os K melhores dentro todos os vizinhos e o processo de repete até o ponto de parada. O ponto de parada foi estabelecido em 15 segundos. 

| Tabuleiro  |  Restrições violadas  |
| ------------------- | ------------------- |
|   Easy 4x4    | 1.23 |
|   Extreme 4x4 | 1.29 |
|   Extreme 4x4 alternativa jogo 2 | 2.41 |
|   Extreme 4x4 | 1.97 |
|   Extreme 4x4  | 4 |
|   Extreme 4x4  | 2.15 |
|   Easy 5x5  | 2.8 |
|   Extreme 5x5  | 4.87 |
|   Trivial 5x5 | 3.42 |
|   Extreme 6x6 | 8.23 |
|   Trivial 6x6 | 6 |
|   Easy 6x6  | 8.8 |
|   Tricky 6x6  | 5.12 |
|   Extreme 6x6 | 4.6 |
|   Trivial 7x7 | 9.4 |
|   Extreme 7x7 | 11.2 |
|   Easy 7x7  | 14.23 |
|   Tricky 7x7 | 18.4 |
|   Easy 8x8  | 60.6 |
|   Extreme 9x9 | 64.49 |

## LOCAL BEAM SEARCH COM K=8

| Tabuleiro  |  Restrições violadas  |
| ------------------- | ------------------- |
|   Easy 4x4  | 2.2  |
|   Extreme 4x4  | 2.3  |
|   Extreme 4x4 alternativa jogo 2  | 0  |
|   Extreme 4x4  | 2.2  |
|   Extreme 4x4   | 2.06  |
|   Extreme 4x4   | 1.6  |
|   Easy 5x5  | 2.9  |
|   Extreme 5x5  | 2.83  |
|   Trivial 5x5  | 0.6  |
|   Extreme 6x6  | 10.53  |
|   Trivial 6x6  | 8.6  |
|   Easy 6x6  | 30.6  |
|   Tricky 6x6  | 20.13  |
|   Extreme 6x6  | 19.1  |
|   Trivial 7x7  | 35.73  |
|   Extreme 7x7  | 52.9  |
|   Easy 7x7  | 61.83  |
|   Tricky 7x7  | 72.06  |
|   Easy 8x8  | 112.8  |
|   Extreme 9x9  | 98.66  |


Os algoritmos que utilizam o Local Beam Search tentem a ficar presos em um máximo local, logo não encontram a solução ótima. Para tentar solucionar o problema poderia ser implementado uma estratégia de random restart para escapar do local atual 

#Instruções de execução
Não há nenhuma biblioteca terceira a ser instalada, é necessário apenas executar o arquivo main.py