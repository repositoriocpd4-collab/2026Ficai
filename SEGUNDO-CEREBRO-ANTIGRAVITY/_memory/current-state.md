---
tags: [memory, state, current]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# Estado Atual do Projeto — FICAI 4.0

## Última Atualização: 24/08/2026

### 🟢 O Que Realmente Existe e Foi Implementado (Validados no Código e Banco)

1. **Módulo de Auditoria 'Logs do Sistema' (`#view-logs`):**
   - Item de navegação no menu lateral abaixo de *Configurações*.
   - Interface com busca em tempo real (*live search*), filtro por nível de evento (*Criação*, *Atualização*, *Cancelamento*, *Autenticação*, *Alertas*) e filtro por data.
   - Cards de atividades com bordas coloridas contextuais, ícone circular, tempo relativo (*"há 2 dias"*), e-mail do usuário e descrição.
   - Acordeão **"Ver Detalhes Técnicos ⌄"** expandindo payload JSON estruturado com cópia direta para a área de transferência.
   - Exportação direta de dados em CSV.
   - Disparo automático de logs auditáveis integrado aos eventos de: confirmação de cancelamento, criação/edição de FICAI, encaminhamento ao Conselho Tutelar e autenticação (login/logout).

2. **Banco de Dados Relacional Supabase Cloud (`https://ojvxsrvmmkjxfgyczypm.supabase.co`):**
   - Tabela `escolas` sincronizada com **67 registros** (64 escolas municipais oficiais de Itaguaí + cadastros do sistema).
   - Tabelas populadas e migradas: `modalidades` (3), `turmas` (12), `usuarios` (5), `permissoes` (5), `pessoas` (6), `procedimentos` (7), `motivos` (41), `students`, `ficais`, `ficai_info_entries`, `marcadores`, `student_tags` e `cancelamentos_ficais`.
   - Script SQL `supabase_schema.sql` 100% idempotente com triggers de `updated_at` e políticas de Row Level Security (RLS) configuradas.
   - Arquivo `supabase_client.js` encapsulando os serviços `StudentService`, `FicaiService`, `MarcadorService`, `EscolaService` e `CancelamentoService`.

3. **Camada de Dados Local (IndexedDB):**
   - Banco local `FICAI4LocalDB` (versão 1) com *object stores* `students` e `ficais` operando de forma resiliente em ambiente local.

4. **Redesign UX/UI do Modal de Configurações (`configModal`):**
   - Modal reformulado em grid responsivo de 2 colunas.
   - Cabeçalho com badge em degradê azul (`fa-building-columns`).
   - Ícones prefixados em cada campo de entrada (INEP, Nome, Diretor, Endereço, Bairro, Telefone, E-mail, Modalidade, Google Maps).
   - Campo **Modalidade de Ensino** em seletor dinâmico conectado às modalidades cadastradas.
   - Card **Unidade Ativa** com chave seletora animada (*Toggle Switch*).

5. **Dashboard Stat-Cards e Split Grid:**
   - Stat-cards otimizados com altura mínima de 116px, padding compacto (14px 14px 12px), tipografia de 25px e badges contextuais (`Ativo`, `Principal`, `Social`, `Saúde`, `Alerta`, `Sucesso`).
   - Recálculo dinâmico automático dos Stat-Cards a partir dos registros reais do sistema.
   - Painel em layout *Split Dual-Column* (*Recebidos CT* e *Gerados*) com busca global, seletores de turma, situação e período.

6. **Endereços Residenciais & Roteamento Cartográfico Real:**
   - Endereços de estudantes atualizados para ruas reais de Itaguaí, RJ (ex.: Fazenda Caxias, São Salvador, Monte Serrat, Vila Nova).
   - Integração vetorial via MapLibre GL 5.x + OpenFreeMap.
   - Traçado de rota viária real via API OSRM contornando o litoral pela BR-101 / Rodovia Rio-Santos (sem linhas retas cortando a água), exibindo distância (~21.6 km) e tempo estimado (~21 min).

7. **Marcador Visual "Visualizado pelo CT" (CT View Tracker UX):**
   - Selo em tom lilás/roxo `👁️ Visualizado pelo CT` com efeito hover e tooltip contendo data, hora e e-mail auditável da leitura (`conselhotutelar@itaguai.rj.gov.br`).

