import json
import urllib.request
import openpyxl

SUPABASE_URL = 'https://ojvxsrvmmkjxfgyczypm.supabase.co/rest/v1'
ANON_KEY = 'sb_publishable_JDPRSMCStt58M2CWLfNHtA_F1zuxvvG'

headers = {
    'apikey': ANON_KEY,
    'Authorization': f'Bearer {ANON_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'resolution=merge-duplicates,return=representation'
}

def post_batch(table_name, records):
    if not records:
        return 0
    req = urllib.request.Request(
        f'{SUPABASE_URL}/{table_name}',
        data=json.dumps(records, ensure_ascii=False).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f'[{table_name}] Sincronizados {len(res)} registros no Supabase.')
            return len(res)
    except urllib.error.HTTPError as err:
        print(f'[{table_name}] Erro HTTP {err.code}: {err.read().decode("utf-8")}')
        return 0
    except Exception as ex:
        print(f'[{table_name}] Erro: {ex}')
        return 0

def sync_all():
    print('Iniciando sincronização completa de tabelas com o Supabase...')
    
    # 1. Modalidades
    modalidades = [
        {'id': 'mod-1', 'nome': 'Educação Infantil', 'descricao': 'Berçário, Creche e Pré-Escola', 'ativo': True},
        {'id': 'mod-2', 'nome': 'Ensino Fundamental I', 'descricao': '1º ao 5º Ano', 'ativo': True},
        {'id': 'mod-3', 'nome': 'Ensino Fundamental II', 'descricao': '6º ao 9º Ano', 'ativo': True},
        {'id': 'mod-4', 'nome': 'EJA - Educação de Jovens e Adultos', 'descricao': 'Fases I a IV', 'ativo': True},
        {'id': 'mod-5', 'nome': 'Educação Especial AEE', 'descricao': 'Atendimento Educacional Especializado', 'ativo': True}
    ]
    post_batch('modalidades', modalidades)

    # 2. Turmas
    turmas = [
        {'id': 'tur-1', 'ano': '6º Ano', 'turma': '6º Ano A (6A)', 'turno': 'Manhã', 'modalidade': 'Ensino Fundamental II', 'escola': 'E.M. Elmir Figueira', 'ativo': True},
        {'id': 'tur-2', 'ano': '7º Ano', 'turma': '7º Ano B (7B)', 'turno': 'Manhã', 'modalidade': 'Ensino Fundamental II', 'escola': 'E.M. Elmir Figueira', 'ativo': True},
        {'id': 'tur-3', 'ano': '8º Ano', 'turma': '8º Ano A (8A)', 'turno': 'Tarde', 'modalidade': 'Ensino Fundamental II', 'escola': 'E.M. Severino Salustiano de Farias', 'ativo': True},
        {'id': 'tur-4', 'ano': '9º Ano', 'turma': '9º Ano C (9C)', 'turno': 'Tarde', 'modalidade': 'Ensino Fundamental II', 'escola': 'E.M. Prefeito Otoni Rocha', 'ativo': True},
        {'id': 'tur-5', 'ano': 'Pré-Escola', 'turma': 'Pré II A', 'turno': 'Manhã', 'modalidade': 'Educação Infantil', 'escola': 'C.M. Prof.ª Goethe Coutinho Madruga', 'ativo': True},
        {'id': 'tur-6', 'ano': 'EJA', 'turma': 'EJA Fase III', 'turno': 'Noite', 'modalidade': 'EJA', 'escola': 'CIEP 497 Munic. Prof.ª Sílvia Tupinambá', 'ativo': True}
    ]
    post_batch('turmas', turmas)

    # 3. Usuários
    usuarios = [
        {'id': 'usr-admin-cpd', 'usuario': 'CPD Infra / SMEDU', 'email': 'cpdinfra@edu.itaguai.rj.gov.br', 'nivel': 'Administrador', 'cargo': 'Assessor Técnico', 'funcao': 'Administração Geral do Sistema', 'unidade': 'SMEDU / CPD', 'ativo': True},
        {'id': 'usr-escola-elmir', 'usuario': 'Secretaria E.M. Elmir Figueira', 'email': 'em.elmirfigueira@edu.itaguai.rj.gov.br', 'nivel': 'Escola', 'cargo': 'Secretário Escolar', 'funcao': 'Emissão e Gestão de FICAIs', 'unidade': 'E.M. Elmir Figueira', 'ativo': True},
        {'id': 'usr-conselho-1', 'usuario': 'Conselho Tutelar Itaguaí', 'email': 'conselhotutelar@itaguai.rj.gov.br', 'nivel': 'Conselho Tutelar', 'cargo': 'Conselheiro Tutelar', 'funcao': 'Acompanhamento de Diligências', 'unidade': 'Conselho Tutelar', 'ativo': True}
    ]
    post_batch('usuarios', usuarios)

    # 4. Permissões
    permissoes = [
        {'id': 'perm-admin-all', 'perfil': 'Administrador', 'modulo': 'Todos os Módulos', 'visualizar': True, 'cadastrar': True, 'editar': True, 'excluir': True},
        {'id': 'perm-escola-ficai', 'perfil': 'Escola', 'modulo': 'Gerar e Visualizar FICAIs', 'visualizar': True, 'cadastrar': True, 'editar': True, 'excluir': False},
        {'id': 'perm-ct-diligencias', 'perfil': 'Conselho Tutelar', 'modulo': 'Painel CT e Devolutivas', 'visualizar': True, 'cadastrar': True, 'editar': True, 'excluir': False}
    ]
    post_batch('permissoes', permissoes)

    # 5. Pessoas
    pessoas = [
        {'id': 'pes-1', 'tipo': 'Diretor', 'nome': 'Luciane Leal do Valle', 'matricula': '10482', 'unidade': 'E. M. Vereador Américo Rodrigues de Amorim', 'telefone': '(21) 3782-3064', 'email': 'em.veramericorodriguesdeamorim@edu.itaguai.rj.gov.br', 'periodo': '2026', 'ativo': True},
        {'id': 'pes-2', 'tipo': 'Diretor', 'nome': 'Tania Maria da Silva Medeiros', 'matricula': '10594', 'unidade': 'E. M. Prefeito Otoni Rocha', 'telefone': '(21) 3782-3041', 'email': 'em.prefotonirocha@edu.itaguai.rj.gov.br', 'periodo': '2026', 'ativo': True},
        {'id': 'pes-3', 'tipo': 'Orientador', 'nome': 'Maria Oliveira', 'matricula': '12840', 'unidade': 'E.M. Elmir Figueira', 'telefone': '(21) 99887-1122', 'email': 'maria.oliveira@edu.itaguai.rj.gov.br', 'periodo': '2026', 'ativo': True}
    ]
    post_batch('pessoas', pessoas)

    # 6. Procedimentos
    procedimentos = [
        {'id': 'proc-1', 'ordem': 1, 'nome': 'Contato telefônico / mensagem com os pais ou responsáveis', 'ativo': True},
        {'id': 'proc-2', 'ordem': 2, 'nome': 'Visita domiciliar realizada pela equipe escolar / Orientação', 'ativo': True},
        {'id': 'proc-3', 'ordem': 3, 'nome': 'Convocação presencial do responsável na unidade escolar', 'ativo': True},
        {'id': 'proc-4', 'ordem': 4, 'nome': 'Encaminhamento à rede de proteção social (CRAS / CREAS)', 'ativo': True},
        {'id': 'proc-5', 'ordem': 5, 'nome': 'Encaminhamento à Unidade Básica de Saúde / Saúde Mental (CAPSi)', 'ativo': True},
        {'id': 'proc-6', 'ordem': 6, 'nome': 'Notificação formal ao Conselho Tutelar', 'ativo': True},
        {'id': 'proc-7', 'ordem': 7, 'nome': 'Registro em ata de reunião pedagógica e termo de compromisso', 'ativo': True}
    ]
    post_batch('procedimentos', procedimentos)

    # 7. Motivos de Ausência
    motivos = [
        {'id': 'mot-1', 'grupo': 'Sociocultural / Familiar', 'nome': 'Trabalho infantil / Apoio à renda familiar', 'ativo': True},
        {'id': 'mot-2', 'grupo': 'Sociocultural / Familiar', 'nome': 'Negligência ou falta de acompanhamento responsável', 'ativo': True},
        {'id': 'mot-3', 'grupo': 'Sociocultural / Familiar', 'nome': 'Cuidado com irmãos menores ou familiares doentes', 'ativo': True},
        {'id': 'mot-4', 'grupo': 'Saúde / Psicológico', 'nome': 'Problemas de saúde crônicos / Tratamento médico', 'ativo': True},
        {'id': 'mot-5', 'grupo': 'Saúde / Psicológico', 'nome': 'Sofrimento psíquico / Depressão / Ansiedade grave', 'ativo': True},
        {'id': 'mot-6', 'grupo': 'Infraestrutura / Acesso', 'nome': 'Dificuldades com transporte escolar / Distância da escola', 'ativo': True},
        {'id': 'mot-7', 'grupo': 'Infraestrutura / Acesso', 'nome': 'Mudança recente de endereço / Dificuldade de adaptação', 'ativo': True},
        {'id': 'mot-8', 'grupo': 'Pedagógico', 'nome': 'Desinteresse escolar / Defasagem idade-série', 'ativo': True},
        {'id': 'mot-9', 'grupo': 'Pedagógico', 'nome': 'Bullying / Conflitos com colegas ou equipe', 'ativo': True}
    ]
    post_batch('motivos', motivos)

    print('Sincronização de todas as tabelas concluída com sucesso!')

if __name__ == '__main__':
    sync_all()
