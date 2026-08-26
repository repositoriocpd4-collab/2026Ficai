---
tags: [knowledge, project, ficai, ux-ui]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Padrões de Design System e UX/UI

## 1. Tipografia e Cores

- **Família Tipográfica:** **Alexandria** (pesos 100 a 900) via Google Fonts. Aplicada universalmente a títulos, botões, modais, formulários e tabelas.
- **Paleta de Cores Institucional:**
  - *Dark Navy (Cabeçalhos / Modais)*: `#071a2f`, `#0c2138`, `#0f172a`, `#1e293b`
  - *Primary Blue*: `#0066cc`, `#0284c7`, `#0369a1`
  - *Accent Gold / Status*: `#b8860b`, `#ffd700`
  - *Status de Notificação*: Sucesso (`#10b981` / `#22c55e`), Alerta (`#f59e0b`), Erro/Cancelamento (`#ef4444` / `#dc2626`), Conselho Tutelar (`#8b5cf6`).

---

## 2. Padrões de Componentes

### 2.1 Stat-Cards (Cards de Estatísticas)
- **Dimensões:** Altura mínima de 116px, padding compacto (14px 14px 12px), número numérico de 25px em negrito.
- **Badges:** Cápsulas superiores e inferiores com ícone e texto relativo (*"Ativo"*, *"Social"*, *"Saúde"*, *"Semana"*).

### 2.2 Modais de Configuração (`configModal`)
- **Largura:** `min(94vw, 780px)`.
- **Cabeçalho:** Badge de ícone em degradê azul (`width: 44px; height: 44px; border-radius: 12px; font-size: 20px; background: linear-gradient(135deg, #0284c7, #0369a1)`), título 18px e subtítulo 12.5px.
- **Grid Layout:** 2 colunas para dados curtos (INEP, Diretor, Bairro, Telefone, E-mail, Modalidade) e 1 coluna total para Nome da Escola, Endereço e Link do Google Maps.
- **Campos de Entrada:** Wrapper `.config-input-icon-wrap` com ícone prefixado em `#94a3b8` que muda para `#0284c7` no foco, com foco em anel suave (`0 0 0 3.5px rgba(2, 132, 199, 0.14)`).
- **Chave Seletora (Toggle Switch):** Substitui caixas de seleção padrão pelo `.config-toggle-card` com controle animado em verde (`#22c55e`).

### 2.4 Split Dual-Column Grid (Recebidos do CT vs Gerados)
- **Recebidos do CT (Entrada / Retornos Intersetoriais):**
  - **Cor Temática:** Roxo Imperial / Violeta (`#7c3aed`, `#8b5cf6`).
  - **Destaque Visual:** Borda superior sólida (`border-top: 4px solid #7c3aed`), degradê translúcido no cabeçalho, badge circular radial em roxo com ícone `fa-inbox`, subtítulo `🛡️ Devolutivas & Retornos CT` e pílula de contador em degradê roxo fosco.
  - **Linhas de Tabela:** Marcação lateral esquerda em `#8b5cf6`.
- **Gerados (Produção Escolar / Fichas em Acompanhamento):**
  - **Cor Temática:** Primary Blue da Educação (`#0284c7`, `#0369a1`).
  - **Destaque Visual:** Borda superior sólida (`border-top: 4px solid #0284c7`), degradê translúcido em azul, badge circular em azul com ícone `fa-file-circle-plus`, subtítulo `🏫 Fichas Criadas na Escola` e pílula de contador em tom azul claro.
  - **Linhas de Tabela:** Marcação lateral esquerda em `#0284c7`.
