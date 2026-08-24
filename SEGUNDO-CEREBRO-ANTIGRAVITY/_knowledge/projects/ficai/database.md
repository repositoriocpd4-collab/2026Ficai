---
tags: [knowledge, project, ficai, database]
status: active
created: 2026-08-24
updated: 2026-08-24
---

# FICAI 4.0 — Estrutura de Banco de Dados

## 1. Instância Supabase (PostgreSQL 15+)

- **URL Base:** `https://ojvxsrvmmkjxfgyczypm.supabase.co`
- **Chave de Acesso:** `sb_publishable_JDPRSMCStt58M2CWLfNHtA_F1zuxvvG`
- **Script SQL de Origem:** `supabase_schema.sql`
- **Status do Banco Cloud (Verificado em 24/08/2026):**

| Tabela | Função | Quantidade Atual de Registros |
| :--- | :--- | :---: |
| `escolas` | Cadastro oficial das unidades escolares de Itaguaí | **67 registros** |
| `students` / `alunos` | Alunos cadastrados na rede | 3 registros |
| `ficais` | Registro das FICAIs geradas | 0 registros (em homologação) |
| `modalidades` | Modalidades de ensino | 3 registros |
| `turmas` | Turmas e turnos vinculados às escolas | 12 registros |
| `usuarios` | Perfis de acesso e usuários do sistema | 5 registros |
| `permissoes` | Matriz de permissões por perfil/módulo | 5 registros |
| `pessoas` | Diretores, orientadores e conselheiros | 6 registros |
| `procedimentos` | Catálogo de procedimentos escolares | 7 registros |
| `motivos` | Motivos de ausência e diagnósticos | 41 registros |

---

## 2. Esquema Relacional Supabase (`escolas` e `ficais`)

### Tabela `escolas`
```sql
CREATE TABLE public.escolas (
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
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);
```

### Tabela `ficais`
```sql
CREATE TABLE public.ficais (
    id TEXT PRIMARY KEY DEFAULT ('fic-' || gen_random_uuid()),
    numero TEXT NOT NULL UNIQUE,
    ano_letivo TEXT NOT NULL DEFAULT '2026',
    student_id TEXT REFERENCES public.students(id),
    student_nome TEXT NOT NULL,
    escola_id TEXT REFERENCES public.escolas(id),
    escola_nome TEXT NOT NULL,
    turma TEXT,
    turno TEXT,
    modalidade TEXT,
    periodo_faltas TEXT,
    total_faltas INT DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'Gerada',
    created_by TEXT,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);
```

---

## 3. Banco de Dados Local (IndexedDB — `FICAI4LocalDB`)

O banco local `FICAI4LocalDB` (versão 1) mantém as seguintes *object stores*:
- `students`: Armazena cadastro local de estudantes.
- `ficais`: Armazena o objeto completo da FICAI (incluindo metadados de formulário, dados das 6 seções e array `infoEntries` com a linha do tempo).
