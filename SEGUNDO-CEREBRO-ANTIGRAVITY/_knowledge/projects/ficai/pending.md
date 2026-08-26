---
tags: [knowledge, project, ficai, pending]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Pendências, Bugs e Soluções

## 1. Pendências Ativas de Desenvolver / Ajustar

| ID | Área | Descrição da Pendência | Prioridade |
| :---: | :--- | :--- | :---: |
| **PND-01** | Banco Cloud | Homologar gravação e leitura ponta a ponta de FICAIs na tabela `ficais` do Supabase durante o clique em *"Salvar FICAI"*. | Alta |
| **PND-02** | RBAC | Ativar o bloqueio visual e de rotas do menu lateral conforme a sessão ativa (`usr-escola`, `usr-smedu`, `usr-conselho`). | Média |
| **PND-03** | RAE | Refinar a exibição de diagnósticos de vulnerabilidade no módulo RAE. | Média |
| **PND-04** | Form Wizard | Adicionar máscaras de entrada em tempo real para CPF, Telefone e CEP no formulário. | Baixa |

---

## 2. Bugs Identificados e Solucionados (Histórico de Correções)

| Data | Componente | Bug Identificado | Solução Aplicada |
| :---: | :--- | :--- | :--- |
| **23/08/2026** | Layout / SPA | `view-logs` ficava oculto em tela branca ao clicar no menu. | Identificado que a tag `<section id="view-cancelamento">` não havia sido fechada antes de `view-logs`. Adicionado o `</section>` correto. |
| **23/08/2026** | Supabase REST | Erro HTTP 400 ao enviar campo `bairro` para a tabela `escolas`. | Identificado que a tabela no Supabase possuía colunas simplificadas (`id`, `nome`, `endereco`, `telefone`, `email`, `ativo`). Ajustada a carga REST para enviar os dados nos campos ativos. |
| **23/08/2026** | Supabase Sync | Erro HTTP 500 (`duplicate key`) ao salvar escolas em lote. | Identificada duplicidade de INEP no registro de uma escola da planilha. Ajustado o script para atribuir IDs 100% únicos (`rec_id`). |
| **23/08/2026** | Modal UX/UI | Modal de edição de escolas apresentava lista longa e vertical sem ícones nem campo seletor de modalidade. | Redesenho completo do `configModal` em grid de 2 colunas, ícones prefixados, dropdown para **Modalidade de Ensino** e Toggle Switch para **Unidade Ativa**. |
