"""Caso ejecutable de unidad 06; ejecutar desde cualquier carpeta."""

import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "laboratorios"))
from algoritmos import demostracion

if __name__ == "__main__":
    print(json.dumps(demostracion(6), ensure_ascii=False, sort_keys=True))
