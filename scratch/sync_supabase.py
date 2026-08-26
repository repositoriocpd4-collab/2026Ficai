import json
import urllib.request

SUPABASE_URL = 'https://ojvxsrvmmkjxfgyczypm.supabase.co/rest/v1'
ANON_KEY = 'sb_publishable_JDPRSMCStt58M2CWLfNHtA_F1zuxvvG'

headers = {
    'apikey': ANON_KEY,
    'Authorization': f'Bearer {ANON_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'resolution=merge-duplicates,return=representation'
}

def sync_escolas():
    with open('scratch/escolas_index.json', 'r', encoding='utf-8') as f:
        escolas = json.load(f)

    print(f'Carregadas {len(escolas)} escolas do JSON.')

    seen_ids = set()
    formatted_escolas = []
    
    for idx, e in enumerate(escolas):
        rec_id = e.get('id')
        if rec_id in seen_ids or not rec_id:
            rec_id = f"{rec_id}-dup-{idx+1}"
        seen_ids.add(rec_id)

        rec = {
            'id': rec_id,
            'nome': e.get('nome') or '',
            'endereco': e.get('endereco') or '',
            'telefone': e.get('telefone') or '',
            'email': e.get('email') or '',
            'ativo': e.get('ativo', True)
        }
        formatted_escolas.append(rec)

    success_count = 0
    errors = []

    # Envia individualmente ou em lote para garantir sincronia limpa
    for rec in formatted_escolas:
        req = urllib.request.Request(
            f'{SUPABASE_URL}/escolas',
            data=json.dumps([rec]).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                success_count += len(data)
        except urllib.error.HTTPError as err:
            err_body = err.read().decode('utf-8')
            errors.append((rec['nome'], err.code, err_body))
        except Exception as ex:
            errors.append((rec['nome'], 500, str(ex)))

    print(f'Sincronização concluída!')
    print(f'Sucesso: {success_count} / {len(formatted_escolas)} escolas cadastradas no Supabase.')
    if errors:
        print(f'Erros registrados: {len(errors)}')
        for err in errors[:5]:
            print(' - Escola:', err[0], '| Erro:', err[1], err[2])

if __name__ == '__main__':
    sync_escolas()
