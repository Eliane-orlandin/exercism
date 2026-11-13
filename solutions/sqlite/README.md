# SQLite

Soluções da trilha de SQLite, seguindo o mesmo padrão das demais trilhas.

## Estrutura

```
solutions/sqlite/
└── <slug>/
    └── <iteracao>/
        └── <slug>.sql
```

Exemplo:

```
solutions/sqlite/hello-world/1/hello-world.sql
```

Convenções:

- O diretório `<iteracao>` é criado pelo `exercism-sync` a cada envio. Envios
  antigos não são editados; uma correção gera uma nova iteração.
- O arquivo `.sql` contém apenas a solução. O esquema (`bootstrap.sql`), os
  testes e o restante do exercício são gerenciados pelo Exercism e não são
  versionados aqui.
- Pastas usam o _slug_ oficial em `kebab-case`; o arquivo recebe o mesmo nome,
  por exemplo `hello-world/1/hello-world.sql`.

## Executar localmente

O esquema de cada exercício vem junto com o download feito pelo CLI do Exercism.
Com o exercício baixado, aplique o esquema e depois a solução:

```bash
sqlite3 exercicio.db < bootstrap.sql
sqlite3 exercicio.db < ../exercism/solutions/sqlite/<slug>/<iteracao>/<slug>.sql
```

Para uma verificação rápida de sintaxe sem esquema, use um banco em memória:

```bash
sqlite3 :memory: < solutions/sqlite/hello-world/1/hello-world.sql
```
