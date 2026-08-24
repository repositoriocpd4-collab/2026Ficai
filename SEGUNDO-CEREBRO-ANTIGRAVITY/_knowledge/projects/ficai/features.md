---
tags: [knowledge, project, ficai, features]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Funcionalidades e Status

Status atual das funcionalidades do sistema FICAI 4.0 categorizadas rigorosamente por estágio de maturidade.

---

## 🟢 IMPLEMENTADO (100% Funcional e Validado)

1. **Módulo de Logs do Sistema (`#view-logs`):**
   - Menu lateral abaixo de *Configurações*.
   - Filtros de pesquisa em tempo real, seleção de nível (`create`, `update`, `cancel`, `auth`, `alert`) e data.
   - Cards com borda colorida contextual, tempo relativo (*"há 2 dias"*) e e-mail do usuário.
   - Acordeão **"Ver Detalhes Técnicos"** com payload JSON e botão de cópia.
   - Botão de exportação em CSV.
   - Disparadores automáticos de auditoria (login, logout, criação/edição de FICAI, cancelamento e encaminhamento ao CT).

2. **Gerador Automático Sequencial de Número FICAI:**
   - Cálculo automático do próximo número no padrão `XXXXX/2026` via IndexedDB/Supabase.
   - Atualização ao mudar o ano letivo, badge `[✨ Auto]` e botão de recálculo `[🔄]`.

3. **Mapeamento Cartográfico & Roteamento Viário Real:**
   - Renderização vetorial MapLibre GL com OpenFreeMap.
   - Traçado de rota viária real via API OSRM (contornando a litoral pela BR-101 / Rodovia Rio-Santos sem linhas retas no mar).
   - Cálculo exato de distância (~21.6 km) e tempo estimado (~21 min) entre a escola e a residência do aluno.

4. **Redesign UX/UI do Modal de Configurações (`configModal`):**
   - Grid de 2 colunas responsivo.
   - Cabeçalho com badge em degradê azul (`fa-building-columns`).
   - Ícones prefixados em cada campo (INEP, Nome, Diretor, Endereço, Bairro, Telefone, E-mail, Modalidade, Google Maps).
   - Campo **Modalidade de Ensino** em dropdown dinâmico com todas as modalidades municipais.
   - Card Toggle Switch animado para a opção **Unidade Ativa**.

5. **Sincronização Inicial de Dados de Escolas e Catálogos no Supabase:**
   - População de **67 escolas** na tabela `escolas` do Supabase.
   - Carga inicial das tabelas `modalidades`, `turmas`, `usuarios`, `permissoes`, `pessoas`, `procedimentos` e `motivos`.

6. **Painel Dashboard & Dual-Column Split (Recebidos CT / Gerados):**
   - Stat-cards recém-otimizados em UX/UI (116px altura mínima, padding compacto, tipografia de 25px, tags contextuais e recálculo automático em tempo real).

7. **Modal de Informações da FICAI:**
   - Visual *Dark Navy*, avatar 3D do estudante, metadados em caixa *inset*, linha do tempo auditável e inclusão de fatos novos pós-geração.

8. **Módulo de Encerramento e Reabertura de Casos:**
   - Justificativa formal de arquivamento por motivo legal e tabela com reabertura/restauração no formulário.

---

## 🟡 EM DESENVOLVIMENTO (Funcionalidades Parciais / Em Ajuste)

1. **Sincronização Bidirecional Automática Cloud ↔ Local:**
   - `supabase_client.js` possui os métodos CRUD, mas o sincronismo em background sem latência ao salvar FICAIs precisa de testes contínuos de estresse.
2. **Formulário Wizard de 6 Seções:**
   - O formulário gera o espelho A4 de impressão perfeitamente, mas a validação de regras de campos cruzados entre seções está em refinamento.

---

## 🔵 PLANEJADO (No Roadmap de Curto/Médio Prazo)

1. **Controle de Acesso Dinâmico por Perfil (RBAC Activo):**
   - Restrição estrita de visualização no menu e tabelas conforme a sessão ativa (`Escola`, `SMEDU`, `Conselho Tutelar`).
2. **Filtros Avançados no Relatório RAE:**
   - Agrupamento de alunos infrequentes por bairro, faixa etária e grau de vulnerabilidade social.

---

## 💡 IDEIAS (Sugestões Futuras)

1. **Integração via API com Diário de Classe Digital:**
   - Importação automática da lista de alunos que ultrapassaram o percentual limite de faltas lançadas pelos professores.
2. **Notificações Automatizadas via WhatsApp / E-mail:**
   - Webhooks para envio de alertas automáticos aos responsáveis legais ao ser gerada a FICAI.
