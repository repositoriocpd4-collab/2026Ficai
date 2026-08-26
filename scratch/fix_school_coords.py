import re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace coordinates for engenho, manoel soares, etc. in REGION_GEO_LOCATIONS
old_geo = """      'engenho': { lng: -43.7690, lat: -22.8580, label: 'Engenho, Itaguaí' },
      'manoel soares': { lng: -43.7690, lat: -22.8580, label: 'Engenho, Itaguaí' },
      'joao rosa': { lng: -43.7690, lat: -22.8580, label: 'Engenho, Itaguaí' },"""

new_geo = """      'ciep 497': { lng: -43.7883, lat: -22.8658, label: 'CIEP 497, Itaguaí' },
      'tupinamba': { lng: -43.7883, lat: -22.8658, label: 'CIEP 497, Itaguaí' },
      'tupinambá': { lng: -43.7883, lat: -22.8658, label: 'CIEP 497, Itaguaí' },
      'jardim ueda': { lng: -43.7883, lat: -22.8658, label: 'Jardim Ueda, Itaguaí' },
      'ueda': { lng: -43.7883, lat: -22.8658, label: 'Jardim Ueda, Itaguaí' },
      'engenho': { lng: -43.7883, lat: -22.8658, label: 'Engenho, Itaguaí' },
      'manoel soares': { lng: -43.7883, lat: -22.8658, label: 'Engenho, Itaguaí' },
      'joao rosa': { lng: -43.7883, lat: -22.8658, label: 'Engenho, Itaguaí' },"""

if old_geo in content:
    content = content.replace(old_geo, new_geo)
    print("1. Updated REGION_GEO_LOCATIONS successfully!")
else:
    print("Warning: old_geo not matched exactly!")

# 2. Add explicit school checks in geocodeAddress
old_geocode_func = """    function geocodeAddress(text, fallbackBase = { lng: -43.7770, lat: -22.8660 }) {
      if (!text) return { ...fallbackBase };
      const lower = text.toLowerCase();
      for (const [key, coords] of Object.entries(REGION_GEO_LOCATIONS)) {
        if (lower.includes(key)) {
          return { lng: coords.lng, lat: coords.lat };
        }
      }"""

new_geocode_func = """    function geocodeAddress(text, fallbackBase = { lng: -43.7770, lat: -22.8660 }) {
      if (!text) return { ...fallbackBase };
      const lower = text.toLowerCase();
      if (lower.includes('497') || lower.includes('tupinamba') || lower.includes('tupinambá')) {
        return { lng: -43.7883, lat: -22.8658 };
      }
      for (const [key, coords] of Object.entries(REGION_GEO_LOCATIONS)) {
        if (lower.includes(key)) {
          return { lng: coords.lng, lat: coords.lat };
        }
      }"""

if old_geocode_func in content:
    content = content.replace(old_geocode_func, new_geocode_func)
    print("2. Updated geocodeAddress successfully!")
else:
    print("Warning: old_geocode_func not matched exactly!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved index.html successfully!")
