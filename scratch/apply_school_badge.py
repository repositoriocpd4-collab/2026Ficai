import re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for .school-badge.compact right after .school-badge i { ... }
css_target = ".school-badge i {\n      color: #0877c9;\n      font-size: 11px\n    }"
css_replacement = """.school-badge i {
      color: #0877c9;
      font-size: 11px
    }

    .school-badge.compact {
      padding: 2.5px 8px;
      font-size: 10.5px;
      font-weight: 700;
      gap: 4.5px;
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #bae6fd;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      white-space: nowrap;
    }

    .school-badge.compact i {
      color: #0284c7;
      font-size: 10px;
    }

    body.dark .school-badge.compact,
    body.dark-mode .school-badge.compact {
      background: #0f172a;
      color: #38bdf8;
      border-color: #0284c7;
    }

    body.dark .school-badge.compact i,
    body.dark-mode .school-badge.compact i {
      color: #38bdf8;
    }"""

if css_target in content:
    content = content.replace(css_target, css_replacement)
    print("1. Added .school-badge.compact CSS successfully!")
else:
    print("CSS target not matched exactly, checking alternative regex for .school-badge i...")
    content = re.sub(r'(\.school-badge i\s*\{[^}]+\})', r'\1\n\n    .school-badge.compact {\n      padding: 2.5px 8px;\n      font-size: 10.5px;\n      font-weight: 700;\n      gap: 4.5px;\n      background: #e0f2fe;\n      color: #0369a1;\n      border: 1px solid #bae6fd;\n      border-radius: 6px;\n      display: inline-flex;\n      align-items: center;\n      white-space: nowrap;\n    }\n    .school-badge.compact i {\n      color: #0284c7;\n      font-size: 10px;\n    }\n    body.dark .school-badge.compact, body.dark-mode .school-badge.compact {\n      background: #0f172a;\n      color: #38bdf8;\n      border-color: #0284c7;\n    }\n    body.dark .school-badge.compact i, body.dark-mode .school-badge.compact i {\n      color: #38bdf8;\n    }', content, count=1)
    print("1. Added CSS via regex fallback.")

# 2. Update moveFicaiToGerados
old_move_gerados = """      const aluno = record.aluno || 'Aluno';
      const turma = record.turma || '';
      const sit = sitLabel || record.situacao || 'Em acompanhamento';
      const viewedInfo = getCtViewInfo(record, fullNum);
      const eventAt = isCT
        ? (record.ctDevolvidoEm || record.ct_devolvido_em || record.updatedAt || record.createdAt)
        : (record.updatedAt || record.createdAt);
      const when = formatCtDateTime(eventAt);

      const chipHtml = isCT
        ? '<span class="chip" style="background:#e0f2fe;color:#0369a1;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">Atendida · Devolvida à Escola</span>'
        : ([CT_FLOW_STATUS.ENVIADA, CT_FLOW_STATUS.VISUALIZADA].includes(flow)
            ? '<span class="chip" style="background:#f3e8ff;color:#7c3aed;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">Encaminhada ao CT</span>'
            : '');

      let row = listGerados.querySelector(`.dash-list-row[data-ficai="${CSS.escape(fullNum)}"]`) ||
                listGerados.querySelector(`.dash-list-row[data-ficai="${CSS.escape(cleanNum)}"]`);

      const rowHtml = `
        <label class="custom-check-wrap" onclick="event.stopPropagation()">
          <input type="checkbox" class="gerados-check item-check" style="width:16px;height:16px;accent-color:#2563eb;cursor:pointer;">
        </label>
        <div class="dash-row-content" style="flex:1;display:flex;align-items:center;justify-content:space-between;gap:12px;">
          <div style="display:flex;align-items:center;gap:8px;min-width:0;flex-wrap:wrap;">
            <i class="fa-solid ${isCT ? 'fa-file-circle-check' : 'fa-tag'}" style="color:#2563eb;font-size:13px;"></i>
            <a href="#" class="dash-item-link" data-ficai="${escapeHtml(fullNum)}" data-student="${escapeHtml(aluno)}" data-turma="${escapeHtml(turma)}" data-sit="${escapeHtml(sit)}" style="font-weight:800;color:#0f172a;text-decoration:none;">
              ${escapeHtml(cleanNum)}/${escapeHtml(aluno)} / ${escapeHtml(turma)}
            </a>
            ${chipHtml}
          </div>
          <span style="font-size:11.5px;color:#64748b;font-weight:700;white-space:nowrap;">${escapeHtml(when)}</span>
        </div>`;"""

