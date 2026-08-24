---
tags: [knowledge, goals, core]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# Meus Objetivos — Projeto FICAI 4.0

Definição estratégica de objetivos do projeto FICAI 4.0. Este arquivo é dinâmico e evolui conforme o progresso do desenvolvimento.

---

## Curto Prazo (Próximos 30 dias)

### Objetivo 1: Consolidar o Banco de Dados e a Camada de Persistência
- **O que seria sucesso:** Integração 100% confiável entre o IndexedDB local e a instância nuvem do Supabase (`https://ojvxsrvmmkjxfgyczypm.supabase.co`), garantindo que FICAIs geradas, atualizações, cancelamentos e históricos sejam salvos e recuperados sem perda de dados.
- **Métricas:** 64+ escolas totalmente sincronizadas (concluído), 0 erros de escrita no Supabase ao emitir ou atualizar FICAIs, sincronização automática de `infoEntries`.
- **O que está me impedindo:** Necessidade de harmonizar os esquemas locais (`FICAI4LocalDB`) e remotos (PostgreSQL no Supabase) e tratar eventuais falhas de conexão de forma transparente.
- **Próximo passo concreto:** Testar e validar a gravação e leitura de fichas completas no Supabase através do `supabase_client.js`.

### Objetivo 2: Estruturar e Refinar os Fluxos da FICAI & UX/UI das Telas
- **O que seria sucesso:** Fluxo completo da FICAI operando de ponta a ponta com telas refinadas em UX/UI (Formulário de 6 seções, Histórico/Modal de Informações, Logs do Sistema, Encerramento/Reabertura, Conselho Tutelar e Configurações).
- **Métricas:** Telas do sistema adaptadas aos padrões visuais Alexandria / Dark Navy, modais padronizados com o novo layout em 2 colunas com ícones e feedback positivo nos testes de interface.
- **Próximo passo concreto:** Mapear e implementar validações de regras de negócio pendentes no fluxo de encaminhamento e fechamento de ficha.

---

## Médio Prazo (Próximos 6 meses)

### Objetivo 1: Homologação e Implantação Operacional na Rede Municipal de Itaguaí
- **O que seria sucesso:** Aplicação evoluída de protótipo para sistema operacional em produção, sendo utilizado pelas escolas da rede municipal e equipe da SMEDU.
- **Métricas:** Sistema rodando com autenticação RBAC por perfis (Escola, SMEDU, Conselho Tutelar), importação de turmas/alunos e suporte a acompanhamento intersetorial.
- **Dependências:** Sistema totalmente testado, sem inconsistências de dados e com módulo de controle de acesso (RBAC) ativado.

---

## Longo Prazo (Próximo 1 ano)

### Objetivo 1: Ecossistema Integrado FICAI 4.0 (Diário Digital & Notificações)
- **O que seria sucesso:** Integração automatizada por APIs com o Diário de Classe Digital de Itaguaí e disparos de notificações proativas via WhatsApp/E-mail para a Rede de Apoio à Escola (RAE) e responsáveis.
- **Por que isso importa:** Automatiza a detecção da infrequência nos primeiros dias de falta, agilizando drasticamente a busca ativa e a proteção do estudante.

---

## Antiobjetivos (O que NÃO fazer no FICAI 4.0)

- **Não mascarar erros ou incoerências:** Nunca cobrir falhas de banco ou contrato com dados fakes silenciosos.
- **Não comprometer a UX/UI:** Não aceitar telas poluidas, desproporcionais ou sem suporte ao Dark Mode.
- **Não romper a rastreabilidade:** Não permitir alterações no histórico de acompanhamento sem registro de data, usuário e detalhes.
