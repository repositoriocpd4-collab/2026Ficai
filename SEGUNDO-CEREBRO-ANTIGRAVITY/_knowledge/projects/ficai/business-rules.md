---
tags: [knowledge, project, ficai, business-rules]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Regras de Negócio do Sistema

## 1. Regras de Numeração da FICAI

- **Formato Oficial:** `XXXXX/ANO` (ex: `00022/2026`).
- **Geração Sequencial Automática:** O sistema calcula automaticamente o próximo número sequencial disponível no ano letivo selecionado com base nas FICAIs persistidas no IndexedDB e Supabase.
- **Vínculo com Ano Letivo:** Ao alterar o ano letivo no formulário, a numeração é recalculada automaticamente.
- **Edição Manual:** Permite sobreposição manual apenas para digitação de fichas físicas legadas com a devida sinalização.

---

## 2. Regras de Infrequência e Abertura de FICAI

- **Gatilho de Infrequência:** A FICAI deve ser gerada quando o aluno atingir o limite estipulado de faltas consecutivas ou alternadas injustificadas (conforme legislação e diretrizes da SMEDU).
- **Dados Obrigatórios da Ficha:**
  - Código INEP / Unidade Escolar cadastrada;
  - Nome completo do estudante, data de nascimento e filiação/responsável;
  - Turma, turno e modalidade de ensino;
  - Período exato das faltas;
  - Ao menos 1 procedimento interno de busca ativa realizado pela escola (com data);
  - Pelo menos 1 motivo ou hipótese de ausência assinalado.

---

## 3. Regras de Rastreabilidade e Histórico (`infoEntries`)

- **Imutabilidade do Histórico:** Todos os acontecimentos, contatos com familiares, pareceres do Conselho Tutelar e encaminhamentos possuem registro temporal com data, hora, tipo e e-mail do usuário responsável.
- **Linha do Tempo Auditável:** Fatos novos podem ser anexados à FICAI após a sua geração original sem alterar a numeração ou o espelho A4 impresso.

---

## 4. Regras de Cancelamento de FICAI

- **Cancelamento Formal:** Uma FICAI só pode ser cancelada mediante preenchimento do motivo oficial de cancelamento (ex: erro de digitação, duplicidade, matrícula indevida) e justificativa detalhada.
- **Auditoria de Cancelamento:** Todo cancelamento é registrado no módulo **Logs do Sistema** com o e-mail do usuário que executou a ação e os metadados do cancelamento.

---

## 5. Regras de Encerramento e Reabertura de Casos

- **Motivos de Encerramento:**
  - Reintegração / Retorno do aluno às aulas com frequência regularizada;
  - Mudança de município / Transferência formal;
  - Maioridade / Outros motivos legais justificados.
- **Reabertura:** Casos encerrados podem ser reabertos se o aluno reincidir na infrequência durante o mesmo ano letivo, preservando todo o histórico anterior.

---

## 6. Regras dos Logs do Sistema

- **Retenção:** Fila FIFO de até 500 registros armazenados no navegador (`localStorage`) e espelhados em nuvem.
- **Tipos de Eventos Auditados:** `create` (cadastros), `update` (alterações), `cancel` (cancelamentos), `auth` (login/logout), `alert` (avisos).
