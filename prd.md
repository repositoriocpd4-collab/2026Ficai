# Documento de Requisitos do Produto (PRD) — FICAI 4.0

**Sistema de Ficha de Comunicação de Aluno Infrequente**  
**Secretaria Municipal de Educação de Itaguaí (SMEDU / CPD)**  
*Versão Atual: 4.0.2 — Atualizado em: 19/08/2026*

---

## 1. Visão Geral do Produto

O **FICAI 4.0** é a plataforma oficial da Secretaria Municipal de Educação de Itaguaí (SMEDU) destinada à identificação, acompanhamento, intervenção e controle da evasão e infrequência escolar na Rede Municipal de Ensino.

O sistema integra e consolida os fluxos intersetoriais entre:
- **Unidades Escolares** (Professores, Orientadores Educacionais e Direção);
- **Rede de Apoio à Escola (RAE)** e Assistência Social (CRAS/CREAS);
- **Conselho Tutelar de Itaguaí**;
- **Promotorias de Justiça da Infância e da Juventude** (Ministério Público).

---

## 2. Objetivos Principais

1. **Combate Ativo à Evasão**: Identificar alunos infrequentes nos estágios iniciais de faltas antes da consolidação do abandono escolar.
2. **Padronização Legal e Documental**: Emissão do espelho oficial da FICAI em formato padrão A4 (1 página retrato) para arquivamento e trâmite legal.
3. **Rastreabilidade e Histórico Contínuo**: Linha do tempo digital auditável que recebe novos fatos, visitas e providências mesmo após a geração inicial da ficha.
4. **Alta Disponibilidade e Offline-First**: Operação local resiliente através de IndexedDB combinada com sincronização em nuvem via Supabase.

---

## 3. Identidade Visual & Design System

- **Tipografia Universal**: Família tipográfica **Alexandria** (pesos de 100 a 900) aplicada em toda a aplicação (títulos, tabelas, formulários, modais e botões).
- **Paleta de Cores**:
  - *Navy Municipal*: `#071a2f`, `#0c2138`, `#15365a`
  - *Primary Blue*: `#0066cc`, `#0877c9`
  - *Accent Gold*: `#b8860b`, `#ffd700`
  - *Status*: Alerta Crítico (Vermelho `#ef4444`), Aviso (Amarelo `#f59e0b`), Conselho Tutelar (Roxo `#8b5cf6`), Sucesso/Retorno (Verde `#10b981`).
- **Aparência e Efeitos**:
  - Suporte completo a **Modo Claro** e **Modo Noturno** (*Dark Mode*).
  - Componentes com profundidade suave, *glassmorphism*, bordas translúcidas e caixas *inset*.
- **Mecanismo Universal de Tooltips**:
  - Engine própria em JS (`initTooltipEngine`) com posicionamento flutuante automático (`top`, `bottom`, `left`, `right`), setas direcionais dinâmicas e proteção contra estouro de tela (*viewport bounds detection*).

---

## 4. Módulos e Funcionalidades

### 4.1 Dashboard
- **Painel de Estatísticas**:
  - Casos Ativos, Motivo Principal (Falta de Motivação), Trabalho Familiar, Saúde/Doença, Alunos Desistentes e FICAIs Finalizadas com tags e tendências semanais.
- **Controle de Evasões / Frequência (Layout Split Dual-Column)**:
  - **Barra de Filtros Superior**:
    - Campo de busca global (*live search*): aluno, documento ou responsável;
    - Dropdowns customizados: *Todas as Turmas*, *Todas as Situações* e *Período Temporal (Últimos 30 dias)*;
    - Reset rápido e foco com feedback visual.
  - **Coluna 1 — Recebidos CT**:
    - Identificação visual com ícone de caixa de entrada em badge azul claro;
    - Contador dinâmico de documentos recebidos;
    - Checkbox de seleção em lote (*Select All*);
    - Itens com indicador de alerta e link direto para o modal de informações (`0021/Ana Clara Nascimento / 7B`).
  - **Coluna 2 — Gerados**:
    - Identificação visual com ícone de etiqueta em badge azul claro;
    - Contador dinâmico de documentos gerados;
    - Checkbox de seleção em lote (*Select All*);
    - Tags coloridas por status (Verde, Azul, Roxo, Cinza) e links com abertura instantânea do modal de histórico (`0017/Bruno Henrique Silva / 6A`, etc.).

### 4.2 Gerar FICAI
- **Gerador Automático Sequencial de Número FICAI**:
  - Algoritmo inteligente que analisa todas as fichas persistidas no IndexedDB local e registros prévios do ano letivo;
  - Gera automaticamente o próximo número disponível no padrão oficial (ex: `00022/2026`);
  - Atualização dinâmica em tempo real ao selecionar um novo **Ano Letivo**;
  - Selo em cápsula `[✨ Auto]` interativo com tooltip e botão de recálculo rápido `[🔄]`;
  - Permite edição manual caso a unidade precise registrar uma numeração física legada.
- **Formulário Passo a Passo em 6 Seções**:
  1. *Escola e Aluno*: Seleção da escola, autocompletar de dados cadastrais do estudante, endereço e responsáveis.
  2. *Situação Escolar*: Turma, turno, modalidade, período de faltas e comunicação.
  3. *Procedimentos da Escola*: Checkboxes com datas para registro de contatos, visitas e reuniões.
  4. *Motivos e Situação*: Constatação dos motivos de ausência, vulnerabilidades sociais e observações.
  5. *Diagnóstico da Evasão*: Grupos diagnósticos (Pedagógico, Familiar, Psicossocial, Saúde).
  6. *Revisão e Impressão*: Visualização do espelho oficial A4 e emissão de PDF.

