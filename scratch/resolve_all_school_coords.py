import json, urllib.request, urllib.parse, time, re

with open(r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\escolas.json', 'r', encoding='utf-8') as f:
    escolas = json.load(f)

print(f"Resolvendo coordenadas para {len(escolas)} escolas...")

coords_map = {}

# Known user-supplied exact coordinates overrides
USER_EXACT_OVERC = {
    'esc-33127530': {'lat': -22.8535216, 'lng': -43.7678924, 'label': 'E. M. Elmira Figueira'}, # User explicit
    'esc-33044872': {'lat': -22.8658521, 'lng': -43.7883110, 'label': 'CIEP 497 Munic. Prof.ª Sílvia Tupinambá'}, # User explicit
}

results = []

for i, e in enumerate(escolas):
    eid = e.get('id', '')
    nome = e.get('nome', '')
    end = e.get('endereco', '')
    bairro = e.get('bairro', '')
    
    if eid in USER_EXACT_OVERC:
        c = USER_EXACT_OVERC[eid]
        results.append({'id': eid, 'nome': nome, 'lat': c['lat'], 'lng': c['lng'], 'source': 'user_explicit'})
        print(f"[{i+1}/{len(escolas)}] {nome} -> EXACT (User): lat={c['lat']}, lng={c['lng']}")
        continue

    # Try Nominatim search with school name + Itaguai
    clean_name = re.sub(r'^(E\.?\s*M\.?|C\.?\s*M\.?|CIEP|E\.?\s*E\.?\s*M\.?)\s*', '', nome).strip()
    query = f"{clean_name}, {bairro}, Itaguai, Rio de Janeiro, Brasil"
    url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query)}&format=json&limit=1"
    
    found_coords = None
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'FICAI-Geocoder/1.0 (edu.itaguai.rj.gov.br)'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            if data and len(data) > 0:
                found_coords = {'lat': float(data[0]['lat']), 'lng': float(data[0]['lon']), 'source': 'nominatim_school'}
    except Exception as ex:
        pass
    
    if not found_coords and end:
        # Fallback to searching address
        clean_end = re.sub(r'\(.*?\)', '', end).replace('s/n', '').replace('nº', '').strip()
        query_end = f"{clean_end}, Itaguai, Rio de Janeiro, Brasil"
        url_end = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query_end)}&format=json&limit=1"
        try:
            req = urllib.request.Request(url_end, headers={'User-Agent': 'FICAI-Geocoder/1.0 (edu.itaguai.rj.gov.br)'})
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if data and len(data) > 0:
                    found_coords = {'lat': float(data[0]['lat']), 'lng': float(data[0]['lon']), 'source': 'nominatim_address'}
        except Exception as ex:
            pass

    if not found_coords and bairro:
        # Fallback to bairro
        query_bairro = f"Bairro {bairro}, Itaguai, Rio de Janeiro, Brasil"
        url_bairro = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query_bairro)}&format=json&limit=1"
        try:
            req = urllib.request.Request(url_bairro, headers={'User-Agent': 'FICAI-Geocoder/1.0 (edu.itaguai.rj.gov.br)'})
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if data and len(data) > 0:
                    found_coords = {'lat': float(data[0]['lat']), 'lng': float(data[0]['lon']), 'source': 'nominatim_bairro'}
        except Exception as ex:
            pass

    if not found_coords:
        # Generic center of Itaguaí fallback
        found_coords = {'lat': -22.8660, 'lng': -43.7770, 'source': 'itaguai_center_fallback'}

    results.append({
        'id': eid,
        'nome': nome,
        'lat': round(found_coords['lat'], 6),
        'lng': round(found_coords['lng'], 6),
        'source': found_coords['source']
    })
    print(f"[{i+1}/{len(escolas)}] {nome} ({bairro}) -> lat={found_coords['lat']:.6f}, lng={found_coords['lng']:.6f} [{found_coords['source']}]")
    time.sleep(0.5)

with open(r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\escolas_coords_resolved.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("\nCoordenadas de todas as 64 escolas resolvidas e salvas em scratch/escolas_coords_resolved.json!")
