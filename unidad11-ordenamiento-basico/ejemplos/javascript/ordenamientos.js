function burbuja(datos) {
  const a = [...datos];
  for (let limite = a.length - 1; limite > 0; limite--)
    for (let i = 0; i < limite; i++)
      if (a[i] > a[i + 1]) [a[i], a[i + 1]] = [a[i + 1], a[i]];
  return a;
}

function seleccion(datos) {
  const a = [...datos];
  for (let i = 0; i < a.length - 1; i++) {
    let menor = i;
    for (let j = i + 1; j < a.length; j++) if (a[j] < a[menor]) menor = j;
    [a[i], a[menor]] = [a[menor], a[i]];
  }
  return a;
}

function insercion(datos) {
  const a = [...datos];
  for (let i = 1; i < a.length; i++) {
    const actual = a[i];
    let j = i - 1;
    while (j >= 0 && a[j] > actual) {
      a[j + 1] = a[j];
      j--;
    }
    a[j + 1] = actual;
  }
  return a;
}
