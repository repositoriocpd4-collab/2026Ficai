import json, re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract configData.escolas JSON block
match = re.search(r'"escolas":\s*(\[\s*\{.*?\}\s*\])', content, re.DOTALL)
if match:
    escolas_json = match.group(1)
    escolas = json.loads(escolas_json)
    print(f"Total escolas encontradas: {len(escolas)}\n")
    for i, e in enumerate(escolas):
        nome = e.get('nome', '')
        end = e.get('endereco', '')
        bairro = e.get('bairro', '')
        link = e.get('maps_link', '')
        print(f"{i+1:02d}. {nome}")
        print(f"    Endereço: {end}")
        print(f"    Bairro: {bairro}")
        print(f"    Maps Link: {link}\n")
else:
    print("Não encontrou escolas")