new_move_gerados = """      const aluno = record.aluno || 'Aluno';
      const turma = record.turma || '';
      const escola = record.escola || record.unidade || 'E.M. Elmir Figueira';
      const sit = sitLabel || record.situacao || 'Em acompanhamento';
      const viewedInfo = getCtViewInfo(record, fullNum);
      const eventAt = isCT
        ? (record.ctDevolvidoEm || record.ct_devolvido_em || record.updatedAt || record.createdAt)
        : (record.updatedAt || record.createdAt);
      const when = formatCtDateTime(eventAt);

      const schoolChipHtml = (isCT || record.escola)
        ? `<span class="school-badge compact" data-tooltip="Escola de origem: ${escapeHtml(escola)}"><i class="fa-solid fa-school"></i> ${escapeHtml(escola)}</span>`
        : '';

      const chipHtml = isCT
        ? '<span class="chip" style="background:#e0f2fe;color:#0369a1;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">Atendida · Devolvida à Escola</span>'
        : ([CT_FLOW_STATUS.ENVIADA, CT_FLOW_STATUS.VISUALIZADA].includes(flow)
            ? '<span class="chip" style="background:#f3e8ff;color:#7c3aed;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">Encaminhada ao CT</span>'
            : '');

      let row = listGerados.querySelector(`.dash-list-row[data-ficai="${CSS.escape(fullNum)}"]`) ||
                listGerados.querySelector(`.dash-list-row[data-ficai="${CSS.escape(cleanNum)}"]`);

      const rowHtml = `
        <label class="custom-check-wrap" onclick="event.stopPropagation()">
          <input type="checkbox" class="gerados-check item-check" style="width:16px;height:16px;accent-color:#2563eb;cursor:pointer;">
        </label>
        <div class="dash-row-content" style="flex:1;display:flex;align-items:center;justify-content:space-between;gap:12px;">
          <div style="display:flex;align-items:center;gap:8px;min-width:0;flex-wrap:wrap;">
            <i class="fa-solid ${isCT ? 'fa-file-circle-check' : 'fa-tag'}" style="color:#2563eb;font-size:13px;"></i>
            <a href="#" class="dash-item-link" data-ficai="${escapeHtml(fullNum)}" data-student="${escapeHtml(aluno)}" data-turma="${escapeHtml(turma)}" data-sit="${escapeHtml(sit)}" style="font-weight:800;color:#0f172a;text-decoration:none;">
              ${escapeHtml(cleanNum)}/${escapeHtml(aluno)} / ${escapeHtml(turma)}
            </a>
            ${schoolChipHtml}
            ${chipHtml}
          </div>
          <span style="font-size:11.5px;color:#64748b;font-weight:700;white-space:nowrap;">${escapeHtml(when)}</span>
        </div>`;"""

if old_move_gerados in content:
    content = content.replace(old_move_gerados, new_move_gerados)
    print("2. Updated moveFicaiToGerados successfully!")
else:
    print("Warning: old_move_gerados not matched exactly!")

