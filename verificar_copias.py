from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
items=json.loads((root/'documentacion/verificacion_y_huellas.json').read_text(encoding='utf-8'))
errors=0
for x in items:
    if 'sha256' not in x: continue
    p=root/x['archivo']
    ok=p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256']
    print('OK' if ok else 'ERROR',x['archivo'])
    errors+=not ok
raise SystemExit(1 if errors else 0)
