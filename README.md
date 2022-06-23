# FUTOSHIKI

    A ideia do jogo é preencher o tabuleiro de forma que mesmo número não pode ser repetido na mesma coluna e linha
    Alguns números podem vir preenchidos já nas células e para dificultar as jogadas,algumas células podem ter restrições como: ">","V", as quais definem os números possíveis jogadas
    Para resolver o puzzle, foram implementados dois algoritmos: Backtracking e o Local Beam Search

## BACKTRACKING

O grafo é montado a partir dos números que podem ser jogados em uma determinada celula, o mesmo serve para seus nós adjacentes(vizinhos). Como existem restrições numéricas para as células, para cada nó devem ser verificadas as restrições de jogadas para não adicionar nós que não levam a uma jogada válida no grafo.
Com este algoritmo foi realizada uma simulação com 20 tabuleiros com diferentes tamanhos e restrições. Como o algoritmo é exato, foi implementado um limite de 15 segundos para a tomada de decisão, caso este limite seja atingido, o tabuleiro do nó atual do grafo é retornado. Para cada tabuleiro retornado pelo gráfico, seja ele vencedor ou não, é contabilizada a quantidade de restrições violadas

| Tabuleiro  |  Restrições violadas  |
| ------------------- | ------------------- |
|   easy 4x4    |  0 |
|   extreme 4x4 |  0 |
|   extreme 4x4 alternativa jogo 2 |  0 |
|   4x4 |  0 |
|   4x4 extreme |  0 |
|   4x4 extreme |  0 |
|   easy 5x5 |  0 |
|   extreme 5x5  |  0 |
|   trivial 5x5 |  0 |
|   extreme 6x6 |  0 |
|   trivial 6x6 |  0 |
|   easy 6x6  |  6.23 |
|   tricky 6x6 (jogo 8) |  3.16 |
|   extreme 6x6 |  5.56 |
|   trivial 7x7 |  2.53 |
|   extreme 7x7  |  10.8 |
|   easy 7x7  |  5.93 |
|   tricky 7x7  |  10.86 |
|   easy 8x8  |  18.9 |
|   extreme 9x9 |  6.2 |


## LOCAL BEAM SEARCH COM K=4
Como o algoritmo de backtrackin é exato, não é suficiente para tabuleiros muito grandes, neste caso, acima de 6 dimensões. Foi necessário então implementar o algoritmo de Local Beam Search. Este algoritmo é baseado em número de K, este K é o número de instãncias que serão utilizadas para tentar achar uma solução que minimize o número de restrições violadas. O algoritmo consiste em: para ca K, inicialmente é gerada uma solução aleatória e a partir dela gerada seus vizinhos. Destes vizinhos, são escolhidos os K melhores dentro todos os vizinhos e o processo de repete até o ponto de parada. O ponto de parada foi estabelecido em 15 segundos. 

| Tabuleiro  |  Restrições violadas  |
| ------------------- | ------------------- |
|   easy 4x4    | 1.23 |
|   extreme 4x4 | 1.29 |
|   extreme 4x4 alternativa jogo 2 | 2.41 |
|   4x4 | 1.97 |
|   4x4 extreme | 4 |
|   4x4 extreme | 2.15 |
|   easy 5x5  | 2.8 |
|   extreme 5x5  | 4.87 |
|   trivial 5x5 | 3.42 |
|   extreme 6x6 | 8.23 |
|   trivial 6x6 | 6 |
|   easy 6x6  | 8.8 |
|   tricky 6x6  | 5.12 |
|   extreme 6x6 | 4.6 |
|   trivial 7x7 | 9.4 |
|   extreme 7x7 | 11.2 |
|   easy 7x7  | 14.23 |
|   tricky 7x7 | 18.4 |
|   easy 8x8  | 60.6 |
|   extreme 9x9 | 64.49 |

## LOCAL BEAM SEARCH COM K=8

| Tabuleiro  |  Restrições violadas  |
| ------------------- | ------------------- |
|   easy 4x4  | 2.2  |
|   extreme 4x4  | 2.3  |
|   extreme 4x4 alternativa jogo 2  | 0  |
|   4x4  | 2.2  |
|   4x4 extreme  | 2.06  |
|   4x4 extreme  | 1.6  |
|   easy 5x5  | 2.9  |
|   extreme 5x5  | 2.83  |
|   trivial 5x5  | 0.6  |
|   extreme 6x6  | 10.53  |
|   trivial 6x6  | 8.6  |
|   easy 6x6  | 30.6  |
|   tricky 6x6  | 20.13  |
|   extreme 6x6  | 19.1  |
|   trivial 7x7  | 35.73  |
|   extreme 7x7  | 52.9  |
|   easy 7x7  | 61.83  |
|   tricky 7x7  | 72.06  |
|   easy 8x8  | 112.8  |
|   extreme 9x9  | 98.66  |


Os algoritmos que utilizam o Local Beam Search tentem a ficar presos em um máximo local, logo não encontram a solução ótima. Para tentar solucionar o problema poderia ser implementado uma estratégia de random restart para escapar do local atual 
