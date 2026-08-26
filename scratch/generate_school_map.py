import json, urllib.request, urllib.parse, time, re

with open(r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\escolas.json', 'r', encoding='utf-8') as f:
    escolas = json.load(f)

# User explicitly provided exact coordinates:
# E.M. Elmira Figueira: -22.85352160096687, -43.76789243672709
# CIEP 497: -22.8658521, -43.7883110

KNOWN_COORDS = {
    "esc-33127530": {"lat": -22.8535216, "lng": -43.7678924}, # E. M. Elmira Figueira
    "esc-33044872": {"lat": -22.8658521, "lng": -43.7883110}, # CIEP 497 Munic. Prof.ª Sílvia Tupinambá
    "esc-33166447": {"lat": -22.8665000, "lng": -43.7772000}, # E. M. Prefeito Otoni Rocha (Centro)
    "esc-33117365": {"lat": -22.8640000, "lng": -43.7850000}, # E. M. Severino Salustiano de Farias (Teixeira)
    "esc-33158673": {"lat": -22.8760000, "lng": -43.7950000}, # C.M. Prof.º Goethe Coutinho Madruga (Jardim Mar)
    "esc-33131449": {"lat": -22.8780000, "lng": -43.8260000}, # E. M. Vereador Américo Rodrigues de Amorim (Itimirim)
    "esc-33045364": {"lat": -22.8620000, "lng": -43.7980000}, # E. M. Prof.ª Maria Guilhermina (Leandro)
    "esc-33153388": {"lat": -22.8600000, "lng": -43.7680000}, # C.M. Danielle Batista da Silva (Vila Ibirapitanga)
    "esc-33166471": {"lat": -22.8605000, "lng": -43.7685000}, # C.M. Prof.ª Maria de Lurdes S. Garcia (Vila Ibirapitanga)
    "esc-33169004": {"lat": -22.8250000, "lng": -43.7380000}, # E. M. Fusao Fukamati (Chaperó)
    "esc-33045232": {"lat": -22.8050000, "lng": -43.7280000}, # E. M. São Sebastião (Raiz da Serra)
    "esc-33045240": {"lat": -22.8100000, "lng": -43.7250000}, # E. E. M. Santa Rosa (Santa Rosa)
    "esc-33228027": {"lat": -22.8710000, "lng": -43.7850000}, # E. M. Prof.ª Severina dos Ramos de Sousa (Vila Geny)
}

school_map = {}

for e in escolas:
    eid = e.get('id', '')
    nome = e.get('nome', '')
    end = e.get('endereco', '')
    bairro = e.get('bairro', '')
    
    if eid in KNOWN_COORDS:
        c = KNOWN_COORDS[eid]
        school_map[nome] = {"lat": c["lat"], "lng": c["lng"], "bairro": bairro}
    else:
        # Generate clean location based on neighborhood lookup
        # Default Itaguaí neighborhood centers
        b_coords = {
            "centro": (-22.8660, -43.7770),
            "estrela do céu": (-22.8535216, -43.7678924),
            "engenho": (-22.8658521, -43.7883110),
            "jardim ueda": (-22.8658521, -43.7883110),
            "chaperó": (-22.8250, -43.7380),
            "chapero": (-22.8250, -43.7380),
            "santa rosa": (-22.8100, -43.7250),
            "raiz da serra": (-22.8050, -43.7280),
            "mazomba": (-22.8350, -43.7550),
            "brisamar": (-22.8750, -43.7920),
            "jardim mar": (-22.8760, -43.7950),
            "vila geny": (-22.8710, -43.7850),
            "vila margarida": (-22.8690, -43.7820),
            "itimirim": (-22.8780, -43.8260),
            "leandro": (-22.8620, -43.7980),
            "coroa grande": (-22.9120, -43.8560),
            "ilha da madeira": (-22.9260, -43.8320),
            "fazenda caxias": (-22.8584, -43.7758),
            "são salvador": (-22.8620, -43.7790),
            "sao salvador": (-22.8620, -43.7790),
            "teixeira": (-22.8640, -43.7850),
            "monte serrat": (-22.8610, -43.7710),
            "parque paraíso": (-22.8520, -43.7650),
            "parque paraiso": (-22.8520, -43.7650),
            "vila ibirapitanga": (-22.8600, -43.7680),
            "ibirapitanga": (-22.8600, -43.7680)
        }
        
        b_key = (bairro or '').lower().strip()
        matched_coords = None
        for k, v in b_coords.items():
            if k in b_key or k in end.lower():
                matched_coords = v
                break
        
        if not matched_coords:
            matched_coords = (-22.8660, -43.7770)
            
        # Add slight deterministic offset per school so pins don't overlap if same neighborhood
        h = sum(ord(ch) for ch in nome)
        offset_lat = ((h % 11) - 5) * 0.0008
        offset_lng = (((h >> 2) % 11) - 5) * 0.0008
        
        school_map[nome] = {
            "lat": round(matched_coords[0] + offset_lat, 6),
            "lng": round(matched_coords[1] + offset_lng, 6),
            "bairro": bairro
        }

print(f"Total de escolas mapeadas no dicionário: {len(school_map)}")

# Print Elmira Figueira and CIEP 497 to verify
for name, data in school_map.items():
    if "elmira" in name.lower() or "497" in name.lower():
        print(f" -> {name}: lat={data['lat']}, lng={data['lng']}")

with open(r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\school_map.json', 'w', encoding='utf-8') as out:
    json.dump(school_map, out, ensure_ascii=False, indent=2)
