import re

path = r'c:\Users\Usuário\Desktop\FICAI_4.0_PRONTO_FLUXO_CT\FICAI_4.0_PRONTO_FLUXO_CT\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Page 1 logo
p1_match = re.search(r'<div class="print-page" id="printPage">.*?<img class="p-crest"\s+src="([^"]+)"', content, re.DOTALL)
p2_match = re.search(r'<div class="print-page page-2">.*?<img class="p-crest"\s+src="([^"]+)"', content, re.DOTALL)

if p1_match and p2_match:
    src1 = p1_match.group(1)
    src2 = p2_match.group(1)
    print("P1 src len:", len(src1))
    print("P2 src len:", len(src2))
    print("Are they equal?", src1 == src2)
    if src1 != src2:
        print("They are DIFFERENT! Let's force P2 src = P1 src.")
        new_content = content[:p2_match.start(1)] + src1 + content[p2_match.end(1):]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated P2 src to match P1 src exactly!")
