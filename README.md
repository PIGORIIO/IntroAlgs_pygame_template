# Nome do Jogo

Intergalactic Race - Um conflito além do terrestre

## Integrantes do grupo

- Pedro Gregório Fernandes Pontes
- Igor Félix Flaviano
- Carlos Eduardo Farias de Oliveira

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo
 > O jogo consiste em controlar uma espaçonave, humana ou alienígena, enquanto o jogador enfrenta uma jornada repleta de desafios espaciais. Ao longo do percurso, será necessário desviar de meteoros e inimigos para sobreviver o maior tempo possível. A pontuação é baseada na distância percorrida antes que todas as três vidas disponíveis sejam perdidas. 

## Objetivo do jogador

> Percorrer a maior distância possível no espaço, evitando perigos e inimigos, pra conseguir desbloquear novos mapas e personagens

## Regras do jogo

- O jogador se movimenta usando as setas do teclado e solta uma habilidade com a tecla espaço.
- Colidir com um obstáculo, inimigo ou habilidades do inimigo reduz a quantidade de vidas.
- A partida termina quando o jogador perde todas as vidas.

## Controles

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: ativar a habilidade
- ESC: sair do jogo
- Enter: Esquivar na direção em que a seta está apontando.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
