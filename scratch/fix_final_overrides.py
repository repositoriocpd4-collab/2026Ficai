import json, re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract EXACT_SCHOOL_COORDINATES
match = re.search(r'const EXACT_SCHOOL_COORDINATES = (\{.*?\});', content, re.DOTALL)
if match:
    coords_dict = json.loads(match.group(1))
    
    # Set exact user overrides for Elmira/Elmir Figueira and CIEP 497
    elmira_coords = {'lat': -22.8535216, 'lng': -43.7678924}
    ciep_coords = {'lat': -22.8658521, 'lng': -43.7883110}
    
    coords_dict['E. M. Elmira Figueira'] = elmira_coords
    coords_dict['E.M. Elmira Figueira'] = elmira_coords
    coords_dict['E. M. Elmir Figueira'] = elmira_coords
    coords_dict['E.M. Elmir Figueira'] = elmira_coords

    coords_dict['CIEP 497'] = ciep_coords
    coords_dict['CIEP 497 Munic. Prof.ª Sílvia Tupinambá'] = ciep_coords
    
    js_coords = json.dumps(coords_dict, ensure_ascii=False, indent=2)
    content = re.sub(r'const EXACT_SCHOOL_COORDINATES = \{.*?\};', f'const EXACT_SCHOOL_COORDINATES = {js_coords};', content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("[OK] Coordenadas atualizadas com sucesso no index.html!")
else:
    print("[ERRO] Nao encontrou EXACT_SCHOOL_COORDINATES")
