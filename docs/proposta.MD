# Proposta Inicial do Jogo

A ideia principal é criar um jogo no estilo **Spacewar**, mas em vez de enfrentar e destruir inimigos, o objetivo do jogador será **desviar e escapar** de ameaças como naves inimigas, meteoros e asteroides. Para sobreviver, o jogador poderá utilizar manobras de esquiva e, dependendo do personagem escolhido — seja humano ou alienígena — terá acesso a uma habilidade exclusiva que oferece diferentes vantagens durante o jogo.

## 1. Nome provisório do jogo

Intergalactic Race - Um conflito além do terrestre

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Pedro Gregório Fernandes Pontes
- Nome 2: Igor Félix Flaviano
- Nome 3: Carlos Eduardo Farias de Oliveira
- Nome 4: .....

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo de sobrevivência espacial com foco em movimentação, esquiva e progressão por pontuação.

## 4. Descrição geral do jogo

- O que aparece na tela? 
>    + Na tela aparece a nave escolhida pelo jogador, depois de um tempo meteoros e inimigos vão aparecendo

- O que o jogador controla?
>    + O jogador controla uma espaçonave, podendo ser uma humana ou uma alienigena

- O que o jogador precisa fazer?
>    + Desviar de meteoros e ataques inimigos

- Quais desafios aparecem durante a partida?
>    + Com o passar do tempo, vai aumentando a quantidade de inimigos e meteoros para desviar

## 5. Objetivo do jogador

> Percorrer a maior distância possível no espaço, evitando perigos e inimigos, pra conseguir desbloquear novos mapas e personagens.

## 6. Regras principais

Regras do grupo:

>- Regra 1: O jogador começa com 3 vidas e Cada colisão com obstáculo(meteoro, asteroide e inimigo) remove 1 vida.
>- Regra 2: O jogador Ganha/ desbloquea uma nova fase se conseguir fazer 125000 pontos
>- Regra 3: O jogador se movimenta usando as setas do teclado, solta uma habilidade com a tecla espaço e esquiva com Enter.
>- Regra 4: A partida termina quando o jogador perde todas as vidas ou clica no botão sair da fase.

## 7. Condição de vitória

Condição de vitória:

> Alcançar a pontuação necessária para desbloquear novas fases e conteúdos.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> Perder todas as vidas antes de atingir a pontuação desejada.

## 9. Elementos previstos no jogo

**Personagens**: Humanos e alienígenas com habilidades especiais únicas.
**Nave Espacial**: Controlada pelo jogador para se mover e escapar dos perigos.
**Inimigos**: Naves que perseguem o jogador e devem ser evitadas.
**Meteoros e Asteroides**: Obstáculos espalhados pelo cenário que podem causar colisões.
**Esquiva**: Movimento rápido que ajuda o jogador a escapar de ameaças.
**Cenário Espacial**: Ambiente onde o jogo acontece, com estrelas, planetas e campos de asteroides.
**Pontuação**: Aumenta conforme o jogador sobrevive e coleta itens.

## Jogador ou elemento principal

Descrição:

> Uma espaçonave humana ou alienigena controlado pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Descrição:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

## Itens, alvos ou objetos de interação

Descrição:

> Meteoros, asteroides e naves inimigas

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador começa com 3 vidas e vai aumentando os pontos de 5 em 5 com o passar do tempo.

## 10. Controles previstos

- Tecla/comando: Seta para cima: mover para cima
- Tecla/comando: Seta para baixo: mover para baixo
- Tecla/comando: Seta para esquerda: mover para esquerda
- Tecla/comando: Seta para direita: mover para direita
- Tecla/comando: Espaço: soltar a habilidade especial
- Tecla/comando: ESC: sair do jogo

## 11. Organização inicial do código

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.


## 12. Recursos externos previstos

> imagens obtidas de banco gratuito;
> sons gratuitos;
> tutorial usado apenas como referência;
> fonte personalizada.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

>- 1. Fazer os objetos se moverem corretamente : Em um Spacewar, a nave normalmente possui inércia, então ela continua se movendo mesmo sem o jogador pressionar uma tecla.

>- 2. Detectar colisões: Saber quando um tiro, asteroide, meteoro ou inimigo atinge a nave do jogador e diminuir as vidas.

>- 3. Sistema de habilidades especiais e esquiva: Saber cronometrar o tempo em que poderá e não poderá usar a habilidade, contando que cada personagem/espaçonave terá sua própria peculiaridade e esquivas.

>- 4. Loop principal do jogo: Entender o ciclo do jogo muito bem

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: ranking;
- Melhoria 2: diferentes personagens;
- Melhoria 3: menu de pausa.
- Melhoria 4: fases;
- Melhoria 5: aumento de dificuldade;
- Melhoria 6: Sons;