8. **Tela de Cancelamento de FICAI (`#view-cancelamento`):**
   - Layout em 3 colunas estruturadas (Cards de FICAIs + Linha do Tempo | Wizard Stepper 1-2-3 | Resumo de Dados).
   - Tabela no rodapé em tom carmim com o **Histórico Auditável de FICAIs Canceladas** (`CancelamentoService`), garantindo que o registro permaneça 100% permanente.

9. **Gerador Automático Sequencial de Número FICAI:**
   - Numeração dinâmica no formato `XXXXX/2026` com botão de recálculo `[🔄]` e selo `[✨ Auto]`.

10. **Módulo de Encerramento e Reabertura de Casos:**
    - Arquivamento formal por motivo legal e restauração/reabertura imediata de FICAIs no formulário.

13. **Redirecionamento Inteligente, Confirmação e Modal Sofisticado de Cancelamento:**
    - O clique no ícone "Cancelar FICAI" (`#btnActionEncerrar` na barra de ações rápidas) valida se há uma ficha selecionada via checkbox.
    - **Validação estrita de escopo:** Permite o cancelamento exclusivamente para FICAIs da lista **Gerados** (fichas da escola), impedindo o cancelamento de registros do Conselho Tutelar com aviso via toast.
    - **Modal Sofisticado de Sucesso (`#modalCancelamentoSucesso`):** Após o clique em "Sim, cancelar", um modal com estética refinada (gradiente esmeralda, selo de status `CANCELADA`, card resumido com N.º da FICAI, Aluno, Motivo, Responsável e Data/Hora, botão de "Concluir" e "Ver no Histórico") é exibido, enquanto o registro é gravado no Supabase Cloud, IndexedDB e histórico auditável.

14. **Credenciais de Acesso das Escolas Atualizadas:**
    - Senha padrão dos 65 e-mails institucionais de escolas atualizada de `Ficai22026` para **`FicaiSmedu`** no arquivo `supabase_schema.sql` e no mecanismo de autenticação local em `index.html`.

15. **Controle de Acesso e Visibilidade de Módulos no Menu Lateral (RBAC por Perfil):**
    - Quando o usuário conectado **não for administrador** (ex: perfil Escola / usuário padrão):
      - **Módulos Visíveis (7):** `Dashboard`, `Gerar FICAI`, `Dados da Ficha`, `RAE`, `Encerramento de Casos`, `Cancelamento de FICAI` e `Sobre o Sistema`.
      - **Módulos Restritos (3):** `Conselho Tutelar`, `Configurações` e `Logs do Sistema` (bem como a seção `Cadastros`) são ocultados dinamicamente.
      - **Navegação Protegida:** A função `showView()` bloqueia redirecionamentos diretos de não-administradores para telas restritas, exibindo aviso via toast.
    - Quando o usuário conectado **for o Administrador** (`cpdinfra@edu.itaguai.rj.gov.br` / role `Administrador`):
      - Todos os 10 módulos e seções permanecem totalmente visíveis e acessíveis.

16. **Travamento do Campo Escola para Usuários Não-Administradores:**
    - O campo `<select id="escola">` no Passo 1 do formulário principal é preenchido e travado automaticamente (`disabled = true`, fundo suave `#f8fafc` e cursor `not-allowed`) com a unidade escolar logada quando o usuário não for administrador.
    - Se a sessão for do Administrador (`cpdinfra@edu.itaguai.rj.gov.br` / role `Administrador`), o campo permanece liberado para seleção livre de qualquer unidade escolar da rede.

17. **Manual Oficial Completo do Sistema ("Sobre o Sistema") & Gerador de PDF Premium:**
    - A visualização `#view-sobre` contém o **Manual Oficial do FICAI 4.0** completo.
    - **Botão Exclusivo para Administrador ("Gerar PDF do Manual"):**
      - Localizado no topo (*Hero Banner*), com botão em gradiente esmeralda (`#059669` a `#10b981`), ícone PDF da FontAwesome, badge `Admin` e efeitos micro-animados de hover.
      - **Ação Inteligente de Exportação:** limpa termos de busca ativos, expande automaticamente todas as dúvidas do FAQ sanfonado (`<details>`) e aplica regras CSS de impressão (`@media print`) exclusivas que ocultam barras de navegação, índices laterais e filtros, renderizando o manual completo em PDF vetorial de alta fidelidade.
      - **Controle de Acesso RBAC:** O botão fica visível exclusivamente para usuários Administradores (`cpdinfra@edu.itaguai.rj.gov.br` / role `Administrador`).

