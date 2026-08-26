import json, re

# Load resolved Google Maps coordinates
gmaps_file = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\gmaps_exact_coords.json'
with open(gmaps_file, 'r', encoding='utf-8') as f:
    gmaps_coords = json.load(f)

print(f"Total de {len(gmaps_coords)} coordenadas extraidas do Google Maps.")

# Build robust dictionary including alias variations
final_school_coords = {}

for name, data in gmaps_coords.items():
    lat = data['lat']
    lng = data['lng']
    final_school_coords[name] = {'lat': lat, 'lng': lng}
    
    # Add alias variations for Elmir / Elmira Figueira
    if 'Elmira Figueira' in name or 'Elmir Figueira' in name:
        final_school_coords['E. M. Elmir Figueira'] = {'lat': lat, 'lng': lng}
        final_school_coords['E.M. Elmir Figueira'] = {'lat': lat, 'lng': lng}
        final_school_coords['E. M. Elmira Figueira'] = {'lat': lat, 'lng': lng}
        final_school_coords['E.M. Elmira Figueira'] = {'lat': lat, 'lng': lng}

    # Add alias for CIEP 497
    if '497' in name:
        final_school_coords['CIEP 497'] = {'lat': lat, 'lng': lng}
        final_school_coords['CIEP 497 Munic. Prof.ª Sílvia Tupinambá'] = {'lat': lat, 'lng': lng}

# Also add fallback for schools that didn't resolve automatically
user_explicit = {
    'E. M. Alexandre Ignácio': {'lat': -22.8641963, 'lng': -43.8015295},
    'E. M. Prefeito Abeilard Goulart de Souza': {'lat': -22.8633069, 'lng': -43.7722655},
    'E. M. São Sebastião': {'lat': -22.8050000, 'lng': -43.7280000},
    'CIEP 496 Munic. Maestro Francisco Mignone': {'lat': -22.8655927, 'lng': -43.7546781},
    'C.M. Rita Ferreira Feijó': {'lat': -22.8383786, 'lng': -43.7948111}
}

for name, coords in user_explicit.items():
    if name not in final_school_coords:
        final_school_coords[name] = coords

print(f"Total final de mapeamentos com variacoes: {len(final_school_coords)}")

# Now read index.html and update EXACT_SCHOOL_COORDINATES
index_path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

js_coords = json.dumps(final_school_coords, ensure_ascii=False, indent=2)

# Replace EXACT_SCHOOL_COORDINATES definition
regex_exact = r'const EXACT_SCHOOL_COORDINATES = \{.*?\};'
if re.search(regex_exact, content, re.DOTALL):
    content = re.sub(regex_exact, f'const EXACT_SCHOOL_COORDINATES = {js_coords};', content, flags=re.DOTALL)
    print("[OK] EXACT_SCHOOL_COORDINATES atualizado com sucesso no index.html!")
else:
    print("[AVISO] Nao encontrou EXACT_SCHOOL_COORDINATES via regex.")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] index.html salvo com as coordenadas exatas do Google Maps!")
