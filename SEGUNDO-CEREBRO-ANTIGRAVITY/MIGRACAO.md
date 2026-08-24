# Notas de Migração: Claude Code -> Google Antigravity

Esta versão foi produzida a partir do ZIP original sem alterar a lógica central de memória.

## Mapeamento

- `CLAUDE.md` -> `.agents/rules/segundo-cerebro.md`
- `.claude/commands/*.md` -> `.agents/workflows/*.md`
- `$ARGUMENTS` -> entrada/contexto fornecido junto ao slash command
- `_memory`, `_knowledge`, `_decisions`, `_learnings`, `_sessions`, `_pipeline` -> preservados

## Alterações adicionais

- Adicionado frontmatter `description` aos workflows.
- Referências internas a Claude Code foram portadas para Antigravity nos arquivos ativos.
- Criado guia de instalação específico para Antigravity.
- Criada cópia de legado do `CLAUDE.md` e `.claude/commands/` para auditoria e reversibilidade.
- A Rule ativa foi mantida abaixo do limite de 12.000 caracteres.
- Cada Workflow ativo também foi validado abaixo de 12.000 caracteres.

## Arquivos de legado

Não mova `_legacy-claude-original/.claude` de volta para a raiz a menos que queira usar o kit antigo com Claude Code. O Antigravity deve operar exclusivamente sobre `.agents/`.