### 4.3 Modal de Informações da FICAI
- **Layout Premium Fiel ao Design System**:
  - Cabeçalho em degradê *Dark Navy* com botões translúcidos (*Editar FICAI*, *A4 / PDF*, Fechar `✕`).
  - Avatar do estudante esférico em degradê escuro com iniciais em branco e turma em destaque.
  - Grade de metadados em caixas *inset* (`NÚMERO`, `ANO LETIVO`, `PERÍODO DE FALTAS`, `ÚLTIMA ATUALIZAÇÃO`).
  - Painéis de situação, vulnerabilidades, observações e procedimentos com ícones coloridos.
  - Linha do tempo auditável de acompanhamento pós-geração.
  - Formulário para registrar novos fatos com selo dourado metálico `Salva no histórico` e salvamento persistente.

### 4.4 Configurações & Cadastros
- Módulo de gerenciamento de catálogos:
  - Unidades Escolares;
  - Turmas, Turnos e Anos Letivos;
  - Procedimentos da Escola;
  - Motivos da Ausência e Diagnósticos.

---

## 5. Arquitetura Técnica & Banco de Dados

### 5.1 Front-end
- **Tecnologias**: HTML5 Semântico, CSS3 Moderno (Vanilla com Variáveis CSS), JavaScript Vanilla ES6+ (sem frameworks pesados para máxima performance).
- **Fontes & Ícones**: Google Fonts (Alexandria) e Font Awesome 6.

### 5.2 Camada de Dados Local
- **IndexedDB**: Banco local `FICAI4LocalDB` (versão 1) com as *object stores*:
  - `students`: Dados cadastrais de alunos;
  - `ficais`: Fichas completas com dados de formulário, metadados e array de `infoEntries` (histórico pós-geração).

### 5.3 Camada Cloud (Supabase)
- **Instância**: `https://ojvxsrvmmkjxfgyczypm.supabase.co`
- **Tabelas Relacionais Criadas**:
  - `escolas`: Unidades escolares de Itaguaí;
  - `turmas`: Turmas e turnos;
  - `alunos`: Cadastro de estudantes;
  - `ficais`: Fichas registradas;
  - `procedimentos_realizados`: Ações escolares executadas;
  - `motivos_ausencia`: Motivos de falta identificados;
  - `diagnosticos_evasao`: Diagnósticos consolidados;
  - `historico_acompanhamento`: Linha do tempo pós-geração;
  - `encaminhamentos_ct`: Trâmites do Conselho Tutelar;
  - `atuacao_promotoria`: Registros do Ministério Público;
  - `encerramento_casos`: Fechamento com motivo e parecer.
- Políticas de Row Level Security (RLS) habilitadas.

---

## 6. Histórico de Alterações e Implementações (Changelog)

| Data | Versão | Descrição da Implementação |
| :--- | :--- | :--- |
| **19/08/2026** | `4.0.0` | Criação do protótipo base da FICAI 4.0 com IndexedDB e espelho A4 de impressão. |
| **19/08/2026** | `4.0.1` | Configuração do schema relacional no Supabase (`supabase_schema.sql` e `supabase_client.js`). |
| **19/08/2026** | `4.0.1` | Adição de título oficial da aba e favicon oficial da Prefeitura Municipal de Itaguaí. |
| **19/08/2026** | `4.0.1` | Implementação do motor de tooltips universal dinâmico e micro-interações de hover. |
| **19/08/2026** | `4.0.2` | Padronização universal da tipografia para a fonte **Alexandria** (pesos 100–900). |
| **19/08/2026** | `4.0.2` | Redesenho completo do **Modal de Informações da FICAI** com design *Dark Navy*, avatar radial 3D e selo dourado. |
| **19/08/2026** | `4.0.2` | Habilitação do clique sobre o nome do aluno na tabela do Dashboard para abertura imediata do modal de informações. |
| **19/08/2026** | `4.0.2` | Implementação de ordenação e filtros dinâmicos clicáveis nos títulos das colunas da tabela de Controle de Evasões / Frequência. |
| **19/08/2026** | `4.0.2` | Criação do documento oficial de requisitos (`prd.md`). |
| **19/08/2026** | `4.0.3` | Adaptação completa do painel **Controle de Evasões / Frequência** para o formato *Split Dual-Column* (*Recebidos CT* e *Gerados*), com filtros avançados de busca, turma, situação e período. |
| **19/08/2026** | `4.0.4` | Implementação da **geração automática sequencial do Número FICAI** com vínculo ao ano letivo, histórico persistido, badge interativo `[✨ Auto]` e botão de recálculo dinâmico. |

---

## 7. Roadmap & Próximas Etapas

- [ ] **Sincronização Bidirecional em Nuvem**: Conexão em segundo plano entre o IndexedDB local e o Supabase via `supabase_client.js`.
- [ ] **Módulo de Controle de Acesso (RBAC)**: Perfis diferenciados para *Escola*, *Orientação Pedagógica*, *SMEDU/Administrador* e *Conselho Tutelar*.
- [ ] **Integração com Diário Digital**: Importação automática de listas de alunos infrequentes com base nas faltas lançadas pelos professores.
- [ ] **Notificações Automatizadas**: Webhooks para avisos via WhatsApp e e-mail para responsáveis e equipe da RAE.
