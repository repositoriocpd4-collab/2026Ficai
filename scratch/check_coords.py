import json, re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'const EXACT_SCHOOL_COORDINATES =' in content:
    print("[OK] EXACT_SCHOOL_COORDINATES presente no index.html!")

match_elmira = re.search(r'"E\. M\. Elmira Figueira":\s*\{\s*"lat":\s*(-?\d+\.\d+),\s*"lng":\s*(-?\d+\.\d+)', content)
if match_elmira:
    print(f"[OK] E. M. Elmira Figueira -> Lat: {match_elmira.group(1)}, Lng: {match_elmira.group(2)}")

match_ciep = re.search(r'"CIEP 497[^"]*":\s*\{\s*"lat":\s*(-?\d+\.\d+),\s*"lng":\s*(-?\d+\.\d+)', content)
if match_ciep:
    print(f"[OK] CIEP 497 -> Lat: {match_ciep.group(1)}, Lng: {match_ciep.group(2)}")
