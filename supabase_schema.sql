-- ==============================================================================
-- SCHEMA FICAI 4.0 - SUPABASE (POSTGRESQL)
-- Secretaria Municipal de Educação (SMEDU) / Conselho Tutelar / Promotoria
-- ==============================================================================

-- 1. EXTENSÕES NECESSÁRIAS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Função utilitária para atualização automática de updated_at
CREATE OR REPLACE FUNCTION public.handle_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = timezone('utc'::text, now());
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ==============================================================================
-- 2. TABELAS DE CADASTROS BÁSICOS E CONFIGURAÇÕES
-- ==============================================================================

-- Tabela: Escolas
CREATE TABLE IF NOT EXISTS public.escolas (
    id TEXT PRIMARY KEY DEFAULT ('esc-' || gen_random_uuid()),
    inep TEXT,
    nome TEXT NOT NULL UNIQUE,
    diretor TEXT,
    endereco TEXT,
    bairro TEXT,
    telefone TEXT,
    ramal TEXT,
    email TEXT,
    modalidade TEXT,
    maps_link TEXT,
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_escolas_updated_at ON public.escolas;
CREATE TRIGGER set_escolas_updated_at
BEFORE UPDATE ON public.escolas
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Modalidades de Ensino
CREATE TABLE IF NOT EXISTS public.modalidades (
    id TEXT PRIMARY KEY DEFAULT ('mod-' || gen_random_uuid()),
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_modalidades_updated_at ON public.modalidades;
CREATE TRIGGER set_modalidades_updated_at
BEFORE UPDATE ON public.modalidades
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Turmas e Turnos
CREATE TABLE IF NOT EXISTS public.turmas (
    id TEXT PRIMARY KEY DEFAULT ('tur-' || gen_random_uuid()),
    ano TEXT NOT NULL,                -- Ex.: '6º Ano', '7º Ano'
    turma TEXT NOT NULL,              -- Ex.: '6º Ano A', '7º Ano B'
    turno TEXT NOT NULL,              -- 'Manhã', 'Tarde', 'Noite', 'Integral'
    modalidade TEXT,                  -- 'Ensino Fundamental', 'Educação Infantil', 'EJA'
    escola TEXT,                      -- Nome da escola vinculada
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_turmas_updated_at ON public.turmas;
CREATE TRIGGER set_turmas_updated_at
BEFORE UPDATE ON public.turmas
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Usuários do Sistema e Perfis RBAC
CREATE TABLE IF NOT EXISTS public.usuarios (
    id TEXT PRIMARY KEY DEFAULT ('usr-' || gen_random_uuid()),
    usuario TEXT NOT NULL,
    email TEXT,
    nivel TEXT NOT NULL,              -- 'Operacional', 'Gestor', 'Administrador', 'Conselho Tutelar'
    cargo TEXT,
    funcao TEXT,
    unidade TEXT,
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_usuarios_updated_at ON public.usuarios;
CREATE TRIGGER set_usuarios_updated_at
BEFORE UPDATE ON public.usuarios
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Permissões de Acesso por Módulo
CREATE TABLE IF NOT EXISTS public.permissoes (
    id TEXT PRIMARY KEY DEFAULT ('perm-' || gen_random_uuid()),
    perfil TEXT NOT NULL,             -- 'Administrador', 'Operacional', etc.
    modulo TEXT NOT NULL,             -- 'Dashboard', 'Gerar FICAI', 'Dados da Ficha', etc.
    visualizar BOOLEAN NOT NULL DEFAULT true,
    cadastrar BOOLEAN NOT NULL DEFAULT false,
    editar BOOLEAN NOT NULL DEFAULT false,
    excluir BOOLEAN NOT NULL DEFAULT false,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_permissoes_updated_at ON public.permissoes;
CREATE TRIGGER set_permissoes_updated_at
BEFORE UPDATE ON public.permissoes
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Pessoas / Equipe (Diretores, Orientadores, Conselheiros)
CREATE TABLE IF NOT EXISTS public.pessoas (
    id TEXT PRIMARY KEY DEFAULT ('pes-' || gen_random_uuid()),
    tipo TEXT NOT NULL,               -- 'Diretor', 'Diretor Adjunto', 'Orientador', 'Coordenador Pedagógico', 'Conselheiro Tutelar'
    nome TEXT NOT NULL,
    matricula TEXT,
    unidade TEXT,
    telefone TEXT,
    email TEXT,
    periodo TEXT DEFAULT '2026',
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_pessoas_updated_at ON public.pessoas;
CREATE TRIGGER set_pessoas_updated_at
BEFORE UPDATE ON public.pessoas
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Catálogo de Procedimentos da Escola
CREATE TABLE IF NOT EXISTS public.procedimentos (
    id TEXT PRIMARY KEY DEFAULT ('proc-' || gen_random_uuid()),
    ordem INT NOT NULL DEFAULT 1,
    nome TEXT NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_procedimentos_updated_at ON public.procedimentos;
CREATE TRIGGER set_procedimentos_updated_at
BEFORE UPDATE ON public.procedimentos
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Catálogo de Motivos e Diagnósticos da Evasão
CREATE TABLE IF NOT EXISTS public.motivos (
    id TEXT PRIMARY KEY DEFAULT ('mot-' || gen_random_uuid()),
    grupo TEXT NOT NULL,              -- 'Motivos da ausência', 'Estrutural', 'Social / Familiar', 'Saúde', 'Educacional', 'Segurança Pública e Violência', 'Econômica', 'Outros'
    nome TEXT NOT NULL,
    dashboard BOOLEAN NOT NULL DEFAULT false,
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_motivos_updated_at ON public.motivos;
CREATE TRIGGER set_motivos_updated_at
BEFORE UPDATE ON public.motivos
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Catálogos Personalizáveis (Situações do Aluno e Vulnerabilidades Extras)
CREATE TABLE IF NOT EXISTS public.catalogo_personalizado (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tipo TEXT NOT NULL,               -- 'situacao_aluno' ou 'vulnerabilidade'
    nome TEXT NOT NULL,
    descricao TEXT,
    unidade TEXT,
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

-- Tabela: Catálogo de Marcadores (Tags)
CREATE TABLE IF NOT EXISTS public.marcadores (
    id TEXT PRIMARY KEY DEFAULT ('tag-' || gen_random_uuid()),
    nome TEXT NOT NULL UNIQUE,
    cor TEXT NOT NULL DEFAULT '#6b7280',
    ativo BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

DROP TRIGGER IF EXISTS set_marcadores_updated_at ON public.marcadores;
CREATE TRIGGER set_marcadores_updated_at
BEFORE UPDATE ON public.marcadores
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- Tabela: Associação de Marcadores por Aluno/FICAI
CREATE TABLE IF NOT EXISTS public.student_tags (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ficai_numero TEXT NOT NULL REFERENCES public.ficais(numero) ON DELETE CASCADE,
    student_key TEXT,
    tag_nome TEXT NOT NULL,
    tag_cor TEXT NOT NULL DEFAULT '#6b7280',
    texto TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_student_tags_ficai ON public.student_tags(ficai_numero);

-- ==============================================================================
-- 3. TABELA DE ALUNOS (ESTUDANTES)
-- ==============================================================================

CREATE TABLE IF NOT EXISTS public.students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    key TEXT UNIQUE NOT NULL,         -- Chave normalizada para busca local/remota (ex: 'ana-clara-nascimento')
    nome TEXT NOT NULL,
    social TEXT,
    nascimento DATE,
    cpf TEXT,
    rg TEXT,
    filiacao TEXT,
    responsavel TEXT,
    residencia TEXT,
    telefone TEXT,
    referencia TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_students_key ON public.students(key);
CREATE INDEX IF NOT EXISTS idx_students_nome ON public.students(nome);
CREATE INDEX IF NOT EXISTS idx_students_cpf ON public.students(cpf);

DROP TRIGGER IF EXISTS set_students_updated_at ON public.students;
CREATE TRIGGER set_students_updated_at
BEFORE UPDATE ON public.students
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- ==============================================================================
-- 4. TABELA PRINCIPAL DE FICAIS
-- ==============================================================================

CREATE TABLE IF NOT EXISTS public.ficais (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    numero TEXT UNIQUE NOT NULL,       -- Número oficial FICAI (ex: '00001/2026')
    ano TEXT NOT NULL,                 -- Ano letivo (ex: '2026')
    student_key TEXT,
    aluno_id UUID REFERENCES public.students(id) ON DELETE SET NULL,
    aluno TEXT NOT NULL,
    escola TEXT,
    turma TEXT,
    turno TEXT,
    modalidade TEXT,
    situacao TEXT NOT NULL DEFAULT 'Infrequente', -- 'Infrequente', 'Evadido', 'Sem Acesso', personalizada
    
    -- Datas e identificação do profissional
    falta_inicio DATE,
    falta_fim DATE,
    data_comunicacao DATE,
    profissional TEXT,
    assinatura_prof TEXT,
    
    -- Textos e relatos
    relato_visita TEXT,
    outros_motivos TEXT,
    observacao_inicial TEXT,
    
    -- Diagnósticos, procedimentos e listas em JSON estruturado
    motivos JSONB DEFAULT '[]'::jsonb,
    vulnerabilidades JSONB DEFAULT '[]'::jsonb,
    diagnostico JSONB DEFAULT '{}'::jsonb,
    procedimentos JSONB DEFAULT '[]'::jsonb,
    situacoes_personalizadas JSONB DEFAULT '[]'::jsonb,
    
    -- Conselho Tutelar & Promotoria
    ct_recebimento TEXT,
    ct_diligencias TEXT,
    ct_devolucao TEXT,
    ct_conselheiro TEXT,
    promotoria_acoes JSONB DEFAULT '[]'::jsonb,
    promotor TEXT,
    prom_data DATE,
    
    -- Status do fluxo e encerramento
    status_fluxo TEXT NOT NULL DEFAULT 'aberto', -- 'aberto', 'em_analise', 'conselho_tutelar', 'promotoria', 'encerrado'
    data_encerramento TIMESTAMPTZ,
    motivo_encerramento TEXT,
    justificativa_encerramento TEXT,
    
    -- Snapshot completo do formulário (preserva fidelidade absoluta do front-end)
    data JSONB DEFAULT '{}'::jsonb,
    
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    generated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_ficais_numero ON public.ficais(numero);
CREATE INDEX IF NOT EXISTS idx_ficais_ano ON public.ficais(ano);
CREATE INDEX IF NOT EXISTS idx_ficais_aluno ON public.ficais(aluno);
CREATE INDEX IF NOT EXISTS idx_ficais_escola ON public.ficais(escola);
CREATE INDEX IF NOT EXISTS idx_ficais_situacao ON public.ficais(situacao);
CREATE INDEX IF NOT EXISTS idx_ficais_status_fluxo ON public.ficais(status_fluxo);
CREATE INDEX IF NOT EXISTS idx_ficais_updated_at ON public.ficais(updated_at DESC);

DROP TRIGGER IF EXISTS set_ficais_updated_at ON public.ficais;
CREATE TRIGGER set_ficais_updated_at
BEFORE UPDATE ON public.ficais
FOR EACH ROW EXECUTE FUNCTION public.handle_updated_at();

-- ==============================================================================
-- 5. TABELA DE HISTÓRICO E LINHA DO TEMPO PÓS-GERAÇÃO (INFO ENTRIES)
-- ==============================================================================

CREATE TABLE IF NOT EXISTS public.ficai_info_entries (
    id TEXT PRIMARY KEY DEFAULT ('reg-' || gen_random_uuid()),
    ficai_numero TEXT NOT NULL REFERENCES public.ficais(numero) ON DELETE CASCADE,
    date DATE NOT NULL,
    type TEXT NOT NULL,               -- 'Visita Domiciliar', 'Contato Telefônico', 'Devolutiva CT', etc.
    text TEXT NOT NULL,
    responsible TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now())
);

CREATE INDEX IF NOT EXISTS idx_info_entries_ficai ON public.ficai_info_entries(ficai_numero);
CREATE INDEX IF NOT EXISTS idx_info_entries_date ON public.ficai_info_entries(date DESC);

-- ==============================================================================
-- 6. HABILITAÇÃO DO ROW LEVEL SECURITY (RLS) E POLÍTICAS DE ACESSO
-- ==============================================================================

ALTER TABLE public.escolas ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.modalidades ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.turmas ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.usuarios ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.permissoes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.pessoas ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.procedimentos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.motivos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.catalogo_personalizado ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.marcadores ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.student_tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.students ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.ficais ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.ficai_info_entries ENABLE ROW LEVEL SECURITY;

-- Políticas de acesso irrestrito para clientes com a Publishable / Anon Key (ou autenticados)
-- Permite SELECT, INSERT, UPDATE e DELETE no aplicativo FICAI

DO $$
DECLARE
    t TEXT;
BEGIN
    FOR t IN SELECT tablename FROM pg_tables WHERE schemaname = 'public'
    LOOP
        EXECUTE format('DROP POLICY IF EXISTS "Public access for all on %I" ON public.%I', t, t);
        EXECUTE format('CREATE POLICY "Public access for all on %I" ON public.%I FOR ALL TO public USING (true) WITH CHECK (true)', t, t);
    END LOOP;
END;
$$;

-- ==============================================================================
-- 7. SEED INICIAL DE DADOS PADRÃO (ITAGUAÍ / SMEDU)
-- ==============================================================================

-- Escolas
INSERT INTO public.escolas (id, nome, endereco, telefone, email, ativo) VALUES
('aparecida', 'C. M. Aparecida Azêdo', 'Estrada do Teixeira, nº 2 - Itaguaí/RJ', '(21) 3782-9003', 'aparecida.azedo@itaguai.rj.gov.br', true),
('elmir', 'E.M. Elmir Figueira', 'Itaguaí/RJ - endereço cadastrado da unidade', '(21) 3782-9003', 'elmir.figueira@itaguai.rj.gov.br', true),
('mignone', 'CIEP 496 Maestro Francisco Mignone', 'Itaguaí/RJ - endereço cadastrado da unidade', '(21) 3782-9003', 'ciep496@itaguai.rj.gov.br', true)
ON CONFLICT (nome) DO NOTHING;

-- Modalidades
INSERT INTO public.modalidades (id, nome, descricao, ativo) VALUES
('mod-infantil', 'Educação Infantil', 'Pré e etapas da Educação Infantil.', true),
('mod-fundamental', 'Ensino Fundamental', 'Anos Iniciais e Anos Finais.', true),
('mod-eja', 'EJA', 'Educação de Jovens e Adultos / NCEJA.', true)
ON CONFLICT (nome) DO NOTHING;

-- Turmas
INSERT INTO public.turmas (id, ano, turma, turno, modalidade, escola, ativo) VALUES
('tur-6a', '6º Ano', '6º Ano A', 'Manhã', 'Ensino Fundamental', 'E.M. Elmir Figueira', true),
('tur-7b', '7º Ano', '7º Ano B', 'Manhã', 'Ensino Fundamental', 'E.M. Elmir Figueira', true),
('tur-8c', '8º Ano', '8º Ano C', 'Tarde', 'Ensino Fundamental', 'E.M. Elmir Figueira', true),
('tur-9a', '9º Ano', '9º Ano A', 'Tarde', 'Ensino Fundamental', 'E.M. Elmir Figueira', true),
('tur-n6a', 'NCEJA VI', 'NCEJA VI A', 'Noite', 'EJA', 'E.M. Elmir Figueira', true),
('tur-pre2a', 'Pré II', 'Pré II A', 'Manhã', 'Educação Infantil', 'C. M. Aparecida Azêdo', true)
ON CONFLICT (id) DO NOTHING;

-- Usuários
INSERT INTO public.usuarios (id, usuario, nivel, cargo, funcao, unidade, email, ativo) VALUES
('usr-escola', 'Usuário Escola', 'Operacional', 'Agente Administrativo', 'Secretaria Escolar', 'E.M. Elmir Figueira', 'escola@itaguai.rj.gov.br', true),
('usr-smedu', 'Usuário SMEDU', 'Administrador', 'Assessor', 'Gestão FICAI', 'SMEDU', 'smedu@itaguai.rj.gov.br', true)
ON CONFLICT (id) DO NOTHING;

-- Permissões
INSERT INTO public.permissoes (id, perfil, modulo, visualizar, cadastrar, editar, excluir) VALUES
('perm-admin', 'Administrador', 'Todos os módulos', true, true, true, true),
('perm-operacional', 'Operacional', 'FICAI', true, true, true, false)
ON CONFLICT (id) DO NOTHING;

-- Pessoas
INSERT INTO public.pessoas (id, tipo, nome, matricula, unidade, telefone, email, periodo, ativo) VALUES
('pes-dir', 'Diretor', 'Diretor(a) da Unidade', '', 'E.M. Elmir Figueira', '', '', '2026', true),
('pes-ori', 'Orientador', 'Orientador(a) Educacional', '', 'E.M. Elmir Figueira', '', '', '2026', true),
('pes-ct', 'Conselheiro Tutelar', 'Conselheiro(a) responsável', '', 'Conselho Tutelar de Itaguaí', '', '', '2026', true)
ON CONFLICT (id) DO NOTHING;

-- Procedimentos
INSERT INTO public.procedimentos (id, ordem, nome, ativo) VALUES
('proc-1', 1, 'Comunicação/bilhete ao responsável', true),
('proc-2', 2, 'Retorno do estudante à escola', true),
('proc-3', 3, 'Contato telefônico com o responsável', true),
('proc-4', 4, 'Não retorno do aluno à escola', true),
('proc-5', 5, 'Telegrama ao responsável', true),
('proc-6', 6, 'Visita ao domicílio do aluno', true),
('proc-7', 7, 'Comparecimento do responsável e assinatura do termo de responsabilidade', true)
ON CONFLICT (nome) DO NOTHING;

-- Motivos e Diagnósticos
INSERT INTO public.motivos (id, grupo, nome, dashboard, ativo) VALUES
('mot-1', 'Motivos da ausência', 'Mudança de endereço do aluno com pedido de transferência escolar', false, true),
('mot-2', 'Motivos da ausência', 'Aluno está trabalhando', false, true),
('mot-3', 'Motivos da ausência', 'Mudança de endereço do aluno sem pedido de transferência escolar', false, true),
('mot-4', 'Motivos da ausência', 'Falta recurso para o transporte escolar', false, true),
('mot-5', 'Motivos da ausência', 'Informação de matrícula em outra Unidade Educacional', false, true),
('mot-6', 'Motivos da ausência', 'Falta de motivação para ir à escola', true, true),
('mot-7', 'Motivos da ausência', 'Aluno ficou doente (internação, receita, atestado, cuidados caseiros)', true, true),
('mot-8', 'Motivos da ausência', 'Baixo interesse do responsável (omissão, negligência)', false, true),
('mot-9', 'Motivos da ausência', 'Violência no local de moradia', false, true),
('mot-10', 'Estrutural', 'Falta de Vaga na Escola', false, true),
('mot-11', 'Estrutural', 'Dificuldade de Transporte', false, true),
('mot-12', 'Estrutural', 'Distância da Residência', false, true),
('mot-13', 'Estrutural', 'Barreiras Arquitetônicas', false, true),
('mot-14', 'Estrutural', 'Falta de recursos (didático, vestuário)', false, true),
('mot-15', 'Estrutural', 'Falta de políticas escolares', false, true),
('mot-16', 'Estrutural', 'Falta de educação especial', false, true),
('mot-17', 'Social / Familiar', 'Trabalho Infantil', false, true),
('mot-18', 'Social / Familiar', 'Conflito Familiar', false, true),
('mot-19', 'Social / Familiar', 'Gravidez na Adolescência', false, true),
('mot-20', 'Social / Familiar', 'Vulnerabilidade Social', false, true),
('mot-21', 'Social / Familiar', 'Cuidados familiares', false, true),
('mot-22', 'Saúde', 'Saúde do Aluno (Física)', false, true),
('mot-23', 'Saúde', 'Saúde Mental (Aluno)', false, true),
('mot-24', 'Saúde', 'Doença na Família', false, true),
('mot-25', 'Saúde', 'Dependência Química', false, true),
('mot-26', 'Educacional', 'Dificuldade de Aprendizagem', false, true),
('mot-27', 'Educacional', 'Evasão por Bullying', false, true),
('mot-28', 'Educacional', 'Falta de Motivação', false, true),
('mot-29', 'Educacional', 'Desajuste de Nível/Idade', false, true),
('mot-30', 'Educacional', 'Risco de reprovação', false, true),
('mot-31', 'Segurança Pública e Violência', 'Ameaça ou Violência no Trajeto', false, true),
('mot-32', 'Segurança Pública e Violência', 'Envolvimento com Tráfico', false, true),
('mot-33', 'Segurança Pública e Violência', 'Violência Doméstica', false, true),
('mot-34', 'Segurança Pública e Violência', 'Medida Socioeducativa', false, true),
('mot-35', 'Econômica', 'Inserção no Mercado de Trabalho', false, true),
('mot-36', 'Econômica', 'Falta de Recursos Materiais', false, true),
('mot-37', 'Econômica', 'Insegurança Alimentar', false, true),
('mot-38', 'Econômica', 'Mudança de Domicílio/Migração', false, true),
('mot-39', 'Outros', 'Violência', false, true),
('mot-40', 'Outros', 'Bullying', false, true),
('mot-41', 'Outros', 'Preconceito', false, true)
ON CONFLICT (id) DO NOTHING;

-- Alunos demonstrativos
INSERT INTO public.students (key, nome, social, nascimento, cpf, rg, filiacao, responsavel, residencia, telefone, referencia) VALUES
('aluno-demonstrativo', 'Aluno Demonstrativo', '', '2012-05-14', '', '', 'Responsável 1 / Responsável 2', 'Responsável Demonstrativo', 'Endereço demonstrativo - Itaguaí/RJ', '(21) 99999-0000', 'Parente de referência - Itaguaí/RJ'),
('ana-clara-nascimento', 'Ana Clara Nascimento', '', '2012-03-11', '', '', 'Dados cadastrados no sistema', 'Responsável cadastrado', 'Itaguaí/RJ', '(21) 99999-1111', 'Referência cadastrada'),
('bruno-henrique-silva', 'Bruno Henrique Silva', '', '2013-07-21', '', '', 'Dados cadastrados no sistema', 'Responsável cadastrado', 'Itaguaí/RJ', '(21) 99999-2222', 'Referência cadastrada')
ON CONFLICT (key) DO NOTHING;

-- ==============================================================================
-- ==============================================================================
-- CADASTRO EM MASSA DE USUÁRIOS NO AUTHENTICATOR DO SUPABASE (auth.users)
-- Execute no SQL Editor do Supabase: https://supabase.com/dashboard/project/ojvxsrvmmkjxfgyczypm/sql/new
-- ==============================================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

DO $$
DECLARE
  usr_record RECORD;
  usr_id UUID;
  encrypted_pw TEXT;
BEGIN
  -- Tabela temporária de dados para inserção em massa
  CREATE TEMP TABLE IF NOT EXISTS temp_users_seed (
    email TEXT PRIMARY KEY,
    password TEXT,
    role TEXT
  ) ON COMMIT DROP;

  TRUNCATE temp_users_seed;

  -- Inserir Administrador CPD (Senha: T3c4n3x0)
  INSERT INTO temp_users_seed (email, password, role) VALUES
    ('cpdinfra@edu.itaguai.rj.gov.br', 'T3c4n3x0', 'Administrador')
  ON CONFLICT (email) DO UPDATE SET password = EXCLUDED.password;

  -- Inserir os 65 E-mails de Escolas (Senha: Ficai22026)
  INSERT INTO temp_users_seed (email, password, role) VALUES
    ('carmem.menezes.adm@gmail.com', 'Ficai22026', 'Escola'),
    ('cemaee@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cesmi@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('ciep300@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('ciep496@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('ciep497@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.aparecidaazedo@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.daniellebatistadasilva@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.edsoncruzamado@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.elianelopesbarbosa@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.estreladoceu@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.euclydesjoseborges@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.florentinoelias@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.franciscoxavierdemourabrito@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.jardimmar@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.joaquiminoue@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.mariacristinapadelacabraldasilva@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.mariadelurdessgarcia@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.mariaeduvigesdorosariosilva@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.mariarosagomesdonascimento@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.renatobarbosaladislau@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.ritaferreirafeijo@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.senadorteotoniovilella@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.taniamaramottademenezes@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('cm.teresinhadejesuscamposdefarias@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.camilocuquejo@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.carmemmenezesdireito@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.chapero@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.drjorgeabrahao@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.fazsantacandida@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.santarosa@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eem.tacianobasilio@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('eemcamilocuquejo@gmail.com', 'Ficai22026', 'Escola'),
    ('em.acacias@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.alexandreignacio@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.amauriferreira@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.antoniotupinamba@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.argentinacoutinho@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.celalzirosantiago@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.eiderribeirodantas@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.elmirafigueira@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.elmobaptistacoelho@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.fusaofukmati@edu.itaguai.gov.br', 'Ficai22026', 'Escola'),
    ('em.jardimmar@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.joaovicentesoares@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.jorgefloresdasilva@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.mariaguilherminadesouzafreire@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.oscarjosedesouza@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.padrerafaelscarfo@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.prefalbeilardgoulartdesouza@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.prefotonirocha@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.prefwilsonpedrofrancisco@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.renatogoncalvesmartins@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.saosebastiao@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.severinadosramosdesousa@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.severinosalustianodefrarias@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.terezadearaujosagario@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.veramericorodriguesdeamorim@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.vereadorgalliacoprata@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.verprofessorarthurbritodecastro@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.vertaianofernandesnunes@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('em.yolandarangelpereira@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('emei.hypolitovieradecarvalho@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('emei.monteirolobato@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola'),
    ('emei.prefisoldacksoncruzdebrito@edu.itaguai.rj.gov.br', 'Ficai22026', 'Escola')
  ON CONFLICT (email) DO UPDATE SET password = EXCLUDED.password;

  -- Processar inserção/atualização automática no Authenticator (auth.users e auth.identities)
  FOR usr_record IN SELECT * FROM temp_users_seed LOOP
    encrypted_pw := crypt(usr_record.password, gen_salt('bf', 10));

    -- Verifica se o usuário já existe em auth.users
    SELECT id INTO usr_id FROM auth.users WHERE lower(email) = lower(usr_record.email);

    IF usr_id IS NOT NULL THEN
      UPDATE auth.users
      SET
        encrypted_password = encrypted_pw,
        email_confirmed_at = COALESCE(email_confirmed_at, now()),
        raw_app_meta_data = '{"provider":"email","providers":["email"]}'::jsonb,
        raw_user_meta_data = jsonb_build_object('role', usr_record.role),
        updated_at = now()
      WHERE id = usr_id;

      -- Atualiza ou insere em auth.identities
      IF NOT EXISTS (SELECT 1 FROM auth.identities WHERE user_id = usr_id) THEN
        INSERT INTO auth.identities (
          id, provider_id, user_id, identity_data, provider, last_sign_in_at, created_at, updated_at
        ) VALUES (
          gen_random_uuid(), usr_id::text, usr_id, jsonb_build_object('sub', usr_id::text, 'email', usr_record.email),
          'email', now(), now(), now()
        );
      END IF;
    ELSE
      usr_id := gen_random_uuid();

      INSERT INTO auth.users (
        id, instance_id, email, encrypted_password, email_confirmed_at,
        raw_app_meta_data, raw_user_meta_data, is_super_admin, role, aud, created_at, updated_at
      ) VALUES (
        usr_id, '00000000-0000-0000-0000-000000000000', usr_record.email, encrypted_pw, now(),
        '{"provider":"email","providers":["email"]}'::jsonb, jsonb_build_object('role', usr_record.role),
        false, 'authenticated', 'authenticated', now(), now()
      );

      INSERT INTO auth.identities (
        id, provider_id, user_id, identity_data, provider, last_sign_in_at, created_at, updated_at
      ) VALUES (
        gen_random_uuid(), usr_id::text, usr_id, jsonb_build_object('sub', usr_id::text, 'email', usr_record.email),
        'email', now(), now(), now()
      );
    END IF;
  END LOOP;
END $$;