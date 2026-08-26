---
tags: [knowledge, project, ficai, decisions]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Registro de Decisões Estratégicas e Técnicas

Histórico imutável de decisões de arquitetura, banco de dados e regras de negócio tomadas para o FICAI 4.0.

---

### DEC-001 (19/08/2026): Adoção de Arquitetura Single Page Application (SPA) Monolítica Vanilla

- **Contexto:** Necessidade de altíssima performance de carregamento e operação offline resiliente em unidades escolares com conectividade instável em Itaguaí.
- **Decisão:** Desenvolver o front-end sem frameworks JS pesados (React/Vue/Angular), utilizando HTML5 semântico, Vanilla CSS3 e JS Vanilla ES6+ em arquitetura SPA.
- **Raciocínio:** Elimina overhead de compilação, tempo de inicialização nulo e facilita o empacotamento para operação local (IndexedDB) e hospedagem leve.

---

### DEC-002 (19/08/2026): Estratégia de Persistência Híbrida (IndexedDB + Supabase)

- **Contexto:** Garantir que o usuário nunca perca os dados de uma FICAI mesmo se a internet cair durante o preenchimento.
- **Decisão:** Utilizar o IndexedDB (`FICAI4LocalDB`) como camada de persistência local primária e síncrona, espelhando os dados via REST API no Supabase PostgreSQL.
- **Raciocínio:** Proporciona experiência instantânea ao usuário e garante alta disponibilidade e resiliência.

---

### DEC-003 (23/08/2026): Criação do Módulo de Auditoria 'Logs do Sistema'

- **Contexto:** Exigência de conformidade legal e rastreabilidade sobre quem gerou, alterou ou cancelou FICAIs e acessou o portal.
- **Decisão:** Implementar a tela `#view-logs` com classe `SystemLogService` integrada aos eventos de autenticação, geração, edição e cancelamento de fichas.
- **Raciocínio:** Garante transparência intersetorial (SMEDU, Conselho Tutelar, Ministério Público) sobre as ações realizadas no sistema.

---

### DEC-004 (23/08/2026): Redesign do Modal de Configurações com Grid 2 Colunas e Modalidades Dinâmicas

- **Contexto:** O modal de edição de escolas apresentava uma lista vertical única com campos empilhados e sem opções pré-definidas de modalidades de ensino.
- **Decisão:** Reestruturar o `configModal` em layout de 2 colunas responsivo, adicionar ícones prefixados em todos os campos, converter o campo *Modalidade de Ensino* em dropdown dinâmico e usar chave seletora (*Toggle Switch*) para o status ativo.
- **Raciocínio:** Melhora substancialmente a velocidade de preenchimento e reduz erros de digitação de secretários e diretores escolares.
