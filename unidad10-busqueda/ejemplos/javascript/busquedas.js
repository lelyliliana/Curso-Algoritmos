function lineal(datos, objetivo) {
  for (let i = 0; i < datos.length; i++) if (datos[i] === objetivo) return i;
  return -1;
}
function binaria(datos, objetivo) {
  let izquierda = 0, derecha = datos.length - 1;
  while (izquierda <= derecha) {
    const medio = Math.floor((izquierda + derecha) / 2);
    if (datos[medio] === objetivo) return medio;
    if (datos[medio] < objetivo) izquierda = medio + 1;
    else derecha = medio - 1;
  }
  return -1;
}
const datos = [2,5,8,12,16,23,38];
console.log(lineal(datos, 16));
console.log(binaria(datos, 16));