# 3. Update moveFicaiToRecebidosCT
old_move_ct = """      const aluno = record.aluno || 'Aluno';
      const turma = record.turma || '';
      const viewedInfo = getCtViewInfo(record, fullNum);
      const sit = isCT ? (sitLabel || record.situacao || 'Recebida da Escola') : 'Devolutiva CT';
      const eventAt = isCT
        ? (record.ctEnviadoEm || record.ct_enviado_em || record.updatedAt || record.createdAt)
        : (record.ctDevolvidoEm || record.ct_devolvido_em || record.updatedAt || record.createdAt);
      const when = formatCtDateTime(eventAt);
      const chipHtml = isCT
        ? `<span class="chip" style="background:#f3e8ff;color:#7c3aed;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">${flow === CT_FLOW_STATUS.VISUALIZADA ? 'Em análise no CT' : 'Recebida da Escola'}</span>`
        : '<span class="chip" style="background:#f3e8ff;color:#7c3aed;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">Devolutiva CT</span>';

      let row = listCT.querySelector(`.dash-list-row[data-ficai="${CSS.escape(fullNum)}"]`) ||
                listCT.querySelector(`.dash-list-row[data-ficai="${CSS.escape(cleanNum)}"]`);

      const rowHtml = `
        <label class="custom-check-wrap" onclick="event.stopPropagation()">
          <input type="checkbox" class="ct-check item-check" style="width:16px;height:16px;accent-color:#7c3aed;cursor:pointer;">
        </label>
        <div class="dash-row-content" style="flex:1;display:flex;align-items:center;justify-content:space-between;gap:12px;">
          <div style="display:flex;align-items:center;gap:8px;min-width:0;flex-wrap:wrap;">
            <i class="fa-solid ${isCT ? 'fa-inbox' : 'fa-envelope-open-text'}" style="color:#7c3aed;font-size:13px;"></i>
            <a href="#" class="dash-item-link" data-ficai="${escapeHtml(fullNum)}" data-student="${escapeHtml(aluno)}" data-turma="${escapeHtml(turma)}" data-sit="${escapeHtml(sit)}" style="font-weight:800;color:#0f172a;text-decoration:none;">
              ${escapeHtml(cleanNum)}/${escapeHtml(aluno)} / ${escapeHtml(turma)}
            </a>
            ${chipHtml}
          </div>
          <span style="font-size:11.5px;color:#64748b;font-weight:700;white-space:nowrap;">${escapeHtml(when)}</span>
        </div>`;"""

new_move_ct = """      const aluno = record.aluno || 'Aluno';
      const turma = record.turma || '';
      const escola = record.escola || record.unidade || 'E.M. Elmir Figueira';
      const viewedInfo = getCtViewInfo(record, fullNum);
      const sit = isCT ? (sitLabel || record.situacao || 'Recebida da Escola') : 'Devolutiva CT';
      const eventAt = isCT
        ? (record.ctEnviadoEm || record.ct_enviado_em || record.updatedAt || record.createdAt)
        : (record.ctDevolvidoEm || record.ct_devolvido_em || record.updatedAt || record.createdAt);
      const when = formatCtDateTime(eventAt);

      const schoolChipHtml = (isCT || record.escola)
        ? `<span class="school-badge compact" data-tooltip="Escola de origem: ${escapeHtml(escola)}"><i class="fa-solid fa-school"></i> ${escapeHtml(escola)}</span>`
        : '';

      const chipHtml = isCT
        ? `<span class="chip" style="background:#f3e8ff;color:#7c3aed;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">${flow === CT_FLOW_STATUS.VISUALIZADA ? 'Em análise no CT' : 'Recebida da Escola'}</span>`
        : '<span class="chip" style="background:#f3e8ff;color:#7c3aed;font-weight:800;font-size:10.5px;padding:2px 8px;border-radius:99px;">Devolutiva CT</span>';

      let row = listCT.querySelector(`.dash-list-row[data-ficai="${CSS.escape(fullNum)}"]`) ||
                listCT.querySelector(`.dash-list-row[data-ficai="${CSS.escape(cleanNum)}"]`);

      const rowHtml = `
        <label class="custom-check-wrap" onclick="event.stopPropagation()">
          <input type="checkbox" class="ct-check item-check" style="width:16px;height:16px;accent-color:#7c3aed;cursor:pointer;">
        </label>
        <div class="dash-row-content" style="flex:1;display:flex;align-items:center;justify-content:space-between;gap:12px;">
          <div style="display:flex;align-items:center;gap:8px;min-width:0;flex-wrap:wrap;">
            <i class="fa-solid ${isCT ? 'fa-inbox' : 'fa-envelope-open-text'}" style="color:#7c3aed;font-size:13px;"></i>
            <a href="#" class="dash-item-link" data-ficai="${escapeHtml(fullNum)}" data-student="${escapeHtml(aluno)}" data-turma="${escapeHtml(turma)}" data-sit="${escapeHtml(sit)}" style="font-weight:800;color:#0f172a;text-decoration:none;">
              ${escapeHtml(cleanNum)}/${escapeHtml(aluno)} / ${escapeHtml(turma)}
            </a>
            ${schoolChipHtml}
            ${chipHtml}
          </div>
          <span style="font-size:11.5px;color:#64748b;font-weight:700;white-space:nowrap;">${escapeHtml(when)}</span>
        </div>`;"""

