# FICAI 4.0 — Fluxo Escola ↔ Conselho Tutelar

Esta versão contém a implementação do fluxo de tramitação solicitado sem criar cópias da FICAI.

## Fluxo implementado

- Escola cria a FICAI: permanece em **Gerados**.
- Escola envia ao Conselho Tutelar: permanece em **Gerados** na Escola e aparece em **FICAIs Recebidas** no CT.
- CT abre a FICAI: registra a **primeira visualização**, com data/hora e responsável, sem mover o documento.
- Escola passa a visualizar o indicador **Visualizada pelo CT**.
- Anotações internas do CT durante a análise não são tratadas como devolutiva formal.
- A FICAI só muda de contêiner quando o CT executa explicitamente **Devolver para a Escola**.
- Após a devolução:
  - Escola: **Gerados → Recebidos do CT**.
  - CT: **FICAIs Recebidas → FICAIs Atendidas (Devolutivas)**.
- O mesmo registro/ID da FICAI é preservado.
- O histórico anterior é preservado.
- Nova remessa ao CT inicia novo ciclo de visualização, sem apagar o histórico do ciclo anterior.

## Banco de dados — etapa obrigatória no Supabase

Antes de publicar esta versão em produção, execute **uma única vez** no SQL Editor do Supabase:

`MIGRACAO_FLUXO_CT.sql`

O script foi escrito de forma idempotente (`ADD COLUMN IF NOT EXISTS`, `CREATE INDEX IF NOT EXISTS` e `CREATE OR REPLACE FUNCTION`), portanto pode ser reaplicado em caso de dúvida sem duplicar as colunas criadas por esta atualização.

O arquivo `supabase_schema.sql` também já contém a estrutura consolidada para instalações novas.

## Arquivos principais alterados

- `index.html`
- `supabase_client.js`
- `supabase_schema.sql`
- `MIGRACAO_FLUXO_CT.sql` (novo)

## Validações realizadas nesta entrega

- Sintaxe JavaScript de `supabase_client.js`: validada com `node --check`.
- Sintaxe dos scripts JavaScript inline de `index.html`: validada com `node --check` após extração.
- O pacote não contém os arquivos `.bak`, o repositório `.git` nem os diretórios temporários usados na validação.

## Observação de implantação

A interface possui fallback de compatibilidade para instalações que ainda não receberam as novas colunas, mas o fluxo persistente completo entre dispositivos/perfis depende da execução de `MIGRACAO_FLUXO_CT.sql` no banco utilizado pela aplicação.
