import re

with open('FICAI_4_0_Prototipo (6).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update font and styles in head
style_replacement = """<title>Portal FICAI/SMEDU </title>
<link rel="icon" href="https://novoportal.itaguai.rj.gov.br/++resource++gov.cidades/favicon.ico" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="supabase_client.js"></script>
<style>
:root{
  --blue:#005a9c;--blue-2:#0877c9;--blue-light:#edf5fc;--navy:#071d41;--bg:#f4f7fc;--card:#fff;--text:#152238;
  --muted:#627289;--line:#dce4f0;--red:#dc2626;--red-light:#fef2f2;--purple:#7c3aed;--purple-light:#f5f3ff;
  --yellow:#d97706;--yellow-light:#fffbeb;--green:#16a34a;--green-light:#f0fdf4;
  --shadow-sm:0 2px 6px rgba(18,44,82,.04);
  --shadow:0 10px 28px -4px rgba(18,44,82,.08), 0 0 0 1px rgba(220,228,240,.6);
  --shadow-lg:0 20px 38px -6px rgba(18,44,82,.14), 0 0 0 1px rgba(200,215,235,.8);
  --radius-sm:8px;--radius:14px;--radius-lg:18px;
  --font:"Alexandria", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:var(--font);background:var(--bg);color:var(--text);font-size:14.5px;line-height:1.5;-webkit-font-smoothing:antialiased}
button,input,select,textarea{font:inherit}
button{cursor:pointer}
a{text-decoration:none;color:inherit}
.hidden{display:none!important}

/* Custom modern scrollbar */
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:rgba(0,0,0,.03)}
::-webkit-scrollbar-thumb{background:#c5d2e2;border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:#9ab0c8}
body.dark ::-webkit-scrollbar-track{background:rgba(255,255,255,.02)}
body.dark ::-webkit-scrollbar-thumb{background:#33445b}

/* App Shell */
.app-shell{min-height:100vh;display:grid;grid-template-columns:280px minmax(0,1fr);transition:grid-template-columns .24s cubic-bezier(.16,1,.3,1)}
.app-shell.sidebar-collapsed{grid-template-columns:76px minmax(0,1fr)}
.sidebar{position:sticky;top:0;height:100vh;background:#fff;border-right:1px solid var(--line);z-index:40;overflow-x:hidden;overflow-y:auto;display:flex;flex-direction:column;transition:width .24s ease,box-shadow .24s ease;box-shadow:2px 0 12px rgba(12,30,56,.02)}
.brand{height:96px;background:linear-gradient(135deg,#00528e,#0877c9);color:#fff;display:flex;align-items:center;justify-content:flex-start;padding:0 26px;font-weight:800;font-size:26px;letter-spacing:.2px;white-space:nowrap;overflow:hidden;position:relative}
.brand::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:linear-gradient(90deg,rgba(255,255,255,.4),transparent)}
.brand-short{display:none;font-size:24px;letter-spacing:0}
.menu-section-title{padding:18px 24px 6px;color:#8595ac;text-transform:uppercase;font-size:10.5px;font-weight:800;letter-spacing:1.2px}
.nav-item{display:flex;align-items:center;gap:13px;padding:12.5px 22px;border-left:4px solid transparent;color:#33445c;font-weight:600;font-size:14px;transition:all .18s ease;white-space:nowrap;position:relative}
.nav-item i{width:22px;text-align:center;color:#0877c9;font-size:16.5px;transition:transform .18s ease,color .18s ease}
.nav-item:hover{background:#f1f6fc;color:var(--blue);padding-left:26px}
.nav-item:hover i{transform:scale(1.15);color:var(--blue)}
.nav-item.active{background:linear-gradient(90deg,#edf5fd,#f8fbfe);color:var(--blue);border-left-color:var(--blue);font-weight:750}
.nav-item.active i{color:var(--blue)}
.nav-item.ct{color:#6d28d9} .nav-item.ct i{color:#7c3aed}
.nav-item.archive{color:#b91c1c} .nav-item.archive i{color:#dc2626}
.nav-item.active.ct{border-left-color:#7c3aed;background:#f5f0ff}
.nav-item.active.archive{border-left-color:#dc2626;background:#fef2f2}
.menu-divider{height:1px;background:#e2e9f3;margin:8px 18px}
.sidebar-footer{margin-top:auto;padding:18px 22px 24px;color:#78889e;font-size:11.5px;line-height:1.45;border-top:1px solid #eef2f8}

.app-shell.sidebar-collapsed .brand{justify-content:center;padding:0}
.app-shell.sidebar-collapsed .brand-full{display:none}
.app-shell.sidebar-collapsed .brand-short{display:inline}
.app-shell.sidebar-collapsed .menu-section-title,
.app-shell.sidebar-collapsed .menu-divider,
.app-shell.sidebar-collapsed .sidebar-footer{display:none}
.app-shell.sidebar-collapsed .nav-item{justify-content:center;gap:0;padding:15px 0;border-left-width:3px}
.app-shell.sidebar-collapsed .nav-item .nav-label{display:none}
.app-shell.sidebar-collapsed .nav-item:hover{padding-left:0}

/* Topbar */
.main{min-width:0}
.topbar{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.94);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line);box-shadow:0 2px 10px rgba(11,33,64,.04)}
.top-row{height:52px;border-bottom:1px solid rgba(220,228,240,.6);display:flex;align-items:center;justify-content:space-between;padding:0 30px}
.gov-area{display:flex;align-items:center;gap:15px}.gov-logo{width:74px;height:29px;object-fit:contain}.state{font-size:17px;font-weight:600;color:#1e3250}
.header-links{display:flex;align-items:center;gap:20px;color:#00579a;font-size:14px;font-weight:600}
.header-links a{transition:color .18s;padding:5px 8px;border-radius:6px}
.header-links a:hover{color:#0769ad;background:#eef6fc}
.header-icon-btn{border:1px solid #d8e2ee;background:#fff;color:#0e589e;width:34px;height:34px;border-radius:9px;display:grid;place-items:center;font-size:15px;position:relative;transition:all .18s ease}
.header-icon-btn:hover{background:#edf5fc;border-color:#b5d4ed;transform:translateY(-1px);color:#024e8f}
.pulse-badge{position:absolute;top:4px;right:4px;width:8px;height:8px;background:#16a34a;border-radius:50%;box-shadow:0 0 0 2px #fff;animation:pulseIndicator 2.2s infinite}
@keyframes pulseIndicator{0%{box-shadow:0 0 0 0 rgba(22,163,74,.7)}70%{box-shadow:0 0 0 6px rgba(22,163,74,0)}100%{box-shadow:0 0 0 0 rgba(22,163,74,0)}}

.bottom-row{height:58px;display:flex;align-items:center;padding:0 30px;gap:16px}
.hamb{display:grid;place-items:center;width:36px;height:36px;border:1px solid #dbe4ef;border-radius:9px;background:#fff;color:var(--blue);font-size:17px;transition:all .18s ease;flex:0 0 36px}
.hamb:hover{background:#edf5fb;border-color:#b9d5ea;transform:scale(1.04)}
.breadcrumb{display:flex;align-items:center;gap:12px;min-width:0;font-size:15.5px;color:#075b9d;font-weight:700}.breadcrumb .sep{color:#a2b2c6}.breadcrumb .school{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#183254}
.user{margin-left:auto;display:flex;align-items:center;gap:9px;font-weight:650;font-size:14px;padding:6px 12px;background:#f3f7fb;border-radius:99px;border:1px solid #e1eaf3;transition:all .18s}
.user:hover{background:#eaf3fa;border-color:#cfdfef}
.user i{color:var(--blue);font-size:18px}

.content{padding:30px;max-width:1600px;margin:auto}
.view{display:none}.view.active{display:block;animation:viewFadeIn .22s cubic-bezier(.16,1,.3,1) forwards}
@keyframes viewFadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.page-head{display:flex;align-items:flex-start;justify-content:space-between;gap:20px;margin-bottom:22px}
.page-title{margin:0;font-size:26px;font-weight:800;color:#122946;letter-spacing:-.2px}
.page-subtitle{margin:6px 0 0;color:var(--muted);font-size:14px}
.action-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}

/* Interactive Buttons */
.btn{border:1px solid var(--line);background:#fff;color:#1b2c45;padding:9px 15px;border-radius:10px;font-weight:700;font-size:13.5px;display:inline-flex;align-items:center;gap:8px;box-shadow:var(--shadow-sm);transition:all .18s cubic-bezier(.16,1,.3,1);position:relative;overflow:hidden;user-select:none}
.btn:hover{transform:translateY(-1.5px);box-shadow:0 6px 16px -2px rgba(20,45,80,.12);border-color:#b9cbdc}
.btn:active{transform:scale(.97)}
.btn i{font-size:13px;transition:transform .18s ease}
.btn:hover i{transform:scale(1.12)}
.btn.primary{background:linear-gradient(135deg,#005a9c 0%,#0877c9 100%);border-color:#005a9c;color:#fff;box-shadow:0 4px 14px rgba(0,90,156,.28)}
.btn.primary:hover{box-shadow:0 8px 22px rgba(0,90,156,.38);background:linear-gradient(135deg,#024e86 0%,#0a82db 100%)}
.btn.primary::after{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.24),transparent);transition:left .55s ease}
.btn.primary:hover::after{left:100%}
.btn.success{background:linear-gradient(135deg,#15803d,#16a34a);border-color:#15803d;color:#fff;box-shadow:0 4px 14px rgba(22,163,74,.25)}
.btn.danger{background:linear-gradient(135deg,#b91c1c,#dc2626);border-color:#b91c1c;color:#fff;box-shadow:0 4px 14px rgba(220,38,38,.25)}
.btn.purple{background:linear-gradient(135deg,#6d28d9,#7c3aed);border-color:#6d28d9;color:#fff;box-shadow:0 4px 14px rgba(124,58,237,.25)}
.btn.soft{background:#edf5fd;color:#075b9d;border-color:#cee2f2}
.btn.soft:hover{background:#e2effa;border-color:#b0d3ee;color:#004a84}
.btn.small{padding:6px 10.5px;font-size:12px;border-radius:8px}

/* Enhanced Stat Cards */
.stats-grid{display:grid;grid-template-columns:repeat(6,minmax(150px,1fr));gap:16px}
.stat-card{background:#fff;border:1px solid #e3ebf4;border-radius:14px;padding:20px 18px 18px;box-shadow:var(--shadow);min-height:150px;display:flex;flex-direction:column;justify-content:space-between;position:relative;transition:all .22s cubic-bezier(.16,1,.3,1);cursor:default}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3.5px;background:linear-gradient(90deg,#005a9c,#0877c9);opacity:0;border-radius:14px 14px 0 0;transition:opacity .22s}
.stat-card:hover{transform:translateY(-5px) scale(1.012);box-shadow:var(--shadow-lg);border-color:#bdd6ec}
.stat-card:hover::before{opacity:1}
.stat-card-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.stat-tag{font-size:10px;font-weight:800;letter-spacing:.4px;text-transform:uppercase;padding:3px 7px;border-radius:99px;background:#edf5fc;color:#0877c9;display:inline-flex;align-items:center;gap:4px}
.stat-icon-wrap{width:32px;height:32px;border-radius:9px;background:#edf5fc;color:#0877c9;display:grid;place-items:center;font-size:14px;transition:all .22s}
.stat-card:hover .stat-icon-wrap{transform:scale(1.12);background:var(--blue);color:#fff}
.stat-number{font-size:38px;line-height:1.1;font-weight:800;color:var(--blue);letter-spacing:-1px}
.stat-label{font-size:14px;font-weight:700;color:#2c3e56;margin-top:2px}
.stat-trend{font-size:11px;color:#7a8ba2;margin-top:7px;display:flex;align-items:center;gap:5px;font-weight:550}

.stat-card.orange::before{background:linear-gradient(90deg,#ea580c,#f97316)}
.stat-card.orange .stat-number{color:#ea580c}
.stat-card.orange .stat-tag, .stat-card.orange .stat-icon-wrap{background:#fff7ed;color:#ea580c}
.stat-card.orange:hover .stat-icon-wrap{background:#ea580c;color:#fff}

.stat-card.red::before{background:linear-gradient(90deg,#b91c1c,#dc2626)}
.stat-card.red .stat-number{color:#dc2626}
.stat-card.red .stat-tag, .stat-card.red .stat-icon-wrap{background:#fef2f2;color:#dc2626}
.stat-card.red:hover .stat-icon-wrap{background:#dc2626;color:#fff}

.stat-card.green::before{background:linear-gradient(90deg,#15803d,#16a34a)}
.stat-card.green .stat-number{color:#16a34a}
.stat-card.green .stat-tag, .stat-card.green .stat-icon-wrap{background:#f0fdf4;color:#16a34a}
.stat-card.green:hover .stat-icon-wrap{background:#16a34a;color:#fff}

.stat-card.purple::before{background:linear-gradient(90deg,#6d28d9,#7c3aed)}
.stat-card.purple .stat-number{color:#7c3aed}
.stat-card.purple .stat-tag, .stat-card.purple .stat-icon-wrap{background:#f5f3ff;color:#7c3aed}
.stat-card.purple:hover .stat-icon-wrap{background:#7c3aed;color:#fff}

/* Universal Floating Tooltip System - Dark Solid High Contrast with Arrow */
.ui-tooltip{
  position:fixed;
  z-index:999999;
  background:#0b192e;
  color:#ffffff !important;
  font-size:12px;
  font-weight:700;
  line-height:1.45;
  padding:8px 14px;
  border-radius:9px;
  box-shadow:0 12px 28px -2px rgba(4,14,28,.45), 0 0 0 1px rgba(255,255,255,.12);
  pointer-events:none;
  opacity:0;
  transform:scale(.92) translateY(3px);
  transition:opacity .15s cubic-bezier(.16,1,.3,1), transform .15s cubic-bezier(.16,1,.3,1);
  max-width:320px;
  white-space:normal;
  word-break:normal;
  text-align:center;
}
.ui-tooltip.visible{opacity:1;transform:scale(1) translateY(0)}
.ui-tooltip-content{display:block;position:relative;z-index:2;color:#ffffff !important}
.ui-tooltip-arrow{
  position:absolute;
  width:10px;
  height:10px;
  background:#0b192e;
  transform:rotate(45deg);
  z-index:1;
}
.ui-tooltip[data-placed="top"] .ui-tooltip-arrow{
  bottom:-5px;
  left:calc(50% - 5px);
  box-shadow:2px 2px 3px rgba(4,14,28,.2);
}
.ui-tooltip[data-placed="bottom"] .ui-tooltip-arrow{
  top:-5px;
  left:calc(50% - 5px);
  box-shadow:-2px -2px 3px rgba(4,14,28,.2);
}
.ui-tooltip[data-placed="left"] .ui-tooltip-arrow{
  right:-5px;
  top:calc(50% - 5px);
  box-shadow:2px -2px 3px rgba(4,14,28,.2);
}
.ui-tooltip[data-placed="right"] .ui-tooltip-arrow{
  left:-5px;
  top:calc(50% - 5px);
  box-shadow:-2px 2px 3px rgba(4,14,28,.2);
}

/* Card & Panels */
.card{background:#fff;border:1px solid #e1e9f2;border-radius:var(--radius);box-shadow:var(--shadow)}
.panel{margin-top:22px;padding:22px}
.panel-title{font-size:17.5px;font-weight:800;margin:0 0 16px;color:#152842}
.filters{display:grid;grid-template-columns:minmax(240px,1fr) 230px 230px;gap:12px}
.search-wrap{position:relative}
.search-wrap i{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:#8a9bb0;font-size:13.5px}
.search-wrap input{padding-left:38px}

.form-control,input:not([type="checkbox"]):not([type="radio"]),select,textarea{
  width:100%;
  border:1px solid #cbd7e6;
  border-radius:10px;
  background:#fbfcfe;
  padding:9px 12px;
  color:#18283f;
  outline:none;
  font-size:13.5px;
  transition:border-color .16s ease,box-shadow .16s ease,background .16s ease;
}
.form-control:hover,input:not([type="checkbox"]):not([type="radio"]):hover,select:hover,textarea:hover{
  border-color:#97b6d4;background:#fff;
}
.form-control:focus,input:focus,select:focus,textarea:focus{
  border-color:#0877c9;
  background:#fff;
  box-shadow:0 0 0 3.5px rgba(8,119,201,.14);
}
select{
  appearance:none;
  -webkit-appearance:none;
  padding-right:34px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 20 20'%3E%3Cpath fill='%23677a91' d='M5.6 7.4a1 1 0 0 1 1.4 0l3 3 3-3a1 1 0 1 1 1.4 1.4l-3.7 3.7a1 1 0 0 1-1.4 0L5.6 8.8a1 1 0 0 1 0-1.4Z'/%3E%3C/svg%3E");
  background-repeat:no-repeat;
  background-position:right 11px center;
}
textarea{min-height:92px;resize:vertical;line-height:1.45}.textarea-large{min-height:140px}
label{display:block;font-weight:750;font-size:12px;color:#29405d;margin:0 0 5px}
.hint,.field-help{font-size:11px;color:#788aa0;margin-top:4px}
.required{color:#dc2626;font-weight:800}
.counter{float:right;font-size:11px;color:#7b899c;font-weight:600}.counter.over{color:var(--red)}

/* Tables */
.table-wrap{overflow:auto;border:1px solid #e1e9f2;border-radius:12px;background:#fff}
table{width:100%;border-collapse:collapse;min-width:850px}
th,td{padding:12px 15px;border-bottom:1px solid #e9eff6;text-align:left;white-space:nowrap}
th{font-size:11.5px;text-transform:uppercase;letter-spacing:.5px;color:#5a6e87;background:#f8fafc;cursor:pointer;position:sticky;top:0;font-weight:750;user-select:none;transition:background .15s}
th:hover{background:#f1f5fa;color:var(--blue)}
td{font-size:13.5px;color:#20334d}
table tbody tr{transition:all .15s ease}
table tbody tr:hover{background:#f4f8fc;box-shadow:inset 3.5px 0 0 var(--blue)}

.badge{display:inline-flex;align-items:center;gap:6px;padding:4px 9px;border-radius:999px;font-size:11px;font-weight:800;transition:transform .15s}
.badge:hover{transform:scale(1.04)}
.badge.red{background:#fef2f2;color:#b91c1c;border:1px solid #fecaca}
.badge.yellow{background:#fffbeb;color:#b45309;border:1px solid #fde68a}
.badge.blue{background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe}
.badge.green{background:#f0fdf4;color:#15803d;border:1px solid #bbf7d0}
.badge.purple{background:#f5f3ff;color:#6d28d9;border:1px solid #ddd6fe}

/* Step Nav */
.form-layout{display:grid;grid-template-columns:230px minmax(0,1fr);gap:20px;align-items:start}
.step-nav{position:sticky;top:130px;padding:12px;display:grid;gap:5px}
.step-link{display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:9px;color:#546882;font-size:13px;font-weight:700;transition:all .16s ease}
.step-link:hover{background:#f0f5fb;color:var(--blue);transform:translateX(3px)}
.step-link .step-dot{width:24px;height:24px;border-radius:50%;border:1.5px solid #bdcedf;display:grid;place-items:center;background:#fff;color:var(--blue);font-size:11px;font-weight:800;flex:0 0 24px;transition:all .16s}
.step-link.active{background:#edf5fd;color:var(--blue);font-weight:800}
.step-link.active .step-dot{background:var(--blue);color:#fff;border-color:var(--blue);box-shadow:0 0 0 3px rgba(0,90,156,.18)}

.form-card{padding:0;overflow:hidden}
.form-toolbar{padding:14px 20px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,#fff,#fbfcfe);display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.form-toolbar .ficai-id{font-size:13px;color:#576980}
.form-section{padding:22px 22px 18px;border-bottom:1px solid #e8eff6;scroll-margin-top:130px}
.form-section:last-child{border-bottom:0}
.section-title{display:flex;align-items:center;gap:10px;margin:0 0 16px;font-size:16.5px;color:#133357;font-weight:800}
.section-number{width:28px;height:28px;background:#edf5fd;color:var(--blue);border-radius:8px;display:grid;place-items:center;font-size:12.5px;font-weight:800}

.grid{display:grid;gap:12px 14px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.g4{grid-template-columns:repeat(4,minmax(0,1fr))}.g5{grid-template-columns:repeat(5,minmax(0,1fr))}
.span2{grid-column:span 2}.span3{grid-column:span 3}.span4{grid-column:span 4}.span5{grid-column:span 5}
.meta-field{justify-self:start;width:100%}
.meta-year{max-width:118px}.meta-number{max-width:154px}

.inline-card{background:#f8fafc;border:1px solid #e1e9f2;border-radius:12px;padding:14px}
.inline-card h4{margin:0 0 11px;color:#284362;font-size:13.5px;font-weight:750}
.option-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 16px}
.option-grid.three{grid-template-columns:repeat(3,minmax(0,1fr))}
.check,.radio{display:flex;align-items:flex-start;gap:8px;font-size:12.5px;color:#243a57;line-height:1.35;cursor:pointer}
.check input,.radio input{margin-top:2px;accent-color:var(--blue);width:16px;height:16px;flex:0 0 16px;cursor:pointer}
.procedures{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 16px}
.procedure-row{display:grid;grid-template-columns:1fr 136px;gap:8px;align-items:center;padding:6px 0;border-bottom:1px dashed #dbe4ef}
.procedure-row:nth-last-child(-n+2){border-bottom:0}
.procedure-row input[type="date"]{height:34px;font-size:12px}

.radio-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.radio-card{border:1px solid #dce5f0;border-radius:10px;padding:11px 12px;display:flex;gap:9px;align-items:flex-start;background:#fff;cursor:pointer;transition:all .16s ease}
.radio-card:hover{border-color:#95badb;background:#f7faff;transform:translateY(-1px)}
.radio-card:has(input:checked){border-color:#0877c9;background:#f0f7fe;box-shadow:0 0 0 2px rgba(8,119,201,.18)}
.radio-card input{accent-color:var(--blue);margin-top:2px}
.radio-card strong{display:block;color:#1a314e;font-size:12.5px}
.radio-card small{color:#6c7d94;display:block;margin-top:3px;font-size:11px}

.option-card-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}
.option-add-btn{border:1px solid #c4ddf0;background:#fff;color:#0762a4;border-radius:8px;padding:6px 10px;font-size:11.5px;font-weight:750;display:inline-flex;align-items:center;gap:6px;cursor:pointer;transition:all .15s}
.option-add-btn:hover{background:#edf6fe;border-color:#7bb5dc;transform:translateY(-1px)}
.quick-add-panel{display:none;align-items:end;gap:9px;margin:0 0 13px;padding:10px;border:1px dashed #bad2e6;border-radius:10px;background:#f5faff}
.quick-add-panel.open{display:grid}
.quick-add-panel.situation{grid-template-columns:minmax(150px,.8fr) minmax(220px,1.2fr) auto auto}
.quick-add-panel.vulnerability{grid-template-columns:minmax(220px,1fr) auto auto}

.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{background:#edf5fc;color:#075b9d;border:1px solid #d0e4f3;padding:6px 10px;border-radius:999px;font-size:12px;font-weight:700;display:inline-flex;align-items:center;transition:all .15s}
.chip:hover{background:#e2f0fb;border-color:#b4d6ee}
.chip button{border:0;background:none;color:inherit;margin-left:5px;padding:0;cursor:pointer;font-size:14px}
.diagnosis-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.diagnosis-box{border:1px solid #dfe7f1;border-radius:12px;padding:13px 14px;background:#fbfcfe;transition:border-color .15s}
.diagnosis-box:hover{border-color:#b8d1ea;background:#fff}
.diagnosis-box h4{margin:0 0 10px;color:#183e66;font-size:13.5px;display:flex;align-items:center;gap:7px}
.diagnosis-box .check{margin:6px 0}
.form-footer{padding:16px 20px;background:#f9fbfd;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-top:1px solid #e5ebf3}

/* Config Tabs */
.config-tabs{display:flex;gap:6px;flex-wrap:wrap;padding:10px;border-bottom:1px solid var(--line)}
.config-tab{border:0;background:transparent;padding:9px 13px;border-radius:8px;font-weight:750;font-size:13px;color:#53667d;transition:all .16s}
.config-tab:hover{background:#f1f6fc;color:var(--blue)}
.config-tab.active{background:#edf5fc;color:var(--blue);box-shadow:0 2px 6px rgba(0,90,156,.08)}
.config-pane{display:none;padding:20px 22px 24px}
.config-pane.active{display:block;animation:viewFadeIn .18s ease}
.config-manager-head{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:15px}
.config-manager-head h3{margin:0 0 4px;font-size:17.5px;color:#102c50}
.config-manager-head p{margin:0;color:#6f8198;font-size:13px}
.config-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 0 13px;flex-wrap:wrap}
.config-search{position:relative;min-width:250px;max-width:430px;flex:1}
.config-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:#8a9bb0;font-size:12px}
.config-search input{height:36px;padding-left:34px;background:#f8fafc;border-color:#dce5ef}
.config-counter{font-size:11.5px;color:#6a7c93;font-weight:700;background:#f4f7fb;border:1px solid #dfe7f1;border-radius:999px;padding:5px 9px}

.config-table{width:100%;border-collapse:separate;border-spacing:0}
.config-table th{font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:#5f728b;background:#f8fafc;padding:10px 12px;border-bottom:1px solid #dfe7f0;text-align:left}
.config-table td{padding:10px 12px;border-bottom:1px solid #edf2f7;font-size:13px;color:#20344f;vertical-align:middle}
.config-table tr:last-child td{border-bottom:0}
.config-table tbody tr:hover td{background:#f8fbfe}
.config-table .actions-cell{width:100px;white-space:nowrap;text-align:right}
.icon-btn{width:30px;height:30px;border:1px solid #d8e2ee;background:#fff;color:#2c4c6d;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;cursor:pointer;margin-left:4px;transition:all .15s}
.icon-btn:hover{border-color:#90b7e2;color:var(--blue);background:#f2f8fe;transform:scale(1.06)}
.icon-btn.danger:hover{border-color:#fca5a5;color:#dc2626;background:#fef2f2}
.status-pill{display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:3.5px 8px;font-size:11px;font-weight:800;background:#f0fdf4;color:#15803d;border:1px solid #bbf7d0}
.status-pill.off{background:#f3f4f6;color:#6b7280;border-color:#e5e7eb}
.status-pill i{font-size:6.5px}

/* Modals */
.modal{position:fixed;inset:0;z-index:100;background:rgba(7,19,36,.68);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;padding:20px;animation:modalFadeIn .18s ease}
.modal.open{display:flex}
@keyframes modalFadeIn{from{opacity:0}to{opacity:1}}
.modal-card{background:#fff;width:min(95vw,1100px);max-height:94vh;border-radius:18px;overflow:hidden;box-shadow:0 25px 65px -10px rgba(5,18,38,.45),0 0 0 1px rgba(255,255,255,.1);animation:modalZoomIn .22s cubic-bezier(.16,1,.3,1) forwards}
@keyframes modalZoomIn{from{opacity:0;transform:scale(.96) translateY(6px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-head{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-bottom:1px solid var(--line)}
.modal-body{background:#edf2f7;padding:22px;max-height:calc(94vh - 60px);overflow:auto}
.close{border:0;background:#eef3f8;width:32px;height:32px;border-radius:8px;font-size:18px;display:grid;place-items:center;color:#4f637b;transition:all .15s}
.close:hover{background:#dc2626;color:#fff;transform:scale(1.08)}

/* Info Modal Premium Design - Idêntico à Imagem 1 */
.info-modal-card{width:min(96vw,1200px);max-height:95vh;border-radius:18px;background:#ebf1f8;overflow:hidden;border:1px solid rgba(255,255,255,.2);box-shadow:0 25px 70px -12px rgba(4,14,28,.5),0 0 0 1px rgba(200,215,235,.4)}
.info-modal-head{min-height:64px;padding:0 24px;background:linear-gradient(135deg,#0c2138 0%,#15365a 100%);color:#fff;display:flex;align-items:center;justify-content:space-between;gap:14px;border-bottom:1px solid rgba(255,255,255,.08)}
.info-modal-title{display:flex;align-items:center;gap:12px;font-size:17.5px;font-weight:750;color:#fff}
.info-modal-title i{font-size:18px;color:#8cb4dc}
.info-modal-title small{display:block;font-size:11px;font-weight:500;color:#8ea3bf;margin-top:2px}
.info-modal-head .action-row{display:flex;align-items:center;gap:8px}
.info-modal-head .btn.soft{background:rgba(255,255,255,.10);color:#ffffff;border:1px solid rgba(255,255,255,.20);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);font-weight:600;font-size:12.5px;padding:6.5px 12px;border-radius:8px;transition:all .16s ease}
.info-modal-head .btn.soft:hover{background:rgba(255,255,255,.22);border-color:rgba(255,255,255,.38);color:#fff;transform:translateY(-1px)}
.info-modal-head .close{background:rgba(255,255,255,.10);color:#ffffff;border:1px solid rgba(255,255,255,.20);border-radius:8px;width:32px;height:32px;font-size:16px;transition:all .16s ease}
.info-modal-head .close:hover{background:#dc2626;border-color:#dc2626;color:#fff}

.info-modal-body{background:#ebf1f8;padding:20px;max-height:calc(95vh - 64px);overflow-y:auto;display:flex;flex-direction:column;gap:14px}
.info-profile{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.info-student-card{background:#ffffff;border:1px solid #dbe5f0;border-radius:14px;padding:16px 20px;display:flex;align-items:center;gap:16px;box-shadow:0 2px 8px rgba(18,44,82,.04)}
.info-avatar{width:56px;height:56px;flex:0 0 56px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#1c436b,#081729);color:#ffffff;display:grid;place-items:center;font-size:19px;font-weight:800;border:1.5px solid rgba(255,255,255,.3);box-shadow:0 4px 12px rgba(8,25,48,.28);letter-spacing:.5px}
.info-student-name{font-size:19px;font-weight:800;color:#13243a}
.info-student-meta{font-size:13px;font-weight:550;color:#677b93;margin-top:3px}

.info-quick{background:#ffffff;border:1px solid #dbe5f0;border-radius:14px;padding:10px 12px;display:grid;grid-template-columns:repeat(2,1fr);gap:8px;box-shadow:0 2px 8px rgba(18,44,82,.04)}
.info-quick-item{background:#eef3f8;border:1px solid #dce5f0;border-radius:10px;padding:8px 12px;display:flex;flex-direction:column;justify-content:center}
.info-quick-item span{display:block;font-size:9.5px;text-transform:uppercase;letter-spacing:.6px;color:#677a90;font-weight:800;margin-bottom:2px}
.info-quick-item strong{font-size:13px;font-weight:750;color:#162b45}

.info-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.info-stack{display:flex;flex-direction:column;gap:12px}
.info-box{background:#ffffff;border:1px solid #dbe5f0;border-radius:12px;padding:14px 16px;box-shadow:0 2px 8px rgba(18,44,82,.03);display:flex;flex-direction:column;justify-content:center}
.info-box-title{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:0 0 9px;color:#18324e;font-size:10.5px;font-weight:800;text-transform:uppercase;letter-spacing:.5px}
.info-box-title i{color:#0877c9;font-size:12px}
.info-box p{margin:0;font-size:12.5px;color:#33445c;line-height:1.45}
.info-status{display:inline-flex;align-items:center;gap:7px;padding:5px 10px;border-radius:7px;background:#edf5fc;color:#075b9d;font-size:12px;font-weight:750;border:1px solid #d0e3f3}
.info-status i{font-size:11px}
.info-chip-list{display:flex;gap:6px;flex-wrap:wrap}
.info-chip{display:inline-flex;align-items:center;gap:5px;padding:5px 9px;border-radius:7px;border:1px solid #cde3f5;background:#f3f8fd;color:#075b9d;font-size:11.5px;font-weight:700}
.info-chip.alert{border-color:#fecaca;background:#fef2f2;color:#b91c1c}
.info-empty{font-size:12px;color:#7a8ca1;font-style:italic}
.info-actions-list{border:1px solid #dfe7f1;border-radius:9px;overflow:hidden;background:#f8fafc;padding:9px 12px;font-size:12px;color:#708197;font-style:italic}

.info-badge-history{background:#eef5fc;color:#0877c9;border:1px solid #d0e4f3;border-radius:99px;padding:3px 9px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.4px}
.timeline{position:relative;padding-left:12px}
.timeline-placeholder{font-size:12.5px;color:#708197;font-style:italic;padding:3px 0 3px 8px;border-left:2px solid #cbd7e6;margin:4px 0}
.timeline-item{position:relative;padding:0 0 12px 12px;border-left:2px solid #d8e3ef}.timeline-item:last-child{padding-bottom:0;border-left-color:transparent}.timeline-item:before{content:"";position:absolute;left:-6px;top:4px;width:10px;height:10px;border-radius:50%;background:#0877c9;border:2px solid #edf5fc;box-shadow:0 0 0 2px #b7d6ee}.timeline-top{display:flex;align-items:center;justify-content:space-between;gap:10px}.timeline-type{font-size:11.5px;font-weight:800;color:#005a9c}.timeline-date{font-size:10.5px;color:#78899f}.timeline-text{font-size:12px;color:#354963;line-height:1.45;margin-top:4px;white-space:pre-wrap}.timeline-by{font-size:10.5px;color:#8393a6;margin-top:4px}

.info-compose{background:#ffffff;border:1px solid #dbe5f0;border-radius:14px;padding:18px 20px;box-shadow:0 2px 8px rgba(18,44,82,.04)}
.info-compose-head{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;margin-bottom:12px}
.info-compose-head h3{margin:0;color:#13243a;font-size:14px;font-weight:800;display:flex;align-items:center;gap:7px}
.info-compose-head h3 i{color:#0877c9}
.info-compose-head p{margin:3px 0 0;color:#677b93;font-size:11.5px}
.badge-gold{background:linear-gradient(135deg,#c4a260 0%,#87662b 100%);color:#ffffff;font-size:10.5px;font-weight:750;padding:4px 13px;border-radius:99px;box-shadow:0 2px 8px rgba(135,102,43,.28),inset 0 1px 0 rgba(255,255,255,.35);display:inline-flex;align-items:center;gap:5px;letter-spacing:.3px}
.info-compose-grid{display:grid;grid-template-columns:140px 220px 1fr;gap:10px}
.info-compose input,.info-compose select,.info-compose textarea{background:#f8fafc;border:1px solid #cbd7e6;border-radius:10px;padding:8px 12px;font-size:13px;color:#18283f;font-weight:600;font-family:var(--font);transition:all .15s}
.info-compose input:focus,.info-compose select:focus,.info-compose textarea:focus{border-color:#0877c9;background:#fff;box-shadow:0 0 0 3px rgba(8,119,201,.12)}
.info-compose textarea{width:100%;min-height:78px;margin-top:10px;line-height:1.45;resize:vertical;font-weight:400}
.info-compose-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:12px}
.audit-note{display:flex;align-items:center;gap:7px;color:#677b93;font-size:11px;font-weight:550}
.audit-note i{color:#16a34a}
.btn-navy-submit{background:linear-gradient(135deg,#071a2f 0%,#112f54 100%);border:1px solid #071a2f;color:#ffffff !important;font-weight:750;font-size:12.5px;padding:9px 18px;border-radius:10px;box-shadow:0 6px 18px rgba(7,26,47,.35),0 0 0 1px rgba(255,255,255,.08);display:inline-flex;align-items:center;gap:7px;transition:all .18s ease;cursor:pointer}
.btn-navy-submit:hover{background:linear-gradient(135deg,#0b2645 0%,#184172 100%);transform:translateY(-1.5px);box-shadow:0 8px 24px rgba(7,26,47,.45)}
.btn-navy-submit:active{transform:scale(.97)}

/* Dark Mode */
body.dark{--bg:#0c121d;--card:#141c2a;--text:#e8eef6;--muted:#99a9bd;--line:#263447;--shadow:0 10px 28px rgba(0,0,0,.35),0 0 0 1px #223043;--shadow-lg:0 20px 40px rgba(0,0,0,.5),0 0 0 1px #293a52}
body.dark .sidebar,body.dark .topbar,body.dark .stat-card,body.dark .card,body.dark .form-control,body.dark input,body.dark select,body.dark textarea,body.dark .radio-card,body.dark .table-wrap,body.dark .info-box,body.dark .info-student-card,body.dark .info-quick,body.dark .info-compose{background:#141d2c;color:#e8eef6;border-color:#253448}
body.dark .nav-item{color:#c5d4e6}body.dark .nav-item.active,body.dark .nav-item:hover{background:#1d293d}.dark .form-control,.dark input,.dark select,.dark textarea{color:#edf4ff}.dark th{background:#192436;color:#bac8d9}.dark td{border-color:#223043}.dark .inline-card,.dark .diagnosis-box,.dark .form-footer,.dark .info-quick-item,.dark .info-action-row{background:#111824;border-color:#253448}.dark label,.dark .radio-card strong{color:#dce7f5}
body.dark .stat-card-head .stat-icon-wrap{background:#1e2c3e;color:#58a9e8}
body.dark .header-icon-btn,body.dark .hamb,body.dark .user{background:#141d2c;border-color:#28384d;color:#7bbdec}
body.dark .btn{background:#182233;border-color:#2b3c54;color:#e1eaf5}
body.dark .btn.soft{background:#1b2d42;color:#6db7f2;border-color:#2a4563}
body.dark .ui-tooltip{background:#1e293b;border:1px solid rgba(255,255,255,.2);box-shadow:0 12px 30px rgba(0,0,0,.6)}
body.dark .ui-tooltip-arrow{background:#1e293b}

@media(max-width:1250px){.stats-grid{grid-template-columns:repeat(3,1fr)}.g5{grid-template-columns:repeat(3,1fr)}.span5{grid-column:span 3}}
@media(max-width:980px){.app-shell,.app-shell.sidebar-collapsed{grid-template-columns:1fr}.sidebar{position:fixed;left:-290px;width:280px;transition:.2s;box-shadow:10px 0 30px rgba(0,0,0,.25)}.sidebar.open{left:0}.app-shell.sidebar-collapsed .brand{justify-content:flex-start;padding:0 26px}.app-shell.sidebar-collapsed .brand-full{display:inline}.app-shell.sidebar-collapsed .brand-short{display:none}.app-shell.sidebar-collapsed .menu-section-title,.app-shell.sidebar-collapsed .menu-divider,.app-shell.sidebar-collapsed .sidebar-footer{display:block}.app-shell.sidebar-collapsed .nav-item{justify-content:flex-start;gap:13px;padding:12px 22px;border-left-width:4px}.app-shell.sidebar-collapsed .nav-item .nav-label{display:inline}.app-shell.sidebar-collapsed .nav-item i{width:22px;font-size:16.5px}.top-row{padding:0 18px}.bottom-row{padding:0 18px}.header-links a{display:none}.content{padding:18px}.form-layout{grid-template-columns:1fr}.step-nav{display:none}.g4,.g5{grid-template-columns:repeat(2,1fr)}.span4,.span5{grid-column:span 2}.diagnosis-grid{grid-template-columns:1fr}}
@media(max-width:700px){.stats-grid{grid-template-columns:repeat(2,1fr);gap:12px}.stat-card{padding:16px 12px;min-height:120px}.stat-number{font-size:32px}.filters,.g2,.g3,.g4,.g5,.option-grid,.option-grid.three,.procedures,.radio-cards,.quick-add-panel.situation,.quick-add-panel.vulnerability{grid-template-columns:1fr}.span2,.span3,.span4,.span5{grid-column:span 1}.page-head{flex-direction:column}.form-section{padding:18px 14px}.brand{height:84px}}

/* Print A4 */
#printSheet{display:none}
.print-page{width:210mm;height:297mm;background:#fff;color:#111;padding:8mm 8.5mm 6.5mm;font-family:Arial,sans-serif;font-size:6.3pt;line-height:1.13;overflow:hidden;box-sizing:border-box}
.p-header{display:grid;grid-template-columns:1fr 1.2fr .8fr;align-items:start;gap:4mm;margin-bottom:2mm}.p-brand{display:flex;gap:2.5mm;align-items:flex-start}.p-crest{width:16mm;height:18mm;object-fit:contain}.p-inst{font-size:6.5pt;line-height:1.2;text-transform:uppercase;margin-top:.8mm}.p-title{text-align:center;font-weight:800;font-size:8.2pt;margin-top:13mm}.p-number{text-align:right;font-size:8pt;margin-top:11mm}.p-sec{margin-top:1.3mm}.p-sec-title{font-weight:800;font-size:8.4pt;margin:0 0 .8mm}.p-row{display:flex;gap:2mm;align-items:flex-end;min-height:4.2mm}.p-field{display:flex;gap:1.2mm;align-items:flex-end;min-width:0;flex:1}.p-label{font-weight:700;white-space:nowrap}.p-line{border-bottom:.22mm solid #111;min-height:3.3mm;flex:1;padding:0 .8mm .4mm;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.p-box{width:3mm;height:3mm;border:.22mm solid #111;display:inline-grid;place-items:center;font-size:6pt;line-height:1}.p-check{display:flex;align-items:flex-start;gap:1.1mm;margin:.55mm 0}.p-check span:last-child{flex:1}.p-cols2{display:grid;grid-template-columns:1fr 1fr;gap:3.4mm}.p-cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:2mm}.p-txtlines{border-bottom:.22mm solid #111;min-height:4mm;margin:.5mm 0;overflow:hidden}.p-txtlines.two{min-height:7.8mm}.p-small{font-size:5.7pt}.p-sign{text-align:center;margin-left:auto;width:84mm;border-top:.22mm solid #111;padding-top:.7mm}.p-footer{display:flex;justify-content:space-between;align-items:flex-end;margin-top:1mm;font-size:5.4pt;color:#333}.p-diagnosis{display:grid;grid-template-columns:repeat(3,1fr);gap:1.8mm}.p-diag{border:.18mm solid #aaa;padding:1mm}.p-diag b{display:block;margin-bottom:.5mm}.p-ellipsis{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2;overflow:hidden;white-space:normal}.p-ctgrid{display:grid;grid-template-columns:1.5fr .5fr;gap:2mm}.p-prom{display:grid;grid-template-columns:1fr 40mm;gap:1mm 3mm}.p-muted{color:#444}
@media print{
  @page{size:A4 portrait;margin:0}
  html,body{width:210mm;height:297mm;margin:0!important;padding:0!important;background:#fff!important;overflow:hidden!important}
  body > .app-shell, body > .modal, body > #toast, body > .ui-tooltip{display:none!important}
  #printSheet{display:block!important;position:fixed;left:0;top:0;width:210mm;height:297mm;margin:0!important;padding:0!important;overflow:hidden!important}
  .print-page{display:block!important;position:absolute;left:0;top:0;width:210mm!important;height:297mm!important;box-shadow:none!important;margin:0!important;page-break-before:avoid!important;page-break-after:avoid!important;page-break-inside:avoid!important;break-inside:avoid!important;overflow:hidden!important}
}

/* ==============================================================================
   CONTROLE DE EVASÕES / FREQUÊNCIA - NOVO LAYOUT SPLIT (SEI / FICAI STYLE)
   ============================================================================== */
.dash-panel {
  background: var(--card-bg, #ffffff);
  border: 1px solid var(--card-border, #e2e8f0);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05);
}

.dash-panel-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.dash-panel-title {
  font-size: 18px;
  font-weight: 700;
  color: #0b1f38;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin: 0;
  cursor: pointer;
  user-select: none;
}

.dash-panel-title i {
  color: var(--blue, #0877c9);
  font-size: 15px;
}

/* Barra de Filtros Superior */
.dash-filters-bar {
  display: grid;
  grid-template-columns: 1fr 180px 180px 190px;
  gap: 12px;
  margin-bottom: 24px;
}

@media (max-width: 1024px) {
  .dash-filters-bar {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 640px) {
  .dash-filters-bar {
    grid-template-columns: 1fr;
  }
}

.dash-search-box {
  position: relative;
  display: flex;
  align-items: center;
}

.dash-search-box i {
  position: absolute;
  left: 14px;
  color: #94a3b8;
  font-size: 14px;
  pointer-events: none;
}

.dash-input {
  width: 100%;
  height: 42px;
  padding: 0 14px 0 38px;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  background: #ffffff;
  font-family: 'Alexandria', sans-serif;
  font-size: 13px;
  color: #1e293b;
  outline: none;
  transition: all 0.2s ease;
}

.dash-input:focus {
  border-color: #0877c9;
  box-shadow: 0 0 0 3px rgba(8, 119, 201, 0.12);
}

.dash-select-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.dash-select-wrap .dash-date-icon {
  position: absolute;
  left: 14px;
  color: #64748b;
  font-size: 14px;
  pointer-events: none;
  z-index: 1;
}

.dash-select {
  width: 100%;
  height: 42px;
  padding: 0 30px 0 12px;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  background: #ffffff;
  font-family: 'Alexandria', sans-serif;
  font-size: 12.5px;
  font-weight: 500;
  color: #334155;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.dash-select.has-icon {
  padding-left: 36px;
}

.dash-select:focus {
  border-color: #0877c9;
  box-shadow: 0 0 0 3px rgba(8, 119, 201, 0.12);
}

.select-chevron {
  position: absolute;
  right: 12px;
  color: #64748b;
  font-size: 10px;
  pointer-events: none;
}

/* Grid Duas Colunas */
.dash-split-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 900px) {
  .dash-split-grid {
    grid-template-columns: 1fr;
  }
}

.dash-split-card {
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  background: #ffffff;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: box-shadow 0.2s ease;
}

.dash-split-card:hover {
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.04);
}

.dash-split-head {
  padding: 14px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #f1f5f9;
  background: #ffffff;
}

.dash-split-title-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.dash-split-icon-badge {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
}

.dash-split-icon-badge.ct-icon {
  background: #e0f2fe;
  color: #0284c7;
}

.dash-split-icon-badge.gerados-icon {
  background: #e0f2fe;
  color: #0284c7;
}

.dash-split-title {
  font-size: 15px;
  font-weight: 700;
  color: #0f172a;
}

.dash-split-counter {
  font-size: 12px;
  color: #64748b;
  font-weight: 500;
}

/* Tabela interna da lista */
.dash-list-table {
  display: flex;
  flex-direction: column;
}

.dash-list-thead {
  padding: 10px 18px;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  align-items: center;
  gap: 14px;
}

.dash-col-header {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #0877c9;
}

.dash-list-tbody {
  display: flex;
  flex-direction: column;
}

.dash-list-row {
  padding: 12px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid #f1f5f9;
  transition: background 0.15s ease, transform 0.15s ease;
  min-height: 48px;
}

.dash-list-row:last-child {
  border-bottom: none;
}

.dash-list-row:hover {
  background: #f8fafc;
}

/* Checkboxes Customizados */
.custom-check-wrap {
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  margin: 0;
}

.custom-check-wrap input[type="checkbox"] {
  width: 17px;
  height: 17px;
  border-radius: 4px;
  border: 1.5px solid #94a3b8;
  cursor: pointer;
  accent-color: #0877c9;
}

/* Ícones de Status das Linhas */
.dash-row-status-icon {
  width: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  flex-shrink: 0;
}

.dash-row-status-icon.alert-warn {
  color: #f59e0b;
}

.dash-row-status-icon.tag-green {
  color: #10b981;
}

.dash-row-status-icon.tag-blue {
  color: #0284c7;
}

.dash-row-status-icon.tag-purple {
  color: #8b5cf6;
}

.dash-row-status-icon.tag-gray {
  color: #64748b;
}

.dash-row-content {
  flex: 1;
  min-width: 0;
}

.dash-item-link {
  font-size: 13px;
  font-weight: 550;
  color: #1e293b;
  text-decoration: none;
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
  transition: color 0.15s ease, transform 0.15s ease;
}

.dash-item-link strong {
  font-weight: 700;
  color: #0f172a;
}

.dash-item-link:hover {
  color: #0877c9;
  text-decoration: underline;
  transform: translateX(2px);
}

/* Dark Mode para o Split Layout */
body.dark-mode .dash-panel,
body.dark-mode .dash-split-card,
body.dark-mode .dash-split-head {
  background: #111e2e;
  border-color: #1e2f47;
}
body.dark-mode .dash-list-thead {
  background: #0b1624;
  border-color: #1e2f47;
}
body.dark-mode .dash-list-row {
  border-color: #1a293d;
}
body.dark-mode .dash-list-row:hover {
  background: #162438;
}
body.dark-mode .dash-input,
body.dark-mode .dash-select {
  background: #0d1a29;
  border-color: #1e334d;
  color: #e2e8f0;
}
body.dark-mode .dash-panel-title,
body.dark-mode .dash-split-title,
body.dark-mode .dash-item-link strong {
  color: #f1f5f9;
}
body.dark-mode .dash-item-link {
  color: #cbd5e1;
}
body.dark-mode .dash-item-link:hover {
  color: #38bdf8;
}

/* Auto Number FICAI */
.auto-num-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  border-radius: 99px;
  font-size: 10.5px;
  font-weight: 700;
  background: #e0f2fe;
  color: #0284c7;
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
  border: 1px solid #bae6fd;
}
.auto-num-badge:hover {
  background: #0284c7;
  color: #ffffff;
  transform: scale(1.04);
  box-shadow: 0 2px 8px rgba(2, 132, 199, 0.25);
}
.input-with-action {
  position: relative;
  display: flex;
  align-items: center;
}
.input-with-action input {
  width: 100%;
  padding-right: 38px !important;
}
.btn-input-icon {
  position: absolute;
  right: 6px;
  width: 28px;
  height: 28px;
  border: none;
  background: transparent;
  color: #0877c9;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}
.btn-input-icon:hover {
  background: #edf5fc;
  color: #005a9c;
  transform: rotate(180deg);
}
body.dark-mode .auto-num-badge {
  background: #0c4a6e;
  border-color: #0369a1;
  color: #7dd3fc;
}
body.dark-mode .btn-input-icon:hover {
  background: #1e2f47;
  color: #38bdf8;
}
</style>"""

# Replace head style
html = re.sub(r'<title>.*?</title>.*?<style>.*?</style>', style_replacement, html, flags=re.DOTALL)

# 2. Update navigation with tooltips
nav_replacements = [
    ('data-view="dashboard"', 'data-view="dashboard" data-tooltip="Visão consolidada de indicadores, gráficos e atividade recente" data-tooltip-pos="right"'),
    ('data-view="gerar"', 'data-view="gerar" data-tooltip="Abertura de ficha, diagnóstico escolar e emissão oficial A4" data-tooltip-pos="right"'),
    ('data-view="dados"', 'data-view="dados" data-tooltip="Consulta de todas as FICAIs cadastradas e histórico detalhado" data-tooltip-pos="right"'),
    ('data-view="rae"', 'data-view="rae" data-tooltip="Fluxo bidirecional e notificações de devolutivas da rede" data-tooltip-pos="right"'),
    ('data-view="conselho"', 'data-view="conselho" data-tooltip="Painel do Conselho Tutelar e acompanhamento de diligências" data-tooltip-pos="right"'),
    ('data-view="encerramento"', 'data-view="encerramento" data-tooltip="Arquivamento formal e conclusão de casos resolvidos" data-tooltip-pos="right"'),
    ('data-view="config"', 'data-view="config" data-tooltip="Gestão de escolas, turmas, usuários e tabelas auxiliares" data-tooltip-pos="right"'),
    ('data-view="sobre"', 'data-view="sobre" data-tooltip="Diretrizes legais e informações do sistema FICAI 4.0" data-tooltip-pos="right"')
]
for old_s, new_s in nav_replacements:
    html = html.replace(old_s, new_s, 1)

# 3. Update topbar buttons
topbar_replacements = [
    ('<button id="darkToggle" title="Modo noturno"><i class="fa-solid fa-moon"></i></button>', '<button id="darkToggle" class="header-icon-btn" data-tooltip="Alternar tema Claro / Escuro (Alt+D)"><i class="fa-solid fa-moon"></i></button>'),
    ('<button title="Notificações"><i class="fa-solid fa-comments" style="color:green"></i></button>', '<button class="header-icon-btn notification-btn" data-tooltip="3 devolutivas recentes do Conselho Tutelar"><i class="fa-solid fa-bell"></i><span class="pulse-badge"></span></button>'),
    ('id="hamb" type="button" title="Recolher menu lateral" aria-label="Recolher menu lateral" aria-expanded="true"', 'id="hamb" type="button" data-tooltip="Recolher ou expandir menu lateral" aria-label="Recolher menu lateral" aria-expanded="true"')
]
for old_s, new_s in topbar_replacements:
    html = html.replace(old_s, new_s, 1)

# 4. Update Stat Cards in Dashboard
old_stats_grid = """  <div class="stats-grid">
    <div class="stat-card"><div class="stat-number">24</div><div class="stat-label">Casos Ativos</div></div>
    <div class="stat-card"><div class="stat-number">45%</div><div class="stat-label">Falta de motivação</div></div>
    <div class="stat-card orange"><div class="stat-number">30%</div><div class="stat-label">Trabalho familiar</div></div>
    <div class="stat-card red"><div class="stat-number">15%</div><div class="stat-label">Doença / Saúde</div></div>
    <div class="stat-card"><div class="stat-number">71</div><div class="stat-label">Alunos Desistentes</div></div>
    <div class="stat-card green"><div class="stat-number">138</div><div class="stat-label">FICAI Finalizadas</div></div>
  </div>"""

new_stats_grid = """  <div class="stats-grid">
    <div class="stat-card" data-tooltip="Fichas em andamento que demandam intervenção pedagógica ou busca ativa">
      <div class="stat-card-head"><span class="stat-tag"><i class="fa-solid fa-bolt"></i> Ativo</span><div class="stat-icon-wrap"><i class="fa-solid fa-folder-open"></i></div></div>
      <div class="stat-number">24</div>
      <div class="stat-label">Casos Ativos</div>
      <div class="stat-trend"><i class="fa-solid fa-arrow-trend-up"></i> +2 registrados esta semana</div>
    </div>
    <div class="stat-card" data-tooltip="Principal motivo diagnosticado nos relatos escolares e visitas às famílias">
      <div class="stat-card-head"><span class="stat-tag"><i class="fa-solid fa-chart-pie"></i> Principal</span><div class="stat-icon-wrap"><i class="fa-solid fa-heart-crack"></i></div></div>
      <div class="stat-number">45%</div>
      <div class="stat-label">Falta de motivação</div>
      <div class="stat-trend"><i class="fa-solid fa-circle-info"></i> Maior incidência no 7º e 8º ano</div>
    </div>
    <div class="stat-card orange" data-tooltip="Casos em que o estudante auxilia no sustento da família ou cuidados domésticos">
      <div class="stat-card-head"><span class="stat-tag"><i class="fa-solid fa-triangle-exclamation"></i> Social</span><div class="stat-icon-wrap"><i class="fa-solid fa-briefcase"></i></div></div>
      <div class="stat-number">30%</div>
      <div class="stat-label">Trabalho familiar</div>
      <div class="stat-trend"><i class="fa-solid fa-triangle-exclamation"></i> Requer encaminhamento ao CRAS</div>
    </div>
    <div class="stat-card red" data-tooltip="Infrequência gerada por problemas clínicos, internações ou tratamento contínuo">
      <div class="stat-card-head"><span class="stat-tag"><i class="fa-solid fa-notes-medical"></i> Saúde</span><div class="stat-icon-wrap"><i class="fa-solid fa-heart-pulse"></i></div></div>
      <div class="stat-number">15%</div>
      <div class="stat-label">Doença / Saúde</div>
      <div class="stat-trend"><i class="fa-solid fa-hospital"></i> Articulação com Rede de Saúde</div>
    </div>
    <div class="stat-card" data-tooltip="Alunos sem comparecimento há mais de 15 dias consecutivos">
      <div class="stat-card-head"><span class="stat-tag"><i class="fa-solid fa-person-walking"></i> Alerta</span><div class="stat-icon-wrap"><i class="fa-solid fa-user-xmark"></i></div></div>
      <div class="stat-number">71</div>
      <div class="stat-label">Alunos Desistentes</div>
      <div class="stat-trend"><i class="fa-solid fa-magnifying-glass"></i> Em processo de busca ativa</div>
    </div>
    <div class="stat-card green" data-tooltip="Casos solucionados com reintegração do aluno à escola e frequência normalizada">
      <div class="stat-card-head"><span class="stat-tag"><i class="fa-solid fa-check"></i> Sucesso</span><div class="stat-icon-wrap"><i class="fa-solid fa-circle-check"></i></div></div>
      <div class="stat-number">138</div>
      <div class="stat-label">FICAI Finalizadas</div>
      <div class="stat-trend"><i class="fa-solid fa-shield-halved"></i> Casos regularizados em 2026</div>
    </div>
  </div>"""

html = html.replace(old_stats_grid, new_stats_grid, 1)

# 5. Add tooltips to buttons
btn_replacements = [
    ('data-go="gerar"><i class="fa-solid fa-plus"></i> Nova FICAI</button>', 'data-go="gerar" data-tooltip="Iniciar novo preenchimento e cadastro de FICAI"><i class="fa-solid fa-plus"></i> Nova FICAI</button>'),
    ('id="loadDemo"><i class="fa-solid fa-wand-magic-sparkles"></i> Carregar exemplo</button>', 'id="loadDemo" data-tooltip="Preencher formulário com dados demonstrativos para teste rápido"><i class="fa-solid fa-wand-magic-sparkles"></i> Carregar exemplo</button>'),
    ('id="topPreview"><i class="fa-solid fa-file-pdf"></i> Visualizar A4</button>', 'id="topPreview" data-tooltip="Abrir pré-visualização do espelho oficial A4 para impressão"><i class="fa-solid fa-file-pdf"></i> Visualizar A4</button>'),
    ('id="openCurrentInfo"><i class="fa-solid fa-circle-info"></i> Informações</button>', 'id="openCurrentInfo" data-tooltip="Ver histórico completo, linha do tempo e ocorrências"><i class="fa-solid fa-circle-info"></i> Informações</button>'),
    ('id="saveDraft"><i class="fa-solid fa-floppy-disk"></i> Salvar rascunho</button>', 'id="saveDraft" data-tooltip="Gravar dados temporários no navegador para não perder o preenchimento"><i class="fa-solid fa-floppy-disk"></i> Salvar rascunho</button>'),
    ('id="clearDraft"><i class="fa-solid fa-eraser"></i> Limpar</button>', 'id="clearDraft" data-tooltip="Limpar todos os campos do formulário"><i class="fa-solid fa-eraser"></i> Limpar</button>'),
    ('id="newStudentBtn"><i class="fa-solid fa-user-plus"></i> Novo</button>', 'id="newStudentBtn" data-tooltip="Cadastrar novo aluno na base do sistema"><i class="fa-solid fa-user-plus"></i> Novo</button>'),
    ('id="saveBottom"><i class="fa-solid fa-floppy-disk"></i> Salvar FICAI</button>', 'id="saveBottom" data-tooltip="Salvar ficha no banco de dados e cadastrar histórico"><i class="fa-solid fa-floppy-disk"></i> Salvar FICAI</button>'),
    ('id="printBtn"><i class="fa-solid fa-print"></i> Imprimir / Salvar PDF</button>', 'id="printBtn" data-tooltip="Gerar documento oficial em PDF (A4 - 1 página retrato)"><i class="fa-solid fa-print"></i> Imprimir / Salvar PDF</button>'),
    ('id="previewBtn"><i class="fa-solid fa-eye"></i> Pré-visualizar A4</button>', 'id="previewBtn" data-tooltip="Conferir espelho A4 antes de imprimir"><i class="fa-solid fa-eye"></i> Pré-visualizar A4</button>'),
    ('<span class="badge green"><i class="fa-solid fa-database"></i> Salva no histórico</span>', '<span class="badge-gold">Salva no histórico</span>'),
    ('<button class="btn primary" type="button" id="saveInfoEntry"><i class="fa-solid fa-plus"></i> Adicionar ao histórico</button>', '<button class="btn-navy-submit" type="button" id="saveInfoEntry"><i class="fa-solid fa-plus"></i> Adicionar ao histórico</button>'),
    ('<span class="badge blue" id="infoHistoryCount">0 registros</span>', '<span class="info-badge-history" id="infoHistoryCount">0 REGISTROS</span>'),
    ('id="infoModalNumber">Consulta e acompanhamento do caso</small>', 'id="infoModalNumber">00021/2026 · acompanhamento de caso</small>')
]
for old_s, new_s in btn_replacements:
    html = html.replace(old_s, new_s, 1)

# Ajuste no JS de renderização do modal para layout da Imagem 1
html = html.replace(
    "const meta=[r.turma,d.turno,r.escola].filter(Boolean);$('#infoStudentMeta').textContent=meta.join(' · ')||'Dados cadastrais da FICAI';",
    "$('#infoStudentMeta').textContent=r.turma||d.turma||'7º Ano B';"
)

html = html.replace(
    "$('#infoHistoryCount').textContent=`${entries.length} registro${entries.length===1?'':'s'}`;",
    "$('#infoHistoryCount').textContent=`${entries.length} REGISTRO${entries.length===1?'':'S'}`;"
)

html = html.replace(
    "$('#infoModalNumber').textContent=`${r.numero||'FICAI'} · acompanhamento do caso`;",
    "$('#infoModalNumber').textContent=`${r.numero||'00021/2026'} · acompanhamento de caso`;"
)

html = html.replace(
    "if(!rows.length)return '<div class=\"info-empty\" style=\"padding:10px\">Nenhum procedimento registrado.</div>';",
    "if(!rows.length)return '<div class=\"info-empty\" style=\"padding:2px 0\">Nenhum procedimento registrado.</div>';"
)

# 7. Update Dashboard "Controle de Evasões / Frequência" to the new 2-column split layout (Recebidos CT & Gerados)
old_dashboard_card = """  <div class="card panel">
    <h2 class="panel-title">Controle de Evasões / Frequência</h2>
    <div class="filters"><div class="search-wrap"><i class="fa-solid fa-magnifying-glass"></i><input id="dashSearch" class="form-control" placeholder="Buscar aluno na atividade recente..."></div><select class="form-control"><option>Todas as Turmas</option><option>6º Ano A</option><option>7º Ano B</option><option>9º Ano A</option></select><select class="form-control"><option>Todas as Situações</option><option>Alerta de evasão</option><option>Em análise</option><option>No Conselho</option><option>Retorno</option></select></div>
    <div style="margin-top:18px" class="table-wrap"><table id="dashTable"><thead><tr><th>Aluno</th><th>Turma</th><th>Última ocorrência</th><th>Situação</th><th>Ações</th></tr></thead><tbody>
      <tr><td>Ana Clara Nascimento</td><td>7º Ano B</td><td>18/08/2026</td><td><span class="badge red">Alerta crítico</span></td><td><button class="btn small soft" data-go="dados">Abrir</button></td></tr>
      <tr><td>Bruno Henrique Silva</td><td>6º Ano A</td><td>17/08/2026</td><td><span class="badge yellow">Aviso de faltas</span></td><td><button class="btn small soft" data-go="dados">Abrir</button></td></tr>
      <tr><td>Carla Souza Ribeiro</td><td>9º Ano A</td><td>16/08/2026</td><td><span class="badge purple">No Conselho</span></td><td><button class="btn small purple" data-go="conselho">Ver CT</button></td></tr>
      <tr><td>Diego Santos Alves</td><td>8º Ano C</td><td>15/08/2026</td><td><span class="badge green">Retorno</span></td><td><button class="btn small soft" data-go="encerramento">Encerrar</button></td></tr>
    </tbody></table></div>
  </div>"""

new_dashboard_card = """  <div class="dash-panel card">
    <div class="dash-panel-header">
      <h2 class="dash-panel-title" id="dashPanelTitle" data-tooltip="Clique para redefinir filtros ou focar na pesquisa">
        <i class="fa-solid fa-filter"></i> Controle de Evasões / Frequência
      </h2>
    </div>

    <!-- Barra de Filtros Superior -->
    <div class="dash-filters-bar">
      <div class="dash-search-box">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input id="dashSearch" type="text" placeholder="Buscar aluno, documento ou responsável..." class="dash-input" data-tooltip="Filtre instantaneamente por aluno, número ou turma">
      </div>
      <div class="dash-select-wrap">
        <select id="dashTurmaFilter" class="dash-select" data-tooltip="Filtrar por turma">
          <option value="">Todas as Turmas</option>
          <option value="6A">6º Ano A (6A)</option>
          <option value="7B">7º Ano B (7B)</option>
          <option value="8C">8º Ano C (8C)</option>
          <option value="9A">9º Ano A (9A)</option>
        </select>
        <i class="fa-solid fa-chevron-down select-chevron"></i>
      </div>
      <div class="dash-select-wrap">
        <select id="dashSituacaoFilter" class="dash-select" data-tooltip="Filtrar por situação do caso">
          <option value="">Todas as Situações</option>
          <option value="Alerta crítico">Alerta crítico</option>
          <option value="Aviso de faltas">Aviso de faltas</option>
          <option value="No Conselho">No Conselho</option>
          <option value="Retorno">Retorno</option>
        </select>
        <i class="fa-solid fa-chevron-down select-chevron"></i>
      </div>
      <div class="dash-select-wrap">
        <i class="fa-regular fa-calendar dash-date-icon"></i>
        <select id="dashPeriodoFilter" class="dash-select has-icon" data-tooltip="Filtrar por período temporal">
          <option value="30">Últimos 30 dias</option>
          <option value="7">Últimos 7 dias</option>
          <option value="15">Últimos 15 dias</option>
          <option value="90">Últimos 90 dias</option>
          <option value="ano">Ano Letivo 2026</option>
        </select>
        <i class="fa-solid fa-chevron-down select-chevron"></i>
      </div>
    </div>

    <!-- Grid Duas Colunas: Recebidos CT e Gerados -->
    <div class="dash-split-grid">
      <!-- Coluna 1: Recebidos CT -->
      <div class="dash-split-card">
        <div class="dash-split-head">
          <div class="dash-split-title-group">
            <div class="dash-split-icon-badge ct-icon">
              <i class="fa-solid fa-inbox"></i>
            </div>
            <strong class="dash-split-title">Recebidos CT</strong>
          </div>
          <span class="dash-split-counter" id="countRecebidosCT">Documentos recebidos (1 registro)</span>
        </div>
        
        <div class="dash-list-table">
          <div class="dash-list-thead">
            <label class="custom-check-wrap" data-tooltip="Selecionar todos os recebidos do CT">
              <input type="checkbox" id="checkAllCT" checked>
            </label>
            <span class="dash-col-header">N.º FICAI / ALUNO / TURMA</span>
          </div>
          <div class="dash-list-tbody" id="listRecebidosCT">
            <div class="dash-list-row" data-ficai="0021/2026" data-student="Ana Clara Nascimento" data-turma="7B" data-sit="Alerta crítico">
              <label class="custom-check-wrap" data-tooltip="Selecionar este registro">
                <input type="checkbox" class="item-check ct-check">
              </label>
              <div class="dash-row-status-icon alert-warn" data-tooltip="Alerta Crítico: Retorno urgente solicitado pelo Conselho Tutelar">
                <i class="fa-solid fa-triangle-exclamation"></i>
              </div>
              <div class="dash-row-content">
                <a href="javascript:void(0)" class="dash-item-link" data-student="Ana Clara Nascimento" data-ficai="0021/2026" data-turma="7º Ano B" data-sit="Alerta crítico" data-tooltip="Clique para ver o histórico e ficha de Ana Clara Nascimento">
                  <strong>0021</strong>/Ana Clara Nascimento / 7B
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Coluna 2: Gerados -->
      <div class="dash-split-card">
        <div class="dash-split-head">
          <div class="dash-split-title-group">
            <div class="dash-split-icon-badge gerados-icon">
              <i class="fa-solid fa-tag"></i>
            </div>
            <strong class="dash-split-title">Gerados</strong>
          </div>
          <span class="dash-split-counter" id="countGerados">Documentos gerados (4 registros)</span>
        </div>

        <div class="dash-list-table">
          <div class="dash-list-thead">
            <label class="custom-check-wrap" data-tooltip="Selecionar todos os gerados">
              <input type="checkbox" id="checkAllGerados" checked>
            </label>
            <span class="dash-col-header">N.º FICAI / ALUNO / TURMA</span>
          </div>
          <div class="dash-list-tbody" id="listGerados">
            <div class="dash-list-row" data-ficai="0017/2026" data-student="Bruno Henrique Silva" data-turma="6A" data-sit="Aviso de faltas">
              <label class="custom-check-wrap" data-tooltip="Selecionar este registro">
                <input type="checkbox" class="item-check gerados-check">
              </label>
              <div class="dash-row-status-icon tag-green" data-tooltip="Situação: Aviso de faltas regularizado">
                <i class="fa-solid fa-tag"></i>
              </div>
              <div class="dash-row-content">
                <a href="javascript:void(0)" class="dash-item-link" data-student="Bruno Henrique Silva" data-ficai="0017/2026" data-turma="6º Ano A" data-sit="Aviso de faltas" data-tooltip="Clique para ver o histórico e ficha de Bruno Henrique Silva">
                  <strong>0017</strong>/Bruno Henrique Silva / 6A
                </a>
              </div>
            </div>

            <div class="dash-list-row" data-ficai="0018/2026" data-student="Carla Souza Ribeiro" data-turma="9A" data-sit="No Conselho">
              <label class="custom-check-wrap" data-tooltip="Selecionar este registro">
                <input type="checkbox" class="item-check gerados-check">
              </label>
              <div class="dash-row-status-icon tag-blue" data-tooltip="Situação: Encaminhada para diligências">
                <i class="fa-solid fa-tag"></i>
              </div>
              <div class="dash-row-content">
                <a href="javascript:void(0)" class="dash-item-link" data-student="Carla Souza Ribeiro" data-ficai="0018/2026" data-turma="9º Ano A" data-sit="No Conselho" data-tooltip="Clique para ver o histórico e ficha de Carla Souza Ribeiro">
                  <strong>0018</strong>/Carla Souza Ribeiro / 9A
                </a>
              </div>
            </div>

            <div class="dash-list-row" data-ficai="0019/2026" data-student="Diego Santos Alves" data-turma="8C" data-sit="Retorno">
              <label class="custom-check-wrap" data-tooltip="Selecionar este registro">
                <input type="checkbox" class="item-check gerados-check">
              </label>
              <div class="dash-row-status-icon tag-purple" data-tooltip="Situação: Encaminhado ao Conselho Tutelar">
                <i class="fa-solid fa-tag"></i>
              </div>
              <div class="dash-row-content">
                <a href="javascript:void(0)" class="dash-item-link" data-student="Diego Santos Alves" data-ficai="0019/2026" data-turma="8º Ano C" data-sit="Retorno" data-tooltip="Clique para ver o histórico e ficha de Diego Santos Alves">
                  <strong>0019</strong>/Diego Santos Alves / 8C
                </a>
              </div>
            </div>

            <div class="dash-list-row" data-ficai="0020/2026" data-student="Ana Clara Nascimento" data-turma="7B" data-sit="Alerta crítico">
              <label class="custom-check-wrap" data-tooltip="Selecionar este registro">
                <input type="checkbox" class="item-check gerados-check">
              </label>
              <div class="dash-row-status-icon tag-gray" data-tooltip="Situação: Histórico anterior registrado">
                <i class="fa-solid fa-tag"></i>
              </div>
              <div class="dash-row-content">
                <a href="javascript:void(0)" class="dash-item-link" data-student="Ana Clara Nascimento" data-ficai="0020/2026" data-turma="7º Ano B" data-sit="Alerta crítico" data-tooltip="Clique para ver o histórico e ficha de Ana Clara Nascimento">
                  <strong>0020</strong>/Ana Clara Nascimento / 7B
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""

html = html.replace(old_dashboard_card, new_dashboard_card, 1)



# JavaScript for filtering, selecting all, and opening modal from the split lists
split_dashboard_js = """
// ==============================================================================
// FILTRO & SELEÇÃO DO NOVO LAYOUT SPLIT (RECEBIDOS CT & GERADOS)
// ==============================================================================
function filterSplitLists(){
  const q = ($('#dashSearch')?.value || '').toLowerCase().trim();
  const turma = ($('#dashTurmaFilter')?.value || '').toLowerCase().trim();
  const sit = ($('#dashSituacaoFilter')?.value || '').toLowerCase().trim();

  let visibleCT = 0, visibleGerados = 0;

  // Filtrar Recebidos CT
  $$('#listRecebidosCT .dash-list-row').forEach(row => {
    const text = row.innerText.toLowerCase();
    const rTurma = (row.dataset.turma || '').toLowerCase();
    const rSit = (row.dataset.sit || '').toLowerCase();

    const matchQ = !q || text.includes(q);
    const matchTurma = !turma || rTurma.includes(turma);
    const matchSit = !sit || rSit.includes(sit);

    if (matchQ && matchTurma && matchSit) {
      row.style.display = 'flex';
      visibleCT++;
    } else {
      row.style.display = 'none';
    }
  });

  // Filtrar Gerados
  $$('#listGerados .dash-list-row').forEach(row => {
    const text = row.innerText.toLowerCase();
    const rTurma = (row.dataset.turma || '').toLowerCase();
    const rSit = (row.dataset.sit || '').toLowerCase();

    const matchQ = !q || text.includes(q);
    const matchTurma = !turma || rTurma.includes(turma);
    const matchSit = !sit || rSit.includes(sit);

    if (matchQ && matchTurma && matchSit) {
      row.style.display = 'flex';
      visibleGerados++;
    } else {
      row.style.display = 'none';
    }
  });

  // Atualizar contadores
  const countCT = $('#countRecebidosCT');
  if(countCT) countCT.textContent = `Documentos recebidos (${visibleCT} registro${visibleCT === 1 ? '' : 's'})`;

  const countGerados = $('#countGerados');
  if(countGerados) countGerados.textContent = `Documentos gerados (${visibleGerados} registro${visibleGerados === 1 ? '' : 's'})`;
}

$('#dashSearch')?.addEventListener('input', filterSplitLists);
$('#dashTurmaFilter')?.addEventListener('change', filterSplitLists);
$('#dashSituacaoFilter')?.addEventListener('change', filterSplitLists);
$('#dashPeriodoFilter')?.addEventListener('change', filterSplitLists);

// Select All Handlers
$('#checkAllCT')?.addEventListener('change', e => {
  $$('#listRecebidosCT .item-check').forEach(chk => {
    if(chk.closest('.dash-list-row').style.display !== 'none') chk.checked = e.target.checked;
  });
});

$('#checkAllGerados')?.addEventListener('change', e => {
  $$('#listGerados .item-check').forEach(chk => {
    if(chk.closest('.dash-list-row').style.display !== 'none') chk.checked = e.target.checked;
  });
});

// Clique no título do painel reseta os filtros ou foca na pesquisa
$('#dashPanelTitle')?.addEventListener('click', () => {
  if($('#dashSearch').value || $('#dashTurmaFilter').value || $('#dashSituacaoFilter').value){
    $('#dashSearch').value = '';
    $('#dashTurmaFilter').value = '';
    $('#dashSituacaoFilter').value = '';
    filterSplitLists();
    toast('Filtros redefinidos. Exibindo todos os registros.');
  } else {
    $('#dashSearch').focus();
    toast('Digite para buscar aluno, documento ou responsável.');
  }
});

// Abertura do Modal de Informações ao clicar em qualquer item das listas
$('.dash-split-grid')?.addEventListener('click', async e => {
  const link = e.target.closest('.dash-item-link');
  if(link && !e.target.closest('input[type="checkbox"]')) {
    e.preventDefault();
    const studentName = link.dataset.student || 'Ana Clara Nascimento';
    const ficaiNum = link.dataset.ficai || '0021/2026';
    const turma = link.dataset.turma || '7º Ano B';
    const situacao = link.dataset.sit || 'Infrequente';

    let r = null;
    try {
      const all = await dbGetAll('ficais');
      r = all.find(item => item.numero === ficaiNum || item.aluno === studentName || item.studentKey === studentKey(studentName));
    } catch(_e){}

    if(!r) {
      const year = currentYear.toString();
      r = {
        numero: ficaiNum,
        ano: year,
        studentKey: studentKey(studentName),
        aluno: studentName,
        escola: 'E.M. Elmir Figueira',
        turma: turma,
        situacao: situacao,
        createdAt: new Date().toISOString(),
        generatedAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        infoEntries: [],
        demoOnly: true,
        data: {
          nomeCompleto: studentName,
          turma: turma,
          situacao: situacao,
          observacaoInicial: 'Registro consolidado da FICAI.',
          vulnerabilidades: [],
          diagnostico: {},
          procedimentos: []
        }
      };
    }
    renderInfoModal(r);
    $('#infoModal').classList.add('open');
    $('#infoModal').setAttribute('aria-hidden', 'false');
  }
});
"""
html = html.replace("bindFilter($('#dashSearch'),'#dashTable');", split_dashboard_js)

# 5.1 Atualizar campo de Número FICAI com Badge Auto e Botão de Ação
old_num_field = '<div class="meta-field meta-number"><label>Número FICAI</label><input id="numeroFicai" type="text" value="00001/2026" maxlength="10" inputmode="numeric"></div>'
new_num_field = '''<div class="meta-field meta-number">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px">
              <label for="numeroFicai" style="margin-bottom:0">Número FICAI</label>
              <span class="auto-num-badge" id="btnAutoNum" data-tooltip="Recalcular o próximo número sequencial automaticamente"><i class="fa-solid fa-wand-magic-sparkles"></i> Auto</span>
            </div>
            <div class="input-with-action">
              <input id="numeroFicai" type="text" value="00022/2026" maxlength="10" inputmode="numeric" placeholder="00001/2026" data-tooltip="Gerado automaticamente pela sequência do ano. Você também pode digitar se necessário.">
              <button class="btn-input-icon" type="button" id="btnRefreshFicaiNum" data-tooltip="Recalcular próximo número da FICAI"><i class="fa-solid fa-arrows-rotate"></i></button>
            </div>
          </div>'''
html = html.replace(old_num_field, new_num_field, 1)

# 5.2 Substituir normalizeNumber por Geração Automática Sequencial Inteligente
old_normalize_js = r"""function normalizeNumber(){let v=$('#numeroFicai').value.trim();if(/^\d+$/.test(v))v=v.padStart(5,'0')+'/'+$('#anoLetivo').value;if(!v.includes('/'))v='00001/'+$('#anoLetivo').value;$('#numeroFicai').value=v;$('#ficaiHeaderNumber').textContent=v}
$('#anoLetivo').addEventListener('change',()=>{const seq=($('#numeroFicai').value.split('/')[0]||'00001').padStart(5,'0');$('#numeroFicai').value=seq+'/'+$('#anoLetivo').value;normalizeNumber()});$('#numeroFicai').addEventListener('blur',normalizeNumber);normalizeNumber();"""

new_auto_number_js = r"""function normalizeNumber(){
  let v = ($('#numeroFicai')?.value || '').trim();
  const year = $('#anoLetivo')?.value || new Date().getFullYear().toString();
  if(/^\d+$/.test(v)) v = v.padStart(5,'0') + '/' + year;
  if(!v.includes('/')) v = '00001/' + year;
  if($('#numeroFicai')) $('#numeroFicai').value = v;
  if($('#ficaiHeaderNumber')) $('#ficaiHeaderNumber').textContent = v;
}

// Geração sequencial automática do Número FICAI baseada no histórico + IndexedDB
async function getNextFicaiNumber(targetYear){
  const year = targetYear || $('#anoLetivo')?.value || new Date().getFullYear().toString();
  let maxSeq = 0;
  
  // 1. Números base dos registros conhecidos e de demonstração
  const baseKnown = [17, 18, 19, 20, 21];
  baseKnown.forEach(n => { if(n > maxSeq) maxSeq = n; });

  // 2. Registros persistidos no banco local IndexedDB
  try {
    const stored = await dbGetAll('ficais');
    if (Array.isArray(stored)) {
      stored.forEach(r => {
        if (r && r.numero) {
          const parts = String(r.numero).split('/');
          const num = parseInt(parts[0], 10);
          const rYear = parts[1] || year;
          if (rYear === year && !isNaN(num) && num > maxSeq) {
            maxSeq = num;
          }
        }
      });
    }
  } catch (e) {
    console.warn('Erro ao consultar banco para número FICAI', e);
  }

  const nextSeq = maxSeq + 1;
  return String(nextSeq).padStart(5, '0') + '/' + year;
}

async function autoGenerateFicaiNumber(force = false){
  const input = $('#numeroFicai');
  if (!input) return;
  const year = $('#anoLetivo')?.value || new Date().getFullYear().toString();
  const nextNum = await getNextFicaiNumber(year);
  input.value = nextNum;
  if ($('#ficaiHeaderNumber')) $('#ficaiHeaderNumber').textContent = nextNum;
  normalizeNumber();
  if (force) toast(`Número FICAI ${nextNum} gerado automaticamente.`);
}

$('#anoLetivo')?.addEventListener('change', () => autoGenerateFicaiNumber(false));
$('#numeroFicai')?.addEventListener('blur', normalizeNumber);
$('#btnAutoNum')?.addEventListener('click', () => autoGenerateFicaiNumber(true));
$('#btnRefreshFicaiNum')?.addEventListener('click', () => autoGenerateFicaiNumber(true));

// Auto gerar ao carregar
setTimeout(() => autoGenerateFicaiNumber(false), 60);"""

html = html.replace(old_normalize_js, new_auto_number_js, 1)

# Atualizar clearDraft para recalcular número automático após limpeza
old_clear_draft = "$('#clearDraft').onclick=e=>{e.preventDefault();if(confirm('Limpar o formulário atual?')){localStorage.removeItem('ficai4Draft');$('#ficaiForm').reset();$('#escolaEndereco').value='';$('#escolaTelefone').value='';$('#modalidade').value='';normalizeNumber()}};"
new_clear_draft = "$('#clearDraft').onclick=e=>{e.preventDefault();if(confirm('Limpar o formulário atual?')){localStorage.removeItem('ficai4Draft');$('#ficaiForm').reset();$('#escolaEndereco').value='';$('#escolaTelefone').value='';$('#modalidade').value='';autoGenerateFicaiNumber(true)}};"
html = html.replace(old_clear_draft, new_clear_draft, 1)




# 6. Append Tooltip JS Engine with correct content node + arrow positioning
tooltip_js = """
// ==============================================================================
// SISTEMA UNIVERSAL DE TOOLTIPS DINÂMICOS & MICRO-INTERAÇÕES UX
// ==============================================================================
(function initTooltipEngine(){
  let activeTooltip=null, currentEl=null, hideTimeout=null;

  function createTooltip(){
    const tip=document.createElement('div');
    tip.className='ui-tooltip';
    tip.setAttribute('role','tooltip');
    tip.setAttribute('aria-hidden','true');
    const content=document.createElement('span');
    content.className='ui-tooltip-content';
    const arrow=document.createElement('div');
    arrow.className='ui-tooltip-arrow';
    tip.appendChild(content);
    tip.appendChild(arrow);
    document.body.appendChild(tip);
    return tip;
  }

  function showTooltip(el){
    const text=el.dataset.tooltip||el.getAttribute('title');
    if(!text)return;
    if(!activeTooltip)activeTooltip=createTooltip();

    if(el.hasAttribute('title')){
      el.dataset.tooltip=el.getAttribute('title');
      el.removeAttribute('title');
    }

    currentEl=el;
    const contentEl=activeTooltip.querySelector('.ui-tooltip-content');
    if(contentEl)contentEl.textContent=text;
    activeTooltip.classList.add('visible');
    activeTooltip.setAttribute('aria-hidden','false');
    positionTooltip(el);
  }

  function positionTooltip(el){
    if(!activeTooltip||!currentEl)return;
    const rect=el.getBoundingClientRect();
    const tipRect=activeTooltip.getBoundingClientRect();
    let pos=el.dataset.tooltipPos||'top';
    const spacing=9;

    let top=0, left=0;

    if(pos==='top' && rect.top - tipRect.height - spacing < 10){
      pos='bottom';
    }

    if(pos==='bottom'){
      top=rect.bottom+spacing;
      left=rect.left+(rect.width-tipRect.width)/2;
      activeTooltip.setAttribute('data-placed','bottom');
    }else if(pos==='right'){
      top=rect.top+(rect.height-tipRect.height)/2;
      left=rect.right+spacing;
      activeTooltip.setAttribute('data-placed','right');
    }else if(pos==='left'){
      top=rect.top+(rect.height-tipRect.height)/2;
      left=rect.left-tipRect.width-spacing;
      activeTooltip.setAttribute('data-placed','left');
    }else{
      // top
      top=rect.top-tipRect.height-spacing;
      left=rect.left+(rect.width-tipRect.width)/2;
      activeTooltip.setAttribute('data-placed','top');
    }

    // Viewport boundaries
    if(left<12)left=12;
    if(left+tipRect.width>window.innerWidth-12)left=window.innerWidth-tipRect.width-12;

    activeTooltip.style.top=`${Math.round(top)}px`;
    activeTooltip.style.left=`${Math.round(left)}px`;
  }

  function hideTooltip(){
    if(!activeTooltip)return;
    activeTooltip.classList.remove('visible');
    activeTooltip.setAttribute('aria-hidden','true');
    currentEl=null;
  }

  document.addEventListener('mouseover',e=>{
    const target=e.target.closest('[data-tooltip],[title]');
    if(target){
      clearTimeout(hideTimeout);
      showTooltip(target);
    }
  });

  document.addEventListener('mouseout',e=>{
    const target=e.target.closest('[data-tooltip]');
    if(target){
      hideTimeout=setTimeout(hideTooltip,60);
    }
  });

  document.addEventListener('focusin',e=>{
    const target=e.target.closest('[data-tooltip]');
    if(target)showTooltip(target);
  });
  document.addEventListener('focusout',()=>hideTooltip());
  window.addEventListener('scroll',()=>hideTooltip(),{passive:true});
})();
"""

html = html.replace('initConfigCatalogs();', tooltip_js + '\ninitConfigCatalogs();')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html atualizado e corrigido com sucesso!")