if old_move_ct in content:
    content = content.replace(old_move_ct, new_move_ct)
    print("3. Updated moveFicaiToRecebidosCT successfully!")
else:
    print("Warning: old_move_ct not matched exactly!")

# 4. Update column headers dynamically for CT
old_header_update = """      if (isCT) {
        if (ctCardTitle) ctCardTitle.textContent = 'FICAIs Recebidas';
        if (ctCardSubtitle) ctCardSubtitle.innerHTML = '<i class="fa-solid fa-school"></i> Fichas Criadas pelas Escolas';
        if (geradosCardTitle) geradosCardTitle.textContent = 'FICAIS Atendidas (Devolutivas)';
        if (geradosCardSubtitle) geradosCardSubtitle.innerHTML = '<i class="fa-solid fa-shield-halved"></i> Devolutivas enviadas às Escolas';"""

new_header_update = """      const ctColHeaders = document.querySelectorAll('.dash-split-card .dash-col-header');
      if (isCT) {
        if (ctCardTitle) ctCardTitle.textContent = 'FICAIs Recebidas';
        if (ctCardSubtitle) ctCardSubtitle.innerHTML = '<i class="fa-solid fa-school"></i> Fichas Criadas pelas Escolas';
        if (geradosCardTitle) geradosCardTitle.textContent = 'FICAIS Atendidas (Devolutivas)';
        if (geradosCardSubtitle) geradosCardSubtitle.innerHTML = '<i class="fa-solid fa-shield-halved"></i> Devolutivas enviadas às Escolas';
        ctColHeaders.forEach(h => h.textContent = 'N.º FICAI / ALUNO / TURMA / ESCOLA');"""

if old_header_update in content:
    content = content.replace(old_header_update, new_header_update)
    print("4. Updated column headers for CT successfully!")
else:
    print("Warning: old_header_update not matched exactly!")

# Also restore header text for non-CT
old_header_restore = """        if (geradosCardTitle) geradosCardTitle.textContent = 'Gerados';
        if (geradosCardSubtitle) geradosCardSubtitle.innerHTML = '<i class="fa-solid fa-school"></i> Fichas Criadas na Escola';
      }"""

new_header_restore = """        if (geradosCardTitle) geradosCardTitle.textContent = 'Gerados';
        if (geradosCardSubtitle) geradosCardSubtitle.innerHTML = '<i class="fa-solid fa-school"></i> Fichas Criadas na Escola';
        ctColHeaders.forEach(h => h.textContent = 'N.º FICAI / ALUNO / TURMA');
      }"""

if old_header_restore in content:
    content = content.replace(old_header_restore, new_header_restore)
    print("5. Updated column header restoration for Escola/Admin successfully!")
else:
    print("Warning: old_header_restore not matched exactly!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully!")
