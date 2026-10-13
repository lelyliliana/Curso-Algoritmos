function subconjuntos(valores, objetivo) {
  if (!Number.isSafeInteger(objetivo) || objetivo < 0 || objetivo > 10000 ||
      valores.length > 20 ||
      valores.some(v => !Number.isSafeInteger(v) || v <= 0 || v > 10000))
    throw new Error('Dominio invalido');
  const soluciones = [], elegidos = [];
  function explorar(i, suma) {
    if (suma === objetivo) {
      soluciones.push([...elegidos]);
      return;
    }
    if (i === valores.length || suma > objetivo) return;
    elegidos.push(i);
    explorar(i + 1, suma + valores[i]);
    elegidos.pop();
    explorar(i + 1, suma);
  }
  explorar(0, 0);
  return soluciones;
}
module.exports = {subconjuntos};
if (require.main === module)
  console.log(JSON.stringify(subconjuntos([2, 3, 5], 5)));
