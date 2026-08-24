---
tags: [memory, state, current]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# Estado Atual do Projeto — FICAI 4.0

## Última Atualização: 24/08/2026

### O Que Realmente Existe e Foi Implementado (Validados)

1. **Módulo 'Logs do Sistema' (`#view-logs`):**
   - Item de navegação no menu lateral abaixo de *Configurações*.
   - Interface completa com filtros por texto (*live search*), nível de evento (*Criação*, *Atualização*, *Cancelamento*, *Autenticação*, *Alertas*) e filtro por data.
   - Cards de atividades com bordas coloridas contextuais, ícone circular, tempo relativo (*"há 2 dias"*), usuário e descrição.
   - Acordeão **"Ver Detalhes Técnicos ⌄"** expandindo JSON estruturado com cópia direta.
   - Exportação em formato CSV.
   - Disparo automático de logs integrado a: confirmação de cancelamento, criação/edição de FICAI, encaminhamento ao Conselho Tutelar e autenticação (login/logout).

2. **Banco de Dados Supabase (`https://ojvxsrvmmkjxfgyczypm.supabase.co`):**
   - Tabela `escolas` totalmente sincronizada com **67 registros** (todas as 64 escolas municipais de Itaguaí extraídas da base oficial + registros do sistema).
   - Tabelas auxiliares migradas e populadas: `modalidades` (3), `turmas` (12), `usuarios` (5), `permissoes` (5), `pessoas` (6), `procedimentos` (7), `motivos` (41).
   - Arquivo `supabase_client.js` configurado e funcional.

3. **Redesign UX/UI do Modal de Configurações (`configModal`):**
   - Modal reformulado com grid de 2 colunas responsivo.
   - Badge com ícone no cabeçalho (`fa-building-columns`).
   - Ícones prefixando cada campo de entrada (INEP, Nome, Diretor, Endereço, Bairro, Telefone, E-mail, Modalidade, Google Maps).
   - Campo **Modalidade de Ensino** convertido para seletor dinâmico com todas as modalidades municipais.
   - Campo **Unidade Ativa** convertido para Card com Toggle Switch animado (chave seletora verde/cinza).

4. **Dashboard e Stat-Cards Corrigidos:**
   - O cálculo estático dos Stat-Cards foi atualizado para refletir com **100% de precisão os registros reais do sistema** (5 Casos Ativos, 0 FICAI Finalizadas e 5 Alunos em Busca Ativa), eliminando offsets estáticos legados do protótipo (`24`, `71`, `138`).
   - O painel em formato *Split Dual-Column* (*Recebidos CT*: 1 registro / *Gerados*: 4 registros) calcula dinamicamente seus contadores e percentuais a cada inclusão ou alteração.

5. **Endereços Residenciais de Alunos Atualizados:**
   - Todos os endereços de alunos no catálogo e no banco foram atualizados para ruas reais de Itaguaí, RJ (ex: **Bruno Henrique Silva** ➔ `R. João Ramalho, 73 - São Salvador, Itaguaí - RJ, 23810-290`, **Ana Clara Nascimento** ➔ `Rua Pastor Manuel Avelino de Souza, 120 - Fazenda Caxias, Itaguaí - RJ, 23835-006`, etc.).
   - As regras de geocodificação no MapLibre GL foram expandidas em `REGION_GEO_LOCATIONS` para cobrir Fazenda Caxias, São Salvador, Parque de Santana, Monte Serrat e Vila Nova.
   - Registros sincronizados no Supabase Cloud.

6. **Gerador Automático Sequencial de Número FICAI:**
   - Numeração dinâmica no formato `XXXXX/2026` com botão de recálculo `[🔄]` e selo `[✨ Auto]`.

7. **Módulo de Encerramento e Reabertura de Casos:**
   - Formulário de arquivamento por motivo legal e tabela de reabertura imediata de FICAIs.

---

### O Que Está em Desenvolvimento ou Incompleto

- **Sincronização Bidirecional Automática Cloud ↔ Local:** O `supabase_client.js` possui métodos prontos, mas a sincronização em tempo real (background worker) entre o `IndexedDB` local e a nuvem precisa de validação contínua em todas as operações de escrita/edição.
- **Formulário Principal do Wizard (Seções 1 a 6):** As seções do formulário estão visuais e geram espelho A4 de impressão, porém requerem ajustes de validação estrita de regras de negócio em alguns campos.

---

### O Que Está Apenas Planejado / Ideias

- **Módulo de Controle de Acesso (RBAC):** Bloqueio dinâmico das telas de acordo com a sessão logada (Escola só vê seus alunos; Conselho Tutelar só vê devolutivas; SMEDU vê tudo).
- **Integração com Diário de Classe Digital:** Importação por API de alunos infrequentes com base nas chamadas diárias dos professores.
- **Notificações via WhatsApp / E-mail:** Envio de avisos para responsáveis e equipe da RAE via webhooks.

---

### Próximos Passos Recomendados

1. Validar a gravação e leitura direta de FICAIs no Supabase durante a submissão do formulário principal.
2. Homologar os testes de permissão de acesso por perfil (RBAC) com as contas `usr-escola` e `usr-smedu`.
