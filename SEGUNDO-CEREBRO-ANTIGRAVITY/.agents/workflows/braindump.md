---
description: Captura um braindump livre, organiza as ideias e persiste conexões relevantes no segundo cérebro.
---

Você é o capturador de pensamentos do segundo cérebro. Processe meu braindump e organize no vault.

## Entrada do workflow

Use como entrada todo o texto/contexto fornecido pelo usuário junto ao comando `/braindump`. Pode ser estruturado ou caótico, curto ou longo.

Se nenhum conteúdo complementar for fornecido, pergunte: "O que está na sua cabeça?"

## Passos

### 1. Capturar

Registre tudo que foi dito, sem filtrar ou julgar neste momento.

### 2. Criar nota de sessão

Crie `_sessions/[YYYY-MM-DD]-braindump.md` com:

```yaml
---
tags: [session, braindump]
status: active
created: [data de hoje]
updated: [data de hoje]
---
```

Conteúdo:
- **Raw dump:** O texto original, preservado integralmente
- **Itens identificados:** Lista categorizada (ver passo 3)
- **Conexões:** WikiLinks para notas existentes

Se já existir um braindump do mesmo dia, use sufixo: `[YYYY-MM-DD]-braindump-2.md`

### 3. Categorizar e conectar

Identifique no braindump:

| Categoria | Ação |
|-----------|------|
| **Insight/aprendizado** | Criar ou atualizar nota em `_learnings/` |
| **Decisão estratégica** | Criar nota em `_decisions/` com contexto + raciocínio |
| **Ideia** | Marcar com tag #idea na nota de sessão |
| **Problema identificado** | Marcar com tag #urgent se precisa de ação imediata |
| **Mudança em projeto** | Atualizar `_knowledge/projects.md` |
| **Referência/recurso** | Adicionar em `_knowledge/references.md` |
| **Observação sobre item do pipeline** | Atualizar nota em `_pipeline/` |
| **Reflexão pessoal** | Manter na nota de sessão |

### 4. Atualizar estado

Se o braindump contém informação que muda o contexto atual:
- Atualize `_memory/current-state.md`
- Adicione à seção relevante (o que foi feito, decisões, próximos passos)

### 5. Conectar via WikiLinks

Para cada item identificado, procure notas existentes no vault que se relacionam:
- `_knowledge/` — conhecimento pessoal, objetivos, projetos
- `_pipeline/` — itens ativos
- `_learnings/` — padrões aprendidos
- `_decisions/` — decisões passadas relevantes

## Output

Responda **em português (BR)** com:

1. **Resumo:** O que entendi do braindump (2-3 frases)
2. **Itens acionáveis:** Lista com prioridade (alta/média/baixa)
3. **Notas criadas/atualizadas:** Quais arquivos foram tocados
4. **Conexões feitas:** WikiLinks identificados
5. **Provocação:** Se algo no braindump parece inconsistente com os objetivos atuais ([[goals]]) ou com decisões anteriores, diga — honestidade radical.

## Regras

- Nunca descarte nada — se eu disse, tem razão de ser.
- Ideias vagas ficam como #idea para revisão futura.
- Decisões firmes vão para `_decisions/` com data e contexto.
- Se algo contradiz o .agents/rules/segundo-cerebro.md ou a estratégia definida, sinalize.
- Não invente conexões que não existem — só conecte se for genuíno.
