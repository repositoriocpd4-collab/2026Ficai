---
tags: [knowledge, goals, core]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# Objetivos do Projeto — FICAI 4.0

Definição estratégica de objetivos do projeto FICAI 4.0. Este arquivo é dinâmico e evoluirá continuamente conforme o desenvolvimento avança.

---

## Curto Prazo (Próximos 30 dias)

O objetivo principal é transformar o **FICAI 4.0** em uma solução funcional, organizada e confiável, evoluindo progressivamente do protótipo para uma aplicação operacional.

### Prioridades dos Próximos 30 Dias:
1. **Consolidar o Banco de Dados:**
   - Garantir integração total e confiável entre o `IndexedDB` local (`FICAI4LocalDB`) e a instância no Supabase Cloud (`https://ojvxsrvmmkjxfgyczypm.supabase.co`).
2. **Validar os Principais Fluxos:**
   - Homologar os fluxos de Geração de FICAI (6 seções), Consulta, Atualização, Marcador do Conselho Tutelar (`👁️ Visualizado pelo CT`), Cancelamento permanente com histórico auditável e Encerramento/Reabertura.
3. **Desenvolver e Refinar as Telas & UX/UI:**
   - Elevar o padrão visual da interface (Alexandria Typography, Dark Navy Mode, Stat-Cards com 116px e padding otimizado, glassmorphism e modais em 2 colunas com ícones).
4. **Garantir a Persistência Correta dos Dados:**
   - Assegurar que nenhuma ficha gerada ou alteração de linha do tempo seja perdida durante oscilações de conectividade local.
5. **Estruturar o Fluxo Completo da FICAI:**
   - Garantir a rastreabilidade intersetorial completa (Escola ➔ RAE ➔ Conselho Tutelar ➔ Promotoria de Justiça).
6. **Identificar Regras de Negócio Ausentes & Corrigir Inconsistências:**
   - Auditar campos de formulário, numeração automática `XXXXX/2026` e validações cruzadas entre seções.
7. **Evoluir Progressivamente do Protótipo para Aplicação Operacional:**
   - Migrar dados simulados para cadastros reais homologados da Rede Municipal de Itaguaí.

---

## Médio Prazo (Próximos 6 meses)

### Implantação e Operação na Rede Municipal de Itaguaí
- **Métricas:** Sistema rodando com autenticação RBAC por perfis (*Escola*, *Orientação Pedagógica*, *SMEDU*, *Conselho Tutelar*), importação oficial de turmas/alunos e uso diário pelas secretarias escolares.
- **Dependências:** Validação total de persistência e segurança de acesso.

---

## Longo Prazo (Próximo 1 ano)

### Ecossistema Integrado FICAI 4.0
- **Integração com Diário Digital:** Importação por API de alunos infrequentes com base nas chamadas diárias dos professores.
- **Notificações Automatizadas:** Avisos via WhatsApp / E-mail para responsáveis e equipe da RAE.

---

## Antiobjetivos (O que NUNCA fazer no FICAI 4.0)

- **Não mascarar erros:** Nunca cobrir falhas de banco ou contrato com dados fakes silenciosos.
- **Não comprometer a UX/UI:** Não aceitar telas poluídas, desproporcionais ou sem suporte ao Dark Mode.
- **Não romper a rastreabilidade:** Não permitir alterações no histórico sem registro de data, usuário e detalhes técnicos.

