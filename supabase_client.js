/**
 * Cliente de Integração Supabase - FICAI 4.0
 * Conexão direta com o Supabase usando as chaves configuradas
 */

const SUPABASE_URL = 'https://ojvxsrvmmkjxfgyczypm.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_JDPRSMCStt58M2CWLfNHtA_F1zuxvvG';

// Inicialização do cliente Supabase (requer @supabase/supabase-js incluído no HTML)
let supabaseClient = null;

function getSupabase() {
  if (supabaseClient) return supabaseClient;
  if (typeof window !== 'undefined' && window.supabase && window.supabase.createClient) {
    supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    return supabaseClient;
  }
  return null;
}

// Serviços para Alunos (Students)
const StudentService = {
  async getAll() {
    const sb = getSupabase();
    if (!sb) return [];
    const { data, error } = await sb.from('students').select('*').order('nome');
    if (error) throw error;
    return data;
  },

  async upsert(student) {
    const sb = getSupabase();
    if (!sb) return null;
    const payload = {
      key: student.key,
      nome: student.nome,
      social: student.social || '',
      nascimento: student.nascimento || null,
      cpf: student.cpf || '',
      rg: student.rg || '',
      filiacao: student.filiacao || '',
      responsavel: student.responsavel || '',
      residencia: student.residencia || '',
      telefone: student.telefone || '',
      referencia: student.referencia || '',
      updated_at: new Date().toISOString()
    };
    const { data, error } = await sb.from('students').upsert(payload, { onConflict: 'key' }).select();
    if (error) throw error;
    return data?.[0];
  }
};

// Serviços para FICAIs
const FicaiService = {
  async getAll() {
    const sb = getSupabase();
    if (!sb) return [];
    const { data, error } = await sb.from('ficais').select('*').order('updated_at', { ascending: false });
    if (error) throw error;
    return data;
  },

  async getByNumero(numero) {
    const sb = getSupabase();
    if (!sb) return null;
    const { data, error } = await sb.from('ficais').select('*, ficai_info_entries(*)').eq('numero', numero).maybeSingle();
    if (error) throw error;
    return data;
  },

  async upsert(record) {
    const sb = getSupabase();
    if (!sb) return null;
    const payload = {
      numero: record.numero,
      ano: record.ano,
      student_key: record.studentKey || record.student_key,
      aluno: record.aluno,
      escola: record.escola,
      turma: record.turma,
      situacao: record.situacao || 'Infrequente',
      data: record.data || {},
      status_fluxo: record.status_fluxo || 'aberto',
      updated_at: new Date().toISOString()
    };
    const { data, error } = await sb.from('ficais').upsert(payload, { onConflict: 'numero' }).select();
    if (error) throw error;
    return data?.[0];
  },

  async addInfoEntry(entry) {
    const sb = getSupabase();
    if (!sb) return null;
    const payload = {
      ficai_numero: entry.ficai_numero || entry.ficaiNumero,
      date: entry.date,
      type: entry.type,
      text: entry.text,
      responsible: entry.responsible || 'Usuário'
    };
    const { data, error } = await sb.from('ficai_info_entries').insert(payload).select();
    if (error) throw error;
    return data?.[0];
  }
};

// Exporta para escopo global se em navegador
if (typeof window !== 'undefined') {
  window.SupabaseConfig = { SUPABASE_URL, SUPABASE_ANON_KEY };
  window.getSupabase = getSupabase;
  window.StudentService = StudentService;
  window.FicaiService = FicaiService;
}
