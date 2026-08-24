---
tags: [knowledge, projects, core]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# Meus Projetos — FICAI 4.0

---

### FICAI 4.0 — Sistema de Gestão da Evasão Escolar (SMEDU / Itaguaí)

| Campo | Valor |
|-------|-------|
| **Status** | `em desenvolvimento` |
| **Prioridade** | `alta` |
| **Início** | 2026-08-19 |
| **Deadline** | `sem deadline formal informado` |
| **Responsável** | Joe Amado (Concepção, Regras de Negócio, Dev, Banco de Dados, UX/UI, Testes) |
| **Próximo passo** | Validar a persistência bidirecional Supabase ↔ IndexedDB e refinar telas/fluxos pendentes no wizard e modais. |
| **Bloqueios** | Nenhum no momento. |

**Descrição do Sistema:**  
Plataforma oficial da Secretaria Municipal de Educação de Itaguaí (SMEDU) destinada à identificação, acompanhamento, intervenção e controle da evasão e infrequência escolar na Rede Municipal de Ensino. Integra Unidades Escolares, RAE, Conselho Tutelar e Promotoria de Justiça (Ministério Público).

**Funcionalidades por Estágio:**
- **🟢 IMPLEMENTADO:** Criação e gerenciamento de FICAIs (wizard 6 seções), identificação por N.º FICAI / Aluno / Turma, gerador sequencial `XXXXX/2026`, consulta e acompanhamento, Split Grid (Recebidos CT / Gerados), modal de informações detalhadas com linha do tempo, georreferenciamento cartográfico com rota OSRM real (BR-101 / Rio-Santos), módulo de auditoria "Logs do Sistema", cancelamento auditável com histórico permanente, encerramento e reabertura de casos, cadastro/configuração de escolas (67 unidades no Supabase) e turmas.
- **🟡 EM DESENVOLVIMENTO:** Validação fina da sincronização bidirecional em nuvem (`supabase_client.js`), refinamento de validações de regras de negócio entre seções do wizard.
- **🔵 PLANEJADO:** Módulo de controle de acesso por perfis (RBAC: *Escola*, *SMEDU*, *Conselho Tutelar*), relatórios analíticos avançados por bairro e vulnerabilidade.
- **💡 IDEIA:** Integração via API com o Diário de Classe Digital e notificações proativas via WhatsApp / E-mail.

**Arquitetura e Stack:**
- **Stack:** HTML5, Vanilla CSS3 (Alexandria Font), JavaScript ES6+, Supabase (PostgreSQL), MapLibre GL, OpenFreeMap, API OSRM Engine, IndexedDB (`FICAI4LocalDB`).
- **Instância Supabase:** `https://ojvxsrvmmkjxfgyczypm.supabase.co`
- **Repositório:** Git Local + GitHub (`repositoriocpd4-collab/2026Ficai`).
- **Documentação detalhada:** Consulte a pasta `_knowledge/projects/ficai/` para acessar a documentação completa de Arquitetura, Regras de Negócio, Banco de Dados, Funcionalidades, Pendências e UX/UI.

