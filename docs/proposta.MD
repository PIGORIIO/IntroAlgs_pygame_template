# Proposta Inicial do Jogo

A proposta principal é desenvolver um jogo inspirado em **Spacewar**, no qual o jogador enfrenta ondas de inimigos que avançam gradualmente em sua direção. À medida que se aproximam, essas ameaças intensificam a tensão da partida, criando uma atmosfera crescente de ansiedade e pressão constante sobre o jogador.


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

> Jogo de sobrevivência espacial com foco em movimentação e eliminação de inimigos

## 4. Descrição geral do jogo

- O que aparece na tela? 
>    + Na tela aparece a nave do jogador e inimigos vão aparecendo

- O que o jogador controla?
>    + O jogador controla uma espaçonave humana

- O que o jogador precisa fazer?
>    + Desviar de ataques inimigos e elimina-los

- Quais desafios aparecem durante a partida?
>    + Com o passar do tempo, os inimigos vão chando cada vez mais perto do jogador

## 5. Objetivo do jogador

> Eliminar inimigos, se manter vivo e percorrer a maior distancia possível pra desbloquear novas fases

## 6. Regras principais

Regras do grupo:

>- Regra 1: O jogador começa com 3 vidas e Cada colisão com obstáculo(disparo e inimigo) remove 1 vida.
>- Regra 2: O jogador Ganha/ desbloquea uma nova fase se conseguir fazer 125000 pontos
>- Regra 3: O jogador se movimenta usando as setas do teclado, solta uma habilidade com a tecla espaço.
>- Regra 4: A partida termina quando o jogador perde todas as vidas ou clica no botão sair da fase.

## 7. Condição de vitória

Condição de vitória:

> Alcançar a pontuação necessária para desbloquear novas fases.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> Perder todas as vidas antes de atingir a pontuação desejada.

## 9. Elementos previstos no jogo

**Personagens**: Espaçonave Humana
**Nave Espacial**: Controlada pelo jogador para se mover e escapar dos perigos.
**Inimigos**: Naves Alienigenas que perseguem o jogador e devem ser evitadas ou destruidas.
**Cenário Espacial**: Ambiente em que o jogo acontece, o espaço.
**Pontuação**: Aumenta conforme o jogador sobrevive.

## Jogador ou elemento principal

Descrição:

> Uma espaçonave humana controlada pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Descrição:

> Os inimigos aparecem em 5 em 5 fileiras

## Itens, alvos ou objetos de interação

Descrição:

> Naves inimigas

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador começa com 3 vidas e vai aumentando os pontos de 5 em 5 com o passar do tempo em que continua vivo.

## 10. Controles previstos

- Tecla/comando: Seta para esquerda: mover para esquerda
- Tecla/comando: Seta para direita: mover para direita
- Tecla/comando: Espaço: soltar a habilidade especial
- Botão: X: sair do jogo

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

>- 2. Detectar colisões: Saber quando um tiro ou inimigo atinge a nave do jogador e diminuir as vidas.

>- 3. Sistema de habilidades especiais e esquiva: Saber cronometrar o tempo em que poderá e não poderá disparar.

>- 4. Loop principal do jogo: Entender o ciclo do jogo muito bem

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Tela inicial;
- Melhoria 2: diferentes personagens;
- Melhoria 3: menu de pausa.
- Melhoria 4: fases;
- Melhoria 5: aumento de dificuldade;
- Melhoria 6: Sons;
- Melhoria 7: Ranking;