18. **Redesign de UX/UI da Tela de Cancelamento de FICAI (`#view-cancelamento`):**
    - **Card de Preenchimento de Alta Visibilidade:**
      - Agrupamento dos campos de entrada em um container destacado com borda suave (`#cbd5e1`), sombra de elevação e cabeçalho com ícone `fa-file-circle-xmark` e badge `Etapa 2 de 3`.
    - **Labels com Ícones e Micro-Ajuda:**
      - Adicionados ícones temáticos (`fa-list-check`, `fa-pen-to-square`, `fa-user-shield`, `fa-calendar-days`) a todas as legendas e aviso de gravação no histórico de auditoria.
    - **Caixa de Confirmação Interativa:**
      - O checkbox de revisão de informações foi transformado em um banner interativo com efeito dinâmico: ao ser marcado, o fundo alterna de azul suave para verde esmeralda (`#ecfdf5` / `#10b981`), oferecendo feedback imediato de progresso ao usuário.
    - **Orientação Clara do Próximo Passo:**
      - Adicionado um callout instrutivo no topo da barra de ações informando exatamente o que ocorrerá ao clicar no botão: *"Ao clicar em Avançar para revisão, uma janela com o resumo completo e a confirmação com o selo de auditoria será exibida."*
    - **Botão de Ação Destacado:**
      - Botão *"Avançar para revisão"* estilizado em gradiente azul vibrante (`linear-gradient(135deg, #2563eb, #1d4ed8)`), sombra projetada e micro-animação na seta no *hover*.

19. **Deploy Realizado com Sucesso no GitHub (`repositoriocpd4-collab/2026Ficai`):**
    - Todas as alterações da sessão foram consolidadas e enviadas com sucesso para o branch **`DevFicai`**.
    - **Commit `cd51583`:** `feat: RBAC por perfil no menu, trava de escola para nao-admin, manual completo em sobre o sistema com exportacao PDF e redesign UX/UI no cancelamento`
    - **Status:** Repositório remoto sincronizado e 100% atualizado.

20. **Limpeza e Zeramento das FICAIs Iniciais (Pronto para Teste Real):**
    - Zerados os registros simulados das listas **"Gerados"** (`0 registros`) e **"Recebidos do CT"** (`0 registros`) no Dashboard.
    - Zerados os cartões simulados em **"Dados da Ficha"** e na tela de **"Cancelamento de FICAI"**.
    - Zerada a tabela do **"Histórico Auditável de FICAIs Canceladas (Registro Permanente)"** (`0 registros`).
    - Zeradas as notificações do sininho de alertas do cabeçalho (badge de não lidas zerado/ocultado e dropdown com mensagem de estado vazio).
    - Zerados os contadores de estatísticas para **0** casos ativos, permitindo o cadastro de novos registros reais a partir do número `00001/2026`.
    - **Commits `4275ec6`, `62c1d2d` e `b3b66fc` enviados ao GitHub:** `feat: zerar FICAIs geradas, recebidas do CT, historico de cancelamento e notificacoes para testes reais`.

21. **Correção do Preenchimento Automático da Modalidade no Formulário (`Gerar FICAI`):**
    - Criada a função reativa `updateModalidadeFromTurma()` que escuta a seleção do campo **Turma**.
    - Ao selecionar qualquer turma (ex: `6º Ano A`, `7º Ano B`, `NCEJA VI A`, `Pré II A`), o sistema automaticamente lê a modalidade vinculada cadastrada no menu *Configurações & Cadastros* (or dataset) e preenche instantaneamente o campo **Modalidade** (ex: *Ensino Fundamental*, *EJA*, *Educação Infantil*).
    - Também auto-seleciona o **Ano Escolar** e **Turno** caso ainda não estejam preenchidos.
    - **Commit `24b89e8` enviado ao GitHub:** `fix: auto-preencher campo Modalidade ao selecionar a Turma na criacao de FICAI`.

