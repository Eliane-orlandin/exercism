# Exercism

Soluções dos exercícios da trilha do [Exercism](https://exercism.org), organizadas
por linguagem e pelo _slug_ oficial de cada exercício.

Este repositório contém apenas as soluções. Os enunciados, testes e arquivos de
configuração de cada exercício continuam sendo gerenciados pelo CLI do Exercism.

## Estrutura

```
.
├── solutions/
│   ├── java/
│   │   └── <slug>/
│   │       └── <iteracao>/          # enviada pelo exercism-sync
│   │           └── src/main/java/…
│   ├── python/
│   │   └── <slug>/
│   │       └── <modulo>.py          # uma solução por exercício
│   └── sqlite/
│       └── <slug>/
│           └── <iteracao>/          # enviada pelo exercism-sync
│               └── <slug>.sql
├── .editorconfig
├── .gitignore
└── README.md
```

Convenções:

- `solutions/` é o diretório monitorado pelo `exercism-sync`; cada envio gera
  `solutions/<trilha>/<slug>/<iteracao>/`.
- As soluções Python seguem o mesmo esquema por trilha e _slug_, com o arquivo
  nomeado em `snake_case` (por exemplo, `solutions/python/hello-world/hello_world.py`).
- Diretórios usam `kebab-case`, seguindo os _slugs_ do Exercism; arquivos Python
  usam `snake_case`, arquivos Java usam `PascalCase` e os arquivos SQL levam o
  mesmo slug do exercício.
- Cada solução é independente: sem dependências externas e sem imports entre
  exercícios.

## Exercícios

### Python

| Exercício | Caminho |
| --- | --- |
| Blackjack | [`solutions/python/blackjack/blackjack.py`](solutions/python/blackjack/blackjack.py) |
| Card Games | [`solutions/python/card-games/card_games.py`](solutions/python/card-games/card_games.py) |
| Chaitana's Colossal Coaster | [`solutions/python/chaitanas-colossal-coaster/chaitanas_colossal_coaster.py`](solutions/python/chaitanas-colossal-coaster/chaitanas_colossal_coaster.py) |
| Currency Exchange | [`solutions/python/currency-exchange/currency_exchange.py`](solutions/python/currency-exchange/currency_exchange.py) |
| Ghost Gobble Arcade Game | [`solutions/python/ghost-gobble-arcade-game/ghost_gobble_arcade_game.py`](solutions/python/ghost-gobble-arcade-game/ghost_gobble_arcade_game.py) |
| Hello World | [`solutions/python/hello-world/hello_world.py`](solutions/python/hello-world/hello_world.py) |
| Lasagna | [`solutions/python/lasagna/lasagna.py`](solutions/python/lasagna/lasagna.py) |
| Little Sister's Essay | [`solutions/python/little-sisters-essay/little_sisters_essay.py`](solutions/python/little-sisters-essay/little_sisters_essay.py) |
| Little Sister's Vocabulary | [`solutions/python/little-sisters-vocabulary/little_sisters_vocabulary.py`](solutions/python/little-sisters-vocabulary/little_sisters_vocabulary.py) |
| Making the Grade | [`solutions/python/making-the-grade/making_the_grade.py`](solutions/python/making-the-grade/making_the_grade.py) |
| Meltdown Mitigation | [`solutions/python/meltdown-mitigation/meltdown_mitigation.py`](solutions/python/meltdown-mitigation/meltdown_mitigation.py) |

### Java

| Exercício | Caminho |
| --- | --- |
| Annalyn's Infiltration | [`solutions/java/annalyns-infiltration/1`](solutions/java/annalyns-infiltration/1) |
| Hello World | [`solutions/java/hello-world/1`](solutions/java/hello-world/1) |
| Lasagna | [`solutions/java/lasagna/1`](solutions/java/lasagna/1) |

### SQLite

A trilha está preparada em [`solutions/sqlite/`](solutions/sqlite/README.md).
Nenhuma solução registrada ainda — as próximas ficam em
`solutions/sqlite/<slug>/<iteracao>/<slug>.sql`.

## Como executar

### Python 3

```bash
python3 solutions/python/hello-world/hello_world.py
```

Para verificar a sintaxe de todas as soluções:

```bash
python3 -m compileall -q solutions/python
```

### Java 17+

Cada solução Java é um arquivo autocontido, sem dependências:

```bash
javac solutions/java/lasagna/1/src/main/java/Lasagna.java
```

### SQLite 3

Aplicar uma solução a um banco já inicializado com o esquema do exercício:

```bash
sqlite3 exercicio.db < solutions/sqlite/<slug>/<iteracao>/<slug>.sql
```

Detalhes da trilha em [`solutions/sqlite/README.md`](solutions/sqlite/README.md).
