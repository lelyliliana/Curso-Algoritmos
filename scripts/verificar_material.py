from pathlib import Path
from urllib.parse import unquote
import re, json

r = Path(__file__).resolve().parents[1]
errors = []
items = json.loads((r / "laboratorios/catalogo.json").read_text())
if [x["unidad"] for x in items] != list(range(1, 26)):
    errors.append("catalogo debe cubrir 1..25")
for item in items:
    p = r / item["programa"]
    u = r / p.relative_to(r).parts[0]
    for f in [p, u / "LABORATORIO.md", u / "SOLUCIONES.md"]:
        if not f.is_file():
            errors.append(str(f) + " ausente")
for f in r.rglob("*.md"):
    if ".git" in f.parts:
        continue
    for link in re.findall(r"\]\(([^\s)]+)", f.read_text()):
        if re.match(r"^(https?:|mailto:|#)", link):
            continue
        target = unquote(link.split("#")[0].split("?")[0])
        if target and not (f.parent / target).exists():
            errors.append(str(f.relative_to(r)) + ": " + target)
print("\n".join(errors) if errors else "OK: 25 laboratorios y enlaces locales")
raise SystemExit(bool(errors))
