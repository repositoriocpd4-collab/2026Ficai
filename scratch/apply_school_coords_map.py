import json, re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

with open(r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\scratch\school_map.json', 'r', encoding='utf-8') as f:
    school_map = json.load(f)

# Convert school_map into a JS object string
js_school_map = json.dumps(school_map, ensure_ascii=False, indent=2)

# Create the EXACT_SCHOOL_COORDINATES JS variable and updated getMapCoordinatesForFicai function
old_geo_start = "    let infoMapInstance = null;"

new_geo_start = f"""    const EXACT_SCHOOL_COORDINATES = {js_school_map};

    let infoMapInstance = null;"""

if old_geo_start in content and "const EXACT_SCHOOL_COORDINATES =" not in content:
    content = content.replace(old_geo_start, new_geo_start)
    print("1. Injected EXACT_SCHOOL_COORDINATES successfully!")
else:
    print("1. EXACT_SCHOOL_COORDINATES already present or target not found.")

# Update geocodeAddress to check EXACT_SCHOOL_COORDINATES and Elmira/CIEP overrides
old_geocode = """    function geocodeAddress(text, fallbackBase = { lng: -43.7770, lat: -22.8660 }) {
      if (!text) return { ...fallbackBase };
      const lower = text.toLowerCase();
      if (lower.includes('497') || lower.includes('tupinamba') || lower.includes('tupinambá')) {
        return { lng: -43.788311, lat: -22.8658521 };
      }
      for (const [key, coords] of Object.entries(REGION_GEO_LOCATIONS)) {
        if (lower.includes(key)) {
          return { lng: coords.lng, lat: coords.lat };
        }
      }"""

new_geocode = """    function geocodeAddress(text, fallbackBase = { lng: -43.7770, lat: -22.8660 }) {
      if (!text) return { ...fallbackBase };
      const lower = text.toLowerCase();

      // 1. Verificação explícita por nome exato da escola
      if (typeof EXACT_SCHOOL_COORDINATES !== 'undefined') {
        for (const [sName, sCoords] of Object.entries(EXACT_SCHOOL_COORDINATES)) {
          if (sameText(lower, sName.toLowerCase()) || lower.includes(sName.toLowerCase())) {
            return { lng: sCoords.lng, lat: sCoords.lat };
          }
        }
      }

      // 2. Overrides de alta precisão fornecidos pelo usuário
      if (lower.includes('elmira') || (lower.includes('elmir') && lower.includes('figueira'))) {
        return { lng: -43.7678924, lat: -22.8535216 };
      }
      if (lower.includes('497') || lower.includes('tupinamba') || lower.includes('tupinambá')) {
        return { lng: -43.788311, lat: -22.8658521 };
      }

      // 3. Busca por termos regionais e bairros
      for (const [key, coords] of Object.entries(REGION_GEO_LOCATIONS)) {
        if (lower.includes(key)) {
          return { lng: coords.lng, lat: coords.lat };
        }
      }"""

if old_geocode in content:
    content = content.replace(old_geocode, new_geocode)
    print("2. Updated geocodeAddress successfully!")
else:
    print("Warning: old_geocode not matched exactly!")

# Update getMapCoordinatesForFicai
old_get_coords = """    function getMapCoordinatesForFicai(r) {
      const d = r.data || {};
      const escolaName = r.escola || d.escola || 'Colégio M. Senador Teotônio Vilella';
      let escolaEndereco = d.escolaEndereco || '';
      const schoolList = (configData && configData.escolas) ? configData.escolas : [];
      const foundSchool = schoolList.find(s => s.nome === escolaName || (s.id && s.id === escolaName) || sameText(s.nome, escolaName));
      if (foundSchool) { if (!escolaEndereco) escolaEndereco = foundSchool.endereco; }
      const escolaCoords = geocodeAddress(`${escolaName} ${escolaEndereco}`, { lng: -43.7680, lat: -22.8600 });
      const alunoName = r.aluno || d.nomeCompleto || 'Aluno';
      const alunoEndereco = d.residencia || r.residencia || 'Endereço residencial cadastrado';
      const alunoCoords = geocodeAddress(`${alunoEndereco} ${alunoName}`, { lng: -43.9430, lat: -22.9230 });
      return {
        escola: { name: foundSchool?.nome || escolaName, endereco: escolaEndereco, lng: escolaCoords.lng, lat: escolaCoords.lat },
        aluno: { name: alunoName, endereco: alunoEndereco, lng: alunoCoords.lng, lat: alunoCoords.lat }
      };
    }"""

new_get_coords = """    function getMapCoordinatesForFicai(r) {
      const d = r.data || {};
      const escolaName = r.escola || d.escola || 'E. M. Elmira Figueira';
      let escolaEndereco = d.escolaEndereco || '';
      const schoolList = (configData && configData.escolas) ? configData.escolas : [];
      const foundSchool = schoolList.find(s => s.nome === escolaName || (s.id && s.id === escolaName) || sameText(s.nome, escolaName));
      if (foundSchool) { if (!escolaEndereco) escolaEndereco = foundSchool.endereco; }

      let escolaCoords = null;

      // Buscar primeiro no mapa de coordenadas exatas
      if (typeof EXACT_SCHOOL_COORDINATES !== 'undefined') {
        const exactMatch = Object.entries(EXACT_SCHOOL_COORDINATES).find(([n]) => sameText(n, escolaName) || n.toLowerCase() === escolaName.toLowerCase());
        if (exactMatch) {
          escolaCoords = { lng: exactMatch[1].lng, lat: exactMatch[1].lat };
        }
      }

      if (!escolaCoords) {
        escolaCoords = geocodeAddress(`${escolaName} ${escolaEndereco}`, { lng: -43.7678924, lat: -22.8535216 });
      }

      const alunoName = r.aluno || d.nomeCompleto || 'Aluno';
      const alunoEndereco = d.residencia || r.residencia || 'Endereço residencial cadastrado';
      const alunoCoords = geocodeAddress(`${alunoEndereco} ${alunoName}`, { lng: -43.9430, lat: -22.9230 });
      return {
        escola: { name: foundSchool?.nome || escolaName, endereco: escolaEndereco, lng: escolaCoords.lng, lat: escolaCoords.lat },
        aluno: { name: alunoName, endereco: alunoEndereco, lng: alunoCoords.lng, lat: alunoCoords.lat }
      };
    }"""

if old_get_coords in content:
    content = content.replace(old_get_coords, new_get_coords)
    print("3. Updated getMapCoordinatesForFicai successfully!")
else:
    print("Warning: old_get_coords not matched exactly!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully!")
