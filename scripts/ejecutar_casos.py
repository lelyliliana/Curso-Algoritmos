import subprocess, sys, json, argparse
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("--unidad", type=int)
a = p.parse_args()
r = Path(__file__).resolve().parents[1]
items = json.loads((r / "laboratorios/catalogo.json").read_text())
if a.unidad is not None and a.unidad not in range(1, 26):
    raise SystemExit("Unidad debe estar entre 1 y25")
for item in items:
    if a.unidad is not None and item["unidad"] != a.unidad:
        continue
    resultado = subprocess.run(
        [sys.executable, str(r / item["programa"])],
        capture_output=True,
        text=True,
        check=True,
        cwd=r,
    )
    json.loads(resultado.stdout)
    print(f"Unidad {item['unidad']:02d}: OK")
