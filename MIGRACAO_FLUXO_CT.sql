-- ==============================================================================
-- FICAI 4.0 — MIGRAÇÃO DO FLUXO ESCOLA <-> CONSELHO TUTELAR
-- Execute uma única vez no SQL Editor do Supabase antes de publicar esta versão.
-- Script idempotente: pode ser executado novamente sem duplicar colunas.
-- ==============================================================================

ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS section TEXT NOT NULL DEFAULT 'GERADOS';
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS status_tramitacao_ct TEXT NOT NULL DEFAULT 'CRIADA';
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS is_encaminhado_ct BOOLEAN NOT NULL DEFAULT false;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS has_devolutiva_ct BOOLEAN NOT NULL DEFAULT false;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS ct_enviado_em TIMESTAMPTZ;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS ct_enviado_por TEXT;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS ct_visualizado_em TIMESTAMPTZ;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS ct_visualizado_por TEXT;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS ct_devolvido_em TIMESTAMPTZ;
ALTER TABLE public.ficais ADD COLUMN IF NOT EXISTS ct_devolvido_por TEXT;
ALTER TABLE public.ficai_info_entries ADD COLUMN IF NOT EXISTS action TEXT;

CREATE INDEX IF NOT EXISTS idx_ficais_status_tramitacao_ct ON public.ficais(status_tramitacao_ct);
CREATE INDEX IF NOT EXISTS idx_ficais_escola_status_ct ON public.ficais(escola, status_tramitacao_ct);

-- Migração básica de registros legados, sem alterar situação pedagógica.
UPDATE public.ficais
SET status_tramitacao_ct = 'ENVIADA_AO_CT',
    is_encaminhado_ct = true,
    section = 'GERADOS'
WHERE status_tramitacao_ct = 'CRIADA'
  AND (status_fluxo = 'conselho_tutelar' OR situacao ILIKE '%Conselho Tutelar%');

UPDATE public.ficais
SET status_tramitacao_ct = 'DEVOLVIDA_PELO_CT',
    is_encaminhado_ct = true,
    has_devolutiva_ct = true,
    section = 'RECEBIDOS_CT'
WHERE situacao ILIKE '%Devolutiva CT%';

CREATE OR REPLACE FUNCTION public.ficai_marcar_visualizacao_ct(
    p_ficai_numero TEXT,
    p_visualizado_em TIMESTAMPTZ DEFAULT timezone('utc'::text, now()),
    p_visualizado_por TEXT DEFAULT 'Conselho Tutelar'
)
RETURNS SETOF public.ficais
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
    UPDATE public.ficais
    SET status_tramitacao_ct = 'VISUALIZADA_PELO_CT',
        is_encaminhado_ct = true,
        section = 'GERADOS',
        status_fluxo = 'conselho_tutelar',
        ct_visualizado_em = COALESCE(ct_visualizado_em, p_visualizado_em),
        ct_visualizado_por = COALESCE(NULLIF(ct_visualizado_por, ''), p_visualizado_por)
    WHERE numero = p_ficai_numero
      AND ct_visualizado_em IS NULL
      AND status_tramitacao_ct IN ('ENVIADA_AO_CT', 'VISUALIZADA_PELO_CT');

    RETURN QUERY SELECT * FROM public.ficais WHERE numero = p_ficai_numero;
END;
$$;

CREATE OR REPLACE FUNCTION public.ficai_devolver_para_escola(
    p_ficai_numero TEXT,
    p_devolvido_em TIMESTAMPTZ DEFAULT timezone('utc'::text, now()),
    p_devolvido_por TEXT DEFAULT 'Conselho Tutelar'
)
RETURNS SETOF public.ficais
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
    UPDATE public.ficais
    SET status_tramitacao_ct = 'DEVOLVIDA_PELO_CT',
        is_encaminhado_ct = true,
        has_devolutiva_ct = true,
        section = 'RECEBIDOS_CT',
        status_fluxo = 'em_analise',
        ct_devolvido_em = COALESCE(ct_devolvido_em, p_devolvido_em),
        ct_devolvido_por = COALESCE(NULLIF(ct_devolvido_por, ''), p_devolvido_por)
    WHERE numero = p_ficai_numero
      AND status_tramitacao_ct IN ('ENVIADA_AO_CT', 'VISUALIZADA_PELO_CT');

    RETURN QUERY SELECT * FROM public.ficais WHERE numero = p_ficai_numero;
END;
$$;

GRANT EXECUTE ON FUNCTION public.ficai_marcar_visualizacao_ct(TEXT, TIMESTAMPTZ, TEXT) TO anon, authenticated;
GRANT EXECUTE ON FUNCTION public.ficai_devolver_para_escola(TEXT, TIMESTAMPTZ, TEXT) TO anon, authenticated;
