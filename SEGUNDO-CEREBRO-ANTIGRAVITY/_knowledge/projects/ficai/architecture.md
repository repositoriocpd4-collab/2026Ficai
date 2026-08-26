---
tags: [knowledge, project, ficai, architecture]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Arquitetura Técnica

## 1. Visão Geral da Arquitetura

O FICAI 4.0 é construído sob o padrão de **Single Page Application (SPA) Monolítica Modularizada**, priorizando alta performance, independência de frameworks pesados, resiliência offline (*Offline-First*) e integração nativa com serviços em nuvem.

---

## 2. Tecnologias Utilizadas (Stack Real)

| Camada | Tecnologia / Biblioteca | Função |
| :--- | :--- | :--- |
| **Interface (UI)** | HTML5 Semântico + Vanilla CSS3 | Estrutura limpa, variáveis CSS e suporte a Light/Dark mode. |
| **Lógica / Engine** | JavaScript Vanilla ES6+ | Manipulação de DOM, estado local e roteamento SPA. |
| **Tipografia & Ícones** | Google Fonts (Alexandria) + Font Awesome 6 | Identidade visual padronizada (pesos 100-900). |
| **Banco de Dados Local** | IndexedDB (`FICAI4LocalDB` v1) + `localStorage` | Persistência local imediata e cache resiliente offline. |
| **Banco de Dados Cloud** | Supabase (PostgreSQL 15+) | Instância `https://ojvxsrvmmkjxfgyczypm.supabase.co` para sincronização remota. |
| **Mapas & Roteamento** | MapLibre GL 5.x + OpenFreeMap + OSRM Engine API | Renderização vetorial e cálculo de rotas viárias reais (BR-101). |
| **Automações / Tooling** | Python 3.12+ (pandas, openpyxl, urllib) | Extração de dados da planilha oficial de escolas e seeds para o Supabase. |

---

## 3. Estrutura de Arquivos do Repositório

- `index.html`: Arquivo principal da aplicação (contém as seções `<section class="view">`, componentes, diálogos e scripts da SPA).
- `supabase_client.js`: Cliente de integração JavaScript com a REST API do Supabase (`StudentService`, `FicaiService`, etc.).
- `supabase_schema.sql`: Script SQL contendo o esquema relacional PostgreSQL completo, funções PL/pgSQL e políticas RLS.
- `dados_completos_todas_colunas.xlsx`: Base de dados original contendo as 64 escolas municipais de Itaguaí.
- `prd.md`: Documento de Requisitos do Produto (Versão 4.1.1).

---

## 4. Estratégia de Persistência Híbrida (Offline-First)

```
[ Usuário / Interface ]
         │
         ▼
 [ IndexedDB: FICAI4LocalDB ]  ◄── Opções instantâneas (Sem latência)
         │
         ▼ (Sincronização em segundo plano via JS)
 [ REST API Supabase / PostgreSQL ] ◄── Nuvem oficial SMEDU
```

1. **Gravação Primária Local:** Todas as fichas, registros e atualizações são gravadas instantaneamente no `IndexedDB` (`FICAI4LocalDB`) e `localStorage`.
2. **Sincronização Cloud:** O cliente `supabase_client.js` consome a API do Supabase com a chave pública configurada (`sb_publishable_...`), sincronizando as tabelas relacionais do PostgreSQL.
