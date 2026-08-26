# Guia de Instalação - Google Antigravity

## 1. Pré-requisitos

- Google Antigravity IDE instalado e autenticado.
- Obsidian é opcional, mas recomendado para navegar e editar o vault.

Não é necessário instalar Claude Code, Node.js nem o pacote `@anthropic-ai/claude-code` para usar esta versão.

## 2. Descompactar

Extraia a pasta `SEGUNDO-CEREBRO-ANTIGRAVITY` para um local permanente, por exemplo:

```text
C:\Users\SEU_USUARIO\Documents\SEGUNDO-CEREBRO-ANTIGRAVITY
```

Evite usar uma pasta temporária ou Downloads como localização definitiva.

## 3. Abrir no Antigravity

Abra a pasta como workspace no Antigravity. Se você trabalha com um projeto de código separado, mantenha o segundo cérebro como pasta independente e adicione ambos ao mesmo Project quando quiser que o agente tenha acesso aos dois contextos.

## 4. Verificar a Rule

A regra principal está em:

```text
.agents/rules/segundo-cerebro.md
```

O Antigravity usa `.agents/rules` para regras de workspace. Na interface, abra **Customizations > Rules** e confirme que a regra aparece. Se houver seletor de ativação, deixe-a como **Always On**.

## 5. Verificar os Workflows

Os oito slash commands estão em:

```text
.agents/workflows/
```

No Agent, digite `/` e procure:

```text
/daily-briefing
/end-session
/braindump
/weekly-review
/content-idea
/prospect-research
/pipeline
/proposal-generator
```

Os workflows agora usam o texto/contexto fornecido junto ao comando. Não dependem mais da variável `$ARGUMENTS`.

Exemplos:

```text
/braindump Estou pensando em reorganizar a arquitetura do projeto...

/prospect-research Clínica Exemplo Rio de Janeiro

/proposal-generator clinica-exemplo
```

## 6. Abrir no Obsidian (opcional)

No Obsidian, escolha **Open folder as vault** e selecione a mesma pasta `SEGUNDO-CEREBRO-ANTIGRAVITY`. Assim, Antigravity e Obsidian trabalham sobre os mesmos arquivos Markdown.

## 7. Personalizar

Edite primeiro:

- `_knowledge/about-me.md`
- `_knowledge/goals.md`
- `_knowledge/projects.md`
- `.agents/rules/segundo-cerebro.md` na seção Identidade

Se você usa o módulo de negócios, complete também `_knowledge/business/`.

## 8. Primeiro teste

Abra uma nova conversa no Agent e execute:

```text
/daily-briefing
```

O agente deve consultar `_memory/current-state.md`, objetivos e projetos. Depois de uma sessão produtiva, execute:

```text
/end-session
```

Confirme que `_memory/current-state.md` foi atualizado.

## Troubleshooting

### Os slash commands não aparecem

1. Confirme que a pasta aberta no Antigravity é a raiz que contém `.agents/`.
2. Confirme que os arquivos estão em `.agents/workflows/*.md`.
3. Reabra o workspace/conversa.
4. Verifique se cada workflow possui frontmatter YAML com `description`.

### A regra não está sendo aplicada

1. Confirme `.agents/rules/segundo-cerebro.md`.
2. Abra **Customizations > Rules**.
3. Verifique a ativação da regra e use **Always On** quando disponível.

### O agente não lembra de outra conversa

O segundo cérebro não depende do histórico da conversa: a persistência ocorre nos arquivos. Execute `/end-session` ao terminar sessões relevantes e verifique `_memory/current-state.md`, `_decisions/` e `_learnings/`.

### O Obsidian não mostra `.agents`

Pastas iniciadas por ponto podem ficar ocultas dependendo da configuração. Isso não impede o Antigravity de usá-las.

## Referência de arquitetura

- Rules: contexto persistente do workspace.
- Workflows: processos repetíveis acionados por `/comando`.
- `_memory` e `_knowledge`: memória persistente em Markdown.
- Obsidian: interface opcional de organização e consulta.
