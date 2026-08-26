import urllib.request, re, json, time, sys

maps_file = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\_MConverter.eu_maps.json'

schools_data = []

with open(maps_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            name = parts[0].strip().replace('"', '')
            link = parts[1].strip()
            schools_data.append({'name': name, 'link': link})

print(f"Total de {len(schools_data)} links do Google Maps encontrados no arquivo.", flush=True)

resolved_coords = {}

for idx, item in enumerate(schools_data):
    name = item['name']
    link = item['link']
    
    req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    lat, lng = None, None
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            final_url = resp.geturl()
            
            # Check @lat,lng
            m1 = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', final_url)
            if m1:
                lat = float(m1.group(1))
                lng = float(m1.group(2))
            else:
                # Check !3dLAT!4dLNG
                m2 = re.search(r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', final_url)
                if m2:
                    lat = float(m2.group(1))
                    lng = float(m2.group(2))
    except Exception as ex:
        print(f"[{idx+1}/{len(schools_data)}] Erro no link para {name}: {ex}", flush=True)

    if lat and lng:
        resolved_coords[name] = {'lat': round(lat, 7), 'lng': round(lng, 7), 'maps_link': link}
        print(f"[{idx+1}/{len(schools_data)}] {name} -> Lat: {lat}, Lng: {lng}", flush=True)
    else:
        print(f"[{idx+1}/{len(schools_data)}] {name} -> NÃO FOI POSSÍVEL EXTRAIR COORDENADAS", flush=True)
    
    time.sleep(0.3)

out_file = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\gmaps_exact_coords.json'
with open(out_file, 'w', encoding='utf-8') as out:
    json.dump(resolved_coords, out, ensure_ascii=False, indent=2)

print(f"\nSucesso! {len(resolved_coords)} escolas resolvidas e salvas em scratch/gmaps_exact_coords.json", flush=True)
