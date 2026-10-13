"""Compila/ejecuta ejemplos Java y JavaScript y verifica estrategias avanzadas."""

from pathlib import Path
import argparse, subprocess, tempfile, shutil, json

p = argparse.ArgumentParser()
p.add_argument("--jdk")
a = p.parse_args()
r = Path(__file__).resolve().parents[1]
javac = str(Path(a.jdk) / "bin/javac") if a.jdk else shutil.which("javac")
java = str(Path(a.jdk) / "bin/java") if a.jdk else shutil.which("java")
node = shutil.which("node")
if not all([javac, java, node]):
    raise SystemExit(
        "Se requieren javac/java y node; Python se comprueba por separado."
    )


def ejecutar(command):
    return subprocess.run(
        command, capture_output=True, text=True, check=True
    ).stdout.strip()


with tempfile.TemporaryDirectory(prefix="algoritmos-java-") as temp:
    files = sorted(r.glob("unidad*/ejemplos/java/*.java"))
    ejecutar(
        [javac, "-encoding", "UTF-8", "--release", "21", "-d", temp, *map(str, files)]
    )
    for f in files:
        ejecutar([java, "-cp", temp, f.stem])
        print("Java", f.stem, "OK")
    probe = Path(temp) / "ComprobarEstrategias.java"
    probe.write_text("""import java.util.*;
public class ComprobarEstrategias {
 static void comprobar(boolean ok){if(!ok)throw new AssertionError("Propiedad incumplida");}
 public static void main(String[] args){
 comprobar(GreedyCambio.cambio(new int[]{1,3,4},6).equals(List.of(4,1,1)));
 comprobar(GreedyCambio.cambio(new int[]{4,3},6)==null);
 comprobar(CambioDinamico.cambio(new int[]{1,3,4},6).equals(List.of(3,3)));
 comprobar(CambioDinamico.cambio(new int[]{2,4},3)==null);
 comprobar(CambioDinamico.cambio(new int[]{1,3},0).isEmpty());
 comprobar(BacktrackingSuma.soluciones(new int[]{2,3,5},5).equals(List.of(List.of(0,1),List.of(2))));
 comprobar(BacktrackingSuma.soluciones(new int[]{1,1},1).equals(List.of(List.of(0),List.of(1))));
 comprobar(BacktrackingSuma.soluciones(new int[]{},0).equals(List.of(List.of())));
 boolean fallo=false;try{CambioDinamico.cambio(new int[]{0},2);}catch(IllegalArgumentException e){fallo=true;}comprobar(fallo);
 int[] datos={4,1,3,1}, esperados={1,1,3,4};
 comprobar(Arrays.equals(Ordenamientos.burbuja(datos),esperados));
 comprobar(Arrays.equals(Ordenamientos.seleccion(datos),esperados));
 comprobar(Arrays.equals(Ordenamientos.insercion(datos),esperados));
 comprobar(Arrays.equals(datos,new int[]{4,1,3,1}));
 System.out.println("13 propiedades Java aprobadas");
 }}""")
    ejecutar([javac, "--release", "21", "-cp", temp, "-d", temp, str(probe)])
    print(ejecutar([java, "-cp", temp, "ComprobarEstrategias"]))
    scripts = sorted(r.glob("unidad*/ejemplos/javascript/*.js"))
    for f in scripts:
        ejecutar([node, "--check", str(f)])
        ejecutar([node, str(f)])
        print("JavaScript", f.parent.parent.parent.name, f.name, "OK")
    paths = [
        str(next(r.glob(f"unidad{n}*/ejemplos/javascript/caso_completo.js")))
        for n in [21, 22, 23]
    ]
    programa = """const assert=require('node:assert/strict');
const g=require(PATH0),b=require(PATH1),d=require(PATH2);
assert.deepEqual(g.cambioVoraz([1,3,4],6),[4,1,1]);assert.equal(g.cambioVoraz([4,3],6),null);
assert.deepEqual(d.cambioDP([1,3,4],6),[3,3]);assert.equal(d.cambioDP([2,4],3),null);assert.deepEqual(d.cambioDP([1],0),[]);
assert.deepEqual(b.subconjuntos([2,3,5],5),[[0,1],[2]]);assert.deepEqual(b.subconjuntos([1,1],1),[[0],[1]]);assert.deepEqual(b.subconjuntos([],0),[[]]);
assert.throws(()=>d.cambioDP([0],2));const o=require(PATH3),entrada=[4,1,3,1];
assert.deepEqual(o.burbuja(entrada),[1,1,3,4]);assert.deepEqual(o.seleccion(entrada),[1,1,3,4]);assert.deepEqual(o.insercion(entrada),[1,1,3,4]);assert.deepEqual(entrada,[4,1,3,1]);console.log('13 propiedades JavaScript aprobadas');"""
    paths.append(str(r/"unidad11-ordenamiento-basico/ejemplos/javascript/ordenamientos.js"))
    for i, path in enumerate(paths):
        programa = programa.replace("PATH" + str(i), json.dumps(path))
    print(ejecutar([node, "-e", programa]))
print(f"{len(files)} ejemplos Java y {len(scripts)} JavaScript ejecutados")