22. **Sincronização Dinâmica e Resolução de Renderização da Tabela do Conselho Tutelar (`#view-conselho`):**
    - Removidas as linhas estáticas demonstrativas mock (`00018/Carla Souza Ribeiro`, `00015/Eduarda Gomes`, `00012/Lucas Mendonça`) das tabelas do Conselho Tutelar, Encerramento de Casos e RAE.
    - Definidas e exportadas as funções de renderização reativa: `renderSavedFicai()`, `moveFicaiToGerados()`, `moveFicaiToRecebidosCT()`, `renderConselhoTableRow()` e `syncConselhoTableFromDatabase()`.
    - Criada a função de inicialização síncrona `loadSavedFicais()`, prevenindo exceções não tratadas de referência e garantindo que qualquer FICAI encaminhada ao Conselho Tutelar (ex: `00022/Ana Clara Nascimento`) seja lida do IndexedDB e exibida instantaneamente na tabela do Conselho Tutelar (`#tbodyConselho`).
    - **Commits `cc11910` enviados e implantados na branch `DevFicai`:** `fix: renderizar dinamicamente FICAIs no Conselho Tutelar e inicializacao reativa das tabelas`.

23. **Recálculo Dinâmico Automático e Zeramento dos Stat-Cards:**
    - Criada a função `updateAllDynamicStats()` que lê as FICAIs salvas no `IndexedDB` e recalcula em tempo real todas as porcentagens e contadores do Dashboard e do Conselho Tutelar.
    - Quando o banco de dados está vazio (0 registros), todos os cartões de estatísticas (*Casos Ativos*, *Falta de motivação*, *Trabalho familiar*, *Doença / Saúde*, *Alunos Desistentes*, *FICAI Finalizadas*, *Aguardando Recebimento*, *Em Diligência*, *Prazo de Retorno*, *Devolvidas à Escola*) exibem estritamente **`0`** ou **`0%`**, eliminando quaisquer resquícios de porcentagens mock estáticas.
    - **Commit `ae88fa7` enviado e implantado no GitHub (branch `DevFicai`):** `fix: recálculo dinâmico e zeramento total dos stat-cards quando o banco estiver vazio`.

24. **Histórico Documental FICAI (Estilo SEI Simplificado com Anexos):**
    - Implementado o novo padrão de histórico documental no modal de informações da FICAI (`#infoModal`).
    - Substituído o antigo bloco estático de composição por um menu dropdown moderno **`+ Adicionar`** (`Adicionar informação` e `Anexar documento`) com formulário *inline* dinâmico.
    - Suporte a múltiplos anexos com *drag-and-drop* e seleção de arquivos (`.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.png`, `.jpg`), validação de até 5 MB por arquivo e conversão/armazenamento local em Base64 dentro do registro no IndexedDB.
    - Renderização da linha do tempo enriquecida com cards visuais de anexo com opções de pré-visualização direta no navegador e download, mantendo histórico permanente e auditável sem sobreescrita de dados.
    - Integração fluida com devoluções e encaminhamentos (`sendDevolverInfoEntry`), login e permissões.

---

### 🟡 O Que Está em Desenvolvimento ou Requer Validação Fina

1. **Sincronização Bidirecional Automática Cloud ↔ Local:**
   - O `supabase_client.js` possui todos os métodos CRUD, mas a sincronização em tempo real (worker em background) entre o `IndexedDB` e o Supabase requer validação contínua nos fluxos de escrita/edição do wizard.
2. **Validações Cruzadas no Wizard de 6 Seções:**
   - O formulário gera o espelho A4 de impressão com alta fidelidade visual, mas requer refinamento de regras de preenchimento obrigatório cruzado entre seções.

---

### 🔵 O Que Está Planejado / No Roadmap

1. **Módulo de Controle de Acesso por Perfis (RBAC Ativo):**
   - Bloqueio dinâmico das telas e visões de acordo com o perfil logado (*Escola*, *SMEDU*, *Conselho Tutelar*).
2. **Relatórios Analíticos RAE:**
   - Filtros consolidados por bairro e grau de vulnerabilidade social.

---

### 💡 Ideias Futuras

1. **Integração via API com Diário de Classe Digital:**
   - Importação automatizada de alunos infrequentes com base nas chamadas diárias dos professores.
2. **Notificações Automatizadas via WhatsApp / E-mail:**
   - Disparo de alertas para responsáveis e equipe da RAE ao gerar uma FICAI.

---

### 🚀 Próximos Passos Recomendados para Hoje

1. Executar testes de gravação direta e leitura de fichas completas no Supabase via `supabase_client.js`.
2. Validar o comportamento síncrono das seções do formulário principal wizard no `index.html`.
3. Homologar as permissões e o isolamento de visualização dos perfis de usuário (`usr-escola`, `usr-smedu`, `usr-ct`).
ção e leitura direta de FICAIs no Supabase durante a submissão do formulário principal.
2. Homologar os testes de permissão de acesso por perfil (RBAC) com as contas `usr-escola` e `usr-smedu`.
