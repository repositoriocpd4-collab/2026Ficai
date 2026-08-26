# START HERE - Segundo Cérebro para Google Antigravity

Você está com a versão convertida do Kit Segundo Cérebro para o Google Antigravity. A memória continua baseada em arquivos Markdown, compatível com Obsidian; a camada de execução foi migrada de Claude Code para Rules e Workflows nativos do Antigravity.

## O que mudou

| Antes | Agora |
|---|---|
| `CLAUDE.md` | `.agents/rules/segundo-cerebro.md` |
| `.claude/commands/*.md` | `.agents/workflows/*.md` |
| `$ARGUMENTS` | contexto informado junto ao slash command |
| Claude Code | Google Antigravity |
| Pastas de memória | permanecem iguais |

## Instalação rápida

1. Descompacte `SEGUNDO-CEREBRO-ANTIGRAVITY` em uma pasta permanente.
2. Abra essa pasta como workspace no Google Antigravity, ou adicione-a ao Project que você usa para trabalhar.
3. Confirme que o Antigravity reconheceu `.agents/rules/segundo-cerebro.md` como regra de workspace. Se a interface exibir opções de ativação, use **Always On**.
4. No Agent, digite `/` e confirme que aparecem os workflows: `daily-briefing`, `end-session`, `braindump`, `weekly-review`, `content-idea`, `prospect-research`, `pipeline` e `proposal-generator`.
5. Abra a mesma pasta como vault no Obsidian se quiser uma interface humana para consultar e editar a memória.
6. Personalize `_knowledge/about-me.md`, `_knowledge/goals.md`, `_knowledge/projects.md` e os campos de identidade da regra.
7. Teste com `/daily-briefing`.

## Fluxo recomendado

- Início do dia ou sessão: `/daily-briefing`
- Captura rápida de pensamentos: `/braindump`
- Fechamento de uma sessão produtiva: `/end-session`
- Revisão semanal: `/weekly-review`

O `/end-session` é especialmente importante: ele deve atualizar `_memory/current-state.md` e persistir decisões/aprendizados relevantes para que uma nova conversa consiga retomar o contexto.

## Estrutura

```text
SEGUNDO-CEREBRO-ANTIGRAVITY/
├── .agents/
│   ├── rules/
│   │   └── segundo-cerebro.md
│   └── workflows/
│       ├── daily-briefing.md
│       ├── end-session.md
│       ├── braindump.md
│       ├── weekly-review.md
│       ├── content-idea.md
│       ├── prospect-research.md
│       ├── pipeline.md
│       └── proposal-generator.md
├── _memory/
├── _knowledge/
├── _decisions/
├── _learnings/
├── _sessions/
├── _pipeline/
├── _prompts/
└── _legacy-claude-original/
```

## Observação sobre o legado

A pasta `_legacy-claude-original/` contém uma cópia do `CLAUDE.md` e dos comandos originais do ZIP de origem. Ela existe apenas para referência/auditoria. O Antigravity deve usar `.agents/`, não `_legacy-claude-original/`.

Leia também `GUIA-INSTALACAO-ANTIGRAVITY.md` e `GUIA-PERSONALIZACAO.md`.
